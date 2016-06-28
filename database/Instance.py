from sqlalchemy import Integer, Column, create_engine, ForeignKey, String, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

from database.base import Base


class Instance(Base):
    __tablename__ = 'instance'
    id = Column(Integer, primary_key = True)
    status = Column(String(50))
    create_at = Column (DateTime)
    finalized_at =  Column (DateTime)
    wed_flow_id = Column(Integer, ForeignKey('wed_flow.id'))
    wed_flow = relationship('WED_flow', back_populates='instance')
    wed_state = relationship('WED_state', back_populates='instance')
    interruption = relationship('Interruption', back_populates='instance')
    history_entry = relationship('History_entry', back_populates='instance')
