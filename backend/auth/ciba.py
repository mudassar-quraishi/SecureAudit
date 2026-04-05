import httpx

from config import settings


async def request_step_up_approval(user_id: str, action: str, repo: str, payload: dict) -> dict:
    """Create a CIBA auth request for high-impact actions."""
    ciba_payload = {
        "scope": "openid profile write:repo",
        "login_hint": user_id,
        "binding_message": f"SecureAudit wants to {action} in {repo}",
        "requested_expiry": 300,
        "acr_values": "http://schemas.openid.net/pape/policies/2007/06/multi-factor",
        "user_code": payload.get("scan_id", "secureaudit"),
    }

    async with httpx.AsyncClient(timeout=15) as client:
        response = await client.post(
            f"https://{settings.auth0_domain}/oauth/ciba",
            data=ciba_payload,
            auth=(settings.auth0_client_id, settings.auth0_client_secret),
        )

    response.raise_for_status()
    return response.json()


async def poll_ciba_result(auth_req_id: str, interval_seconds: int = 2) -> dict:
    """Poll token endpoint until approval is granted or denied."""
    payload = {
        "grant_type": "urn:openid:params:grant-type:ciba",
        "auth_req_id": auth_req_id,
        "client_id": settings.auth0_client_id,
        "client_secret": settings.auth0_client_secret,
    }

    async with httpx.AsyncClient(timeout=15) as client:
        response = await client.post(
            f"https://{settings.auth0_domain}/oauth/token",
            data=payload,
        )

    if response.status_code in (400, 401):
        return {"status": "pending_or_denied", "detail": response.json()}

    response.raise_for_status()
    return {"status": "approved", "token_response": response.json()}
