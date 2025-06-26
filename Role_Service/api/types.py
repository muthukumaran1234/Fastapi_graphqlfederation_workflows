import strawberry

@strawberry.input
class RoleCreate:
    name:str
    desc:str
@strawberry.type
class RoleResponse:
    id:int
    name:str
    desc:str
@strawberry.input
class CreateRoleMap:
    user_id:int
    role_id:int
@strawberry.type
class GetRoleMap:
    id:int
    user_id:int
    role_id:int
    