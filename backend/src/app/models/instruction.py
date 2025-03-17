from common import Column, Integer, Float, String, JSON, Base, ForeignKey, relationship
class Instruction(Base):
    __tablename__ = "instructions"
    
    id = Column(Integer, primary_key=True)
    route_id = Column(Integer, ForeignKey('routes.id'), nullable=False)
    order = Column(Integer, nullable=False)
    text = Column(String, nullable=False)
    
    route = relationship("Route", backref="instructions") # Route 모델과 연결, 역참조