from typing import Any


async def parser_agent(state: dict[str, Any]) -> dict[str, Any]:
    # In production, fetch repository tree and file blobs from GitHub API.
    repo = state["repo"]
    sample_files = [
        {"path": "src/auth.py", "content": "query = f\"SELECT * FROM users WHERE email = '{email}'\""},
        {"path": "src/config.py", "content": "SECRET_KEY = 'hardcoded-secret'"},
    ]
    return {
        **state,
        "files": sample_files,
        "trace": [*state.get("trace", []), f"parser_agent parsed {repo}"],
    }
