from graphql import GraphQLError
from sqlalchemy import select
import strawberry
from strawberry.types import Info
from .types import RoleCreate,RoleResponse,GetRoleMap,CreateRoleMap
from sqlalchemy.ext.asyncio import AsyncSession
from models.RoleModel import RoleMaster,RoleMapping
@strawberry.type
class Mutation:
    @strawberry.mutation
    async def create_role(self,info:Info,data:RoleCreate)->RoleResponse:
        db:AsyncSession=info.context["db"]
        results= await db.execute(select(RoleMaster).where(RoleMaster.name==data.name))
        role_exists=results.scalar()
        if role_exists:
            raise GraphQLError('role already exists')
        new_role=RoleMaster(name=data.name,desc=data.desc)
        db.add(new_role)
        await db.commit()
        await db.refresh(new_role)
        return new_role
    @strawberry.mutation
    async def create_rolemap(self,info:Info,data:CreateRoleMap)->GetRoleMap:
        db:AsyncSession=info.context["db"]
        role_mapping=RoleMapping(user_id=data.user_id,role_id=data.role_id)
        db.add(role_mapping)
        await db.commit()
        await db.refresh(role_mapping)
        return role_mapping

