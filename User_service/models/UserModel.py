from sqlalchemy import Column,Integer,String,Boolean
from config.database import Base

class Customuser(Base):
    __tablename__ = "customuser"
    id = Column(Integer,primary_key=True)
    name = Column(String,nullable=False)
    mobilenumber = Column(String,nullable=False)
    is_active = Column(Boolean,default=True)