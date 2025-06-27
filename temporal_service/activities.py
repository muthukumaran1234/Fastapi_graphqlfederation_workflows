import httpx
from temporalio import activity

# Using host.docker.internal to access localhost from inside Docker (works on Windows/macOS)
USER_URL = "http://host.docker.internal:8001/graphql"
ROLE_URL = "http://host.docker.internal:8002/graphql"


async def call_graphql(url, query, variables):
    async with httpx.AsyncClient() as client:
        response = await client.post(url, json={"query": query, "variables": variables})
        response.raise_for_status()
        return response.json()


@activity.defn
async def create_user(user_data: dict) -> int:
    result = await call_graphql(
        USER_URL,
        "mutation($i: UserInput!) { createUser(input: $i) { id } }",
        {"i": user_data}
    )
    return result["data"]["createUser"]["id"]


@activity.defn
async def assign_role(user_id: int, role_id: int) -> bool:
    result = await call_graphql(
        ROLE_URL,
        "mutation($input: RoleMapInput!) { createRoleMap(input: $input) { id } }",
        {"input": {"user_id": user_id, "role_id": role_id}}
    )
    return "data" in result and "createRoleMap" in result["data"]
