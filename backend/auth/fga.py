import httpx

from config import settings


RELATION_MAP = {
    "read": "can_read",
    "write": "can_write",
    "delete": "can_delete",
}


async def check_permission(user_id: str, file_path: str, action: str) -> bool:
    relation = RELATION_MAP[action]
    payload = {
        "tuple_key": {
            "user": f"user:{user_id}",
            "relation": relation,
            "object": f"file:{file_path}",
        },
        "authorization_model_id": settings.openfga_model_id,
    }

    headers = {"Content-Type": "application/json"}
    url = f"{settings.openfga_api_url}/stores/{settings.openfga_store_id}/check"

    async with httpx.AsyncClient(timeout=10) as client:
        response = await client.post(url, headers=headers, json=payload)

    response.raise_for_status()
    data = response.json()
    return bool(data.get("allowed", False))
