import strawberry


@strawberry.type
class Query:
    @strawberry.field
    async def get_user():
        return await
