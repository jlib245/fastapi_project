from passlib.context import CryptContext
from sqlalchemy.orm import Session

from ..models import User
from ..schema.user_schema import UserCreate

pwd_context = CryptContext(schemes=["bcrypt"], deprecated = "auto")

def create_user(db: Session, user_create: UserCreate):
    db_user = User(username=user_create.username,
                   password=pwd_context.hash(user_create.password1),
                   email=user_create.email)
    db.add(db_user)
    db.commit()
    
def get_existing_user(db:Session, usercreate:UserCreate):
    return db.query(User).filter(
            (User.username == usercreate.username) |
            (User.email == usercreate.email)
            ).first()
    
    
def get_user(db:Session, username:str):
    return db.query(User).filter(User.username == username).first()