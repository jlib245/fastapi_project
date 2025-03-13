from .common import *

class User(Base):
    __tablename__ = "users" #관리되는 table 이름
    
    id = Column(Integer, primary_key=True) 
    username = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)