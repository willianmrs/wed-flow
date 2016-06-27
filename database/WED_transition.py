from sqlalchemy import Integer, Column, create_engine, ForeignKey, String
from sqlalchemy.orm import relationship, Session
from sqlalchemy.ext.declarative import declarative_base
from database.Associations import *
from database.History_entry import *
from database.WED_trigger import *

from database.base import Base


class WED_transition(Base):
    __tablename__ = 'wed_transition'
    id = Column(Integer, primary_key = True)
    name = Column(String(50))
    history_entry = relationship("History_entry", back_populates="wed_transition")
    wed_trigger = relationship("WED_trigger", back_populates="wed_transition")
