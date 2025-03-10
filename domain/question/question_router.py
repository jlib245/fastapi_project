from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from database import get_db
from models import Question


router = APIRouter(
    prefix="/api/question",
)

@router.get("/list")
def question_list(db: Session = Depends(get_db)):
    _question_list = db.query(Question).all()
    return _question_list