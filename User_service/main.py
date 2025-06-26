from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter



app = FastAPI()

app.include_router()