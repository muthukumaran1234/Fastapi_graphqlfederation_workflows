from select import select
import strawberry
from strawberry.types import Info
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List,Optional
from api.types import *

from models.UserModel import Customuser
@strawberry.type
class Query:
    @strawberry.field
    async def get_users(info:Info,id:Optional[int]=None) -> List[UserType]:
        db:AsyncSession=info.context["db"]
       
        if id:
            result = await db.execute(select(Customuser).where(Customuser.id==id))
        else:
            result = await db.execute(select(Customuser))
        users = result.scalars().all()
        return users

