from sqlalchemy import select
import strawberry
from strawberry.types import Info
from .types import RoleResponse,GetRoleMap
from sqlalchemy.ext.asyncio import AsyncSession
from models.RoleModel import RoleMaster,RoleMapping
from typing import Optional,List
@strawberry.type
class Query:
    @strawberry.field
    async def get_role(info:Info,id:Optional[int]=None)->List[RoleResponse]:
        db:AsyncSession=info.context["db"]
        if id :
            results=await db.execute(select(RoleMaster).select(RoleMaster.id==id))
        else:
            results=await db.execute(select(RoleMaster))
        roles=results.scalars().all()
        return roles

    @strawberry.field
    async def get_role_maps(info:Info)->List[GetRoleMap]:
        db:AsyncSession=info.context["db"]
        
        results=await db.execute(select(RoleMapping))
        role_maps=results.scalars().all()
        return role_maps