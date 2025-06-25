from sqlalchemy.ext.asyncio import AsyncSession,create_async_engine,async_sessionmaker
from sqlalchemy.orm import declarative_base
import asyncpg
Base = declarative_base()

DATABASEURL = "postgresql+asyncpg://postgres:postgres@localhost:5432/fastapi_federation"

engine = create_async_engine(DATABASEURL)

Sessionlocal = async_sessionmaker(bind=engine,expire_on_commit=False,class_=AsyncSession)

async def get_connection():
    async with Sessionlocal() as session:
        yield session
        
async def get_context():
    db = get_connection
    return {"db":db}

