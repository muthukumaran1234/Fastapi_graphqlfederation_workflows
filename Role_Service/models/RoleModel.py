from sqlalchemy import Column,Integer,String,Boolean
from config.database import Base
class RoleMaster(Base):
    __tablename__="rolemaster"
    id=Column(Integer,primary_key=True)
    name=Column(String,nullable=False,unique=True)
    desc=Column(String,nullable=True)
    is_active=Column(Boolean,default=True)   


class RoleMapping(Base):
    __tablename__="rolemapping"
    id=Column(Integer,primary_key=True)
    user_id=Column(Integer,nullable=False)
    role_id=Column(Integer,nullable=False)
