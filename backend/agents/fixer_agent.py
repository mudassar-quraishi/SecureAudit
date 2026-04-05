from typing import Any

from models import PatchSuggestion


async def fixer_agent(state: dict[str, Any]) -> dict[str, Any]:
    patches: list[PatchSuggestion] = []

    for finding in state.get("verified_findings", []):
        if finding.title == "Potential SQL injection":
            patches.append(
                PatchSuggestion(
                    path=finding.path,
                    diff="- query = f\"SELECT * FROM users WHERE email = '{email}'\"\n+ query = \"SELECT * FROM users WHERE email = %s\"\n+ cursor.execute(query, (email,))",
                    reason="Parameterized query prevents injection.",
                )
            )

        if finding.title == "Hardcoded secret":
            patches.append(
                PatchSuggestion(
                    path=finding.path,
                    diff="- SECRET_KEY = 'hardcoded-secret'\n+ SECRET_KEY = os.getenv('SECRET_KEY')",
                    reason="Read secret from runtime environment, not source code.",
                )
            )

    return {
        **state,
        "patches": patches,
        "trace": [*state.get("trace", []), f"fixer_agent generated {len(patches)} patches"],
    }
