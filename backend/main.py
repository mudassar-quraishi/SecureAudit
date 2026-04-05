from uuid import uuid4

from fastapi import FastAPI, HTTPException

from auth.ciba import request_step_up_approval
from graph import run_audit_pipeline
from models import ApprovalRequest, AuditAction, AuditEvent, RepoScanRequest, ScanResult
from store import APPROVALS, AUDIT_LOG, POLICIES, SCANS

app = FastAPI(title="SecureAudit API", version="0.1.0")


@app.get("/health")
async def health() -> dict:
    return {"ok": True, "service": "secureaudit-backend"}


@app.post("/api/scans", response_model=ScanResult)
async def create_scan(payload: RepoScanRequest) -> ScanResult:
    state = await run_audit_pipeline(payload.user_id, payload.repo, payload.branch)
    scan_id = str(uuid4())

    result = ScanResult(
        scan_id=scan_id,
        repo=payload.repo,
        findings=state.get("verified_findings", []),
        patches=state.get("patches", []),
        status="completed",
    )
    SCANS[scan_id] = result.model_dump()

    AUDIT_LOG.append(
        AuditEvent(
            user_id=payload.user_id,
            agent="orchestrator",
            action=AuditAction.analyze,
            repo=payload.repo,
            metadata={"scan_id": scan_id, "trace": state.get("trace", [])},
        )
    )

    return result


@app.get("/api/scans")
async def list_scans() -> dict:
    return {"items": list(SCANS.values())}


@app.post("/api/approvals")
async def request_approval(payload: ApprovalRequest) -> dict:
    approval_id = str(uuid4())
    APPROVALS[approval_id] = {
        "approval_id": approval_id,
        "user_id": payload.user_id,
        "action": payload.action,
        "repo": payload.repo,
        "payload": payload.payload,
        "status": "pending",
    }

    response = await request_step_up_approval(payload.user_id, payload.action, payload.repo, payload.payload)
    APPROVALS[approval_id]["ciba"] = response

    AUDIT_LOG.append(
        AuditEvent(
            user_id=payload.user_id,
            agent="verifier",
            action=AuditAction.approval_request,
            repo=payload.repo,
            metadata={"approval_id": approval_id, "action": payload.action},
        )
    )

    return APPROVALS[approval_id]


@app.get("/api/approvals/{approval_id}")
async def get_approval(approval_id: str) -> dict:
    approval = APPROVALS.get(approval_id)
    if not approval:
        raise HTTPException(status_code=404, detail="Approval not found")
    return approval


@app.get("/api/policies/{user_id}")
async def get_policies(user_id: str) -> dict:
    return {"user_id": user_id, "rules": POLICIES[user_id]}


@app.put("/api/policies/{user_id}")
async def upsert_policies(user_id: str, rules: dict) -> dict:
    POLICIES[user_id] = rules
    return {"ok": True, "user_id": user_id, "rules": rules}


@app.get("/api/audit")
async def get_audit_log() -> dict:
    return {"items": [event.model_dump() for event in AUDIT_LOG]}
