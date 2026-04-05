from datetime import datetime, timedelta, timezone
import uuid

import httpx
import jwt

from config import settings


async def exchange_for_github_token(user_id: str, scope: str) -> str:
    """Exchange user subject for short-lived GitHub token via Auth0 Token Vault."""
    with open(settings.auth0_private_key_path, "r", encoding="utf-8") as file:
        private_key = file.read()

    now = datetime.now(timezone.utc)
    client_assertion = jwt.encode(
        {
            "iss": settings.auth0_client_id,
            "sub": settings.auth0_client_id,
            "aud": f"https://{settings.auth0_domain}/oauth/token",
            "iat": int(now.timestamp()),
            "exp": int((now + timedelta(minutes=5)).timestamp()),
            "jti": str(uuid.uuid4()),
        },
        private_key,
        algorithm="RS256",
    )

    payload = {
        "grant_type": "urn:ietf:params:oauth:grant-type:token-exchange",
        "client_id": settings.auth0_client_id,
        "client_assertion_type": "urn:ietf:params:oauth:client-assertion-type:jwt-bearer",
        "client_assertion": client_assertion,
        "subject_token": user_id,
        "subject_token_type": "urn:auth0:params:oauth:token-type:user-id",
        "requested_token_type": "urn:auth0:params:oauth:token-type:access-token",
        "scope": scope,
        "audience": settings.auth0_audience,
    }

    async with httpx.AsyncClient(timeout=15) as client:
        response = await client.post(f"https://{settings.auth0_domain}/oauth/token", data=payload)

    response.raise_for_status()
    data = response.json()
    return data["access_token"]
