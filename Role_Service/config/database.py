from sqlalchemy.ext.asyncio import AsyncSession,create_async_engine,async_sessionmaker
from sqlalchemy.orm import declarative_base
import asyncpg
Base = declarative_base()

DATABASEURL = "postgresql+asyncpg://postgres.bhgwklwkscjowaxpcbrl:DatayaanMedyaan@aws-0-ap-south-1.pooler.supabase.com:5432/postgres"

engine = create_async_engine(DATABASEURL)

Sessionlocal = async_sessionmaker(bind=engine,expire_on_commit=False,class_=AsyncSession)

async def get_connection():
    async with Sessionlocal() as session:
        yield session
# print(get_connection,"-----------------------connection")
async def get_context():
    async with Sessionlocal() as session:
        return {"db":session}
    
# print(get_context,"--------------------------context")

