from common import *

class Question(Base):
    __tablename__ = "questions" #관리되는 table 이름
    
    id = Column(Integer, primary_key=True) # 고유번호(정수, 기본기 = T)
    subject = Column(String, nullable=False) # 제목(문자열, null 허용 X)
    content = Column(Text, nullable=False) # 내용(텍스트, null 허용 X)
    create_date = Column(DateTime, nullable=False) # 작성일(날짜, null 허용 X)