import strawberry
from api.mutation import Mutation
from api.query import Query
from api.types import *
schema=strawberry.federation.Schema(query=Query,mutation=Mutation,types=[UserType])