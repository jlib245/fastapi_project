from .common import Base, Column, Integer, String, Text, DateTime, ForeignKey, relationship, JSON

class Trip(Base):
    __tablename__ = "trips"
    
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    route_id = Column(Integer, ForeignKey('routes.id'), nullable=True)
    start_time = Column(DateTime, nullable=False)
    end_time = Column(DateTime, nullable=False)
    actual_distance = Column(Integer, nullable=False)
    actual_duration = Column(Integer, nullable=False)
    gps_data = Column(JSON, nullable=False)
    
    user = relationship("User", backref="trips") # User 모델과 연결, 역참조
    route = relationship("Route", backref="trips") # Route 모델과 연결, 역참조
    