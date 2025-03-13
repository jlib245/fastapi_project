'''
from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Question(Base):
    __tablename__ = "questions" #관리되는 table 이름
    
    id = Column(Integer, primary_key=True) # 고유번호(정수, 기본기 = T)
    subject = Column(String, nullable=False) # 제목(문자열, null 허용 X)
    content = Column(Text, nullable=False) # 내용(텍스트, null 허용 X)
    create_date = Column(DateTime, nullable=False) # 작성일(날짜, null 허용 X)
    
class Answer(Base):
    __tablename__ = "answers"
    
    id = Column(Integer, primary_key=True)
    content = Column(Text, nullable=False)
    create_date = Column(DateTime, nullable=False)
    question_id = Column(Integer, ForeignKey("questions.id")) # ForeignKey(참조할 테이블.참조할 컬럼 {외부 키}) : 모델 연결
    question = relationship("Question", backref="answers") # Question 모델과 연결, 역참조조
'''