from select import select
from graphql import GraphQLError
import strawberry
from strawberry.types import Info
from sqlalchemy.ext.asyncio import AsyncSession
from User_service.models.UserModel import Customuser
from utils import password_context
@strawberry.mutation
async def create_user(data: Create_user,info:Info) -> User_details:  
    db: AsyncSession = info.context["db"]
    users=Customuser(name=data.name,mobilenumber=data.mobilenumber)
    db.add(users)
    await db.commit()
    await db.refresh(users)
    return users
