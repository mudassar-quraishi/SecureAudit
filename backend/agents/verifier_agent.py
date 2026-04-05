from typing import Any


async def verifier_agent(state: dict[str, Any]) -> dict[str, Any]:
    findings = state.get("findings", [])
    verified = [finding for finding in findings if finding.confidence >= 0.8]

    return {
        **state,
        "verified_findings": verified,
        "trace": [*state.get("trace", []), f"verifier_agent kept {len(verified)} findings"],
    }
