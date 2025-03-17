from .common import Column, Integer, Base, ForeignKey, JSON, Float, relationship

class Route(Base):
    __tablename__ = "routes" #관리되는 table 이름
    
    id = Column(Integer, primary_key=True) 
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    start_location = Column(JSON, nullable=False) # {lat: 37.123, lng: 127.123}
    end_location = Column(JSON, nullable=False)
    total_distance = Column(Float, nullable=False)
    total_time = Column(Float, nullable=False)
    
    user = relationship("User", backref="routes") # User 모델과 연결, 역참조
    waypoints = relationship("Waypoint", backref="routes", cascade="all, delete-orphan") # Waypoint 모델과 연결, 역참조
    instructions = relationship("Instruction", backref="routes", cascade="all, delete-orphan") # Instruction 모델과 연결, 역참조
    trip = relationship("Trip", backref="routes") # Trip 모델과 연결, 역참조