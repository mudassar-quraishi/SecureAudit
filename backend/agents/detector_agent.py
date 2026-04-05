from uuid import uuid4
from typing import Any

from models import Finding, Severity


async def detector_agent(state: dict[str, Any]) -> dict[str, Any]:
    files = state.get("files", [])
    findings: list[Finding] = []

    for file in files:
        content = file["content"]
        path = file["path"]

        if "SELECT *" in content and "{" in content:
            findings.append(
                Finding(
                    id=str(uuid4()),
                    title="Potential SQL injection",
                    path=path,
                    severity=Severity.critical,
                    explanation="String interpolation used in SQL query.",
                    confidence=0.88,
                )
            )

        if "SECRET_KEY" in content:
            findings.append(
                Finding(
                    id=str(uuid4()),
                    title="Hardcoded secret",
                    path=path,
                    severity=Severity.high,
                    explanation="Secret-like value appears hardcoded in source.",
                    confidence=0.82,
                )
            )

    return {
        **state,
        "findings": findings,
        "trace": [*state.get("trace", []), f"detector_agent found {len(findings)} findings"],
    }
