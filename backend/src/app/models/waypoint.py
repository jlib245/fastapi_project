from common import Column, Integer, String, Base, ForeignKey, relationship

class Waypoint(Base):
    __tablename__ = "waypoints"
    
    id = Column(Integer, primary_key=True)
    route_id = Column(Integer, ForeignKey('routes.id'), nullable=False)
    text = Column(String, nullable=False)
    order = Column(Integer, nullable=False)
    
    route = relationship("Route", backref="waypoints") # Route 모델과 연결, 역참조