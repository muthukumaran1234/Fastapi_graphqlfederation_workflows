import strawberry
from models.RoleModel import RoleMapping, RoleMaster
from sqlalchemy import select
from typing import List
@strawberry.input
class RoleCreate:
    name: str
    desc: str


@strawberry.type
class  RoleResponse:
    id: int
    name: str
    desc: str


@strawberry.input
class CreateRoleMap:
    user_id: int
    role_id: int


@strawberry.federation.type(keys=["id"], extend=True)
class UserType:
    id: strawberry.ID

    @strawberry.field
    async def roles(self, info: strawberry.Info) -> List[RoleResponse]:
        db=info.context["db"]
        users = (await db.execute(select(RoleMapping).where(RoleMapping.user_id==int(self.id)))).scalars().all()
        role_ids = [r.role_id for r in users]
        roles_data = (await db.execute(select(RoleMaster).where(RoleMaster.id==role_ids))).scalars().all()
        
        
@strawberry.type
class GetRoleMap:
    id: int
    user_id: int
    role_id: int

    @strawberry.field
    async def user(self) -> UserType:
        return UserType(id=str(self.user_id))

    @strawberry.field
    async def role(self, info: strawberry.Info) -> RoleResponse:
        db = info.context["db"]
        role = await db.get(RoleMaster, self.role_id)
        return RoleResponse(id=role.id, name=role.name, desc=role.desc)
