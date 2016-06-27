from sqlalchemy import Table, Column, Integer, ForeignKey

from database.base import Base

wedState_wedTrigger = Table('wedState_wedTrigger', Base.metadata,
    Column('wed_state_id', Integer, ForeignKey('wed_state.id'), primary_key=True),
    Column('wed_trigger_id', Integer, ForeignKey('wed_trigger.id'), primary_key=True)
)
