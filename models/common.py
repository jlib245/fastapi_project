from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship

import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from database import Base