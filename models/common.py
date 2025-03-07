from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship

import os
current_file_path = os.path.abspath(__file__)
current_dir = os.path.dirname(current_file_path)
project_dir = os.path.dirname(current_dir)

os.chdir(project_dir)

from db.database import Base
