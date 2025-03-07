from common import *
class Answer(Base):
    __tablename__ = "answers"
    
    id = Column(Integer, primary_key=True)
    content = Column(Text, nullable=False)
    create_date = Column(DateTime, nullable=False)
    question_id = Column(Integer, ForeignKey("questions.id")) # ForeignKey(참조할 테이블.참조할 컬럼 {외부 키}) : 모델 연결
    question = relationship("Question", backref="answers") # Question 모델과 연결, 역참조조