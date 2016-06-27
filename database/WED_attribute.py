from sqlalchemy import Integer, Column, create_engine, ForeignKey, String
from sqlalchemy.orm import relationship, Session
from database.base import Base

class WED_attribute(Base):
    __tablename__ = 'wed_attribute'
    id = Column(Integer, primary_key = True)
    name = Column(String(50))
    type_ = Column(String(50))
