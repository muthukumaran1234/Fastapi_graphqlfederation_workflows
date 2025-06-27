import strawberry
from models.UserModel import Customuser


@strawberry.input
class UserInput:
    id: int
    name: str
    mobilenumber: str
    is_active: bool


@strawberry.federation.type(keys=["id"])
class UserType:
    id: strawberry.ID
    name: str
    mobilenumber: str
    is_active: bool

    @classmethod
    async def resolve_reference(cls, id: strawberry.ID, info: strawberry.Info) -> "UserType":
        db = info.context["db"]
        user = await db.get(Customuser, id)
        return UserType(
            id=user.id,
            name=user.name,
            mobilenumber=user.mobilenumber,
            is_active=user.is_active
        )
    
    # @strawberry.field
    # async def roles():