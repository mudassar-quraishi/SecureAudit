from typing import TypedDict, Any

from agents.parser_agent import parser_agent
from agents.detector_agent import detector_agent
from agents.verifier_agent import verifier_agent
from agents.fixer_agent import fixer_agent


class AuditState(TypedDict, total=False):
    user_id: str
    repo: str
    branch: str
    files: list[dict[str, str]]
    findings: list[Any]
    verified_findings: list[Any]
    patches: list[Any]
    trace: list[str]


async def run_audit_pipeline(user_id: str, repo: str, branch: str = "main") -> AuditState:
    state: AuditState = {
        "user_id": user_id,
        "repo": repo,
        "branch": branch,
        "trace": [],
    }

    state = await parser_agent(state)
    state = await detector_agent(state)
    state = await verifier_agent(state)
    state = await fixer_agent(state)

    return state
