from fastapi import FastAPI
from config.database import get_context
from api.schemas import schema
from strawberry.fastapi import GraphQLRouter

role=GraphQLRouter(schema,context_getter=get_context)

app = FastAPI()

app.include_router(role,prefix='/graphql')