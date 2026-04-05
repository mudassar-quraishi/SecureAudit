from datetime import datetime
from enum import Enum
from pydantic import BaseModel, Field


class Severity(str, Enum):
    low = "LOW"
    medium = "MEDIUM"
    high = "HIGH"
    critical = "CRITICAL"


class AuditAction(str, Enum):
    read = "READ"
    analyze = "ANALYZE"
    verify = "VERIFY"
    patch = "PATCH"
    approval_request = "APPROVAL_REQUEST"
    write = "WRITE"


class RepoScanRequest(BaseModel):
    user_id: str
    repo: str = Field(description="owner/name")
    branch: str = "main"


class Finding(BaseModel):
    id: str
    title: str
    path: str
    severity: Severity
    explanation: str
    confidence: float


class PatchSuggestion(BaseModel):
    path: str
    diff: str
    reason: str


class ScanResult(BaseModel):
    scan_id: str
    repo: str
    findings: list[Finding]
    patches: list[PatchSuggestion]
    status: str


class ApprovalRequest(BaseModel):
    user_id: str
    action: str
    repo: str
    payload: dict


class ApprovalDecision(BaseModel):
    approval_id: str
    approved: bool
    decided_at: datetime = Field(default_factory=datetime.utcnow)


class AuditEvent(BaseModel):
    timestamp: datetime = Field(default_factory=datetime.utcnow)
    user_id: str
    agent: str
    action: AuditAction
    repo: str
    metadata: dict = Field(default_factory=dict)
