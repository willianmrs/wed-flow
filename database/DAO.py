from sqlalchemy.engine.url import URL
from sqlalchemy import Integer, Column, create_engine, ForeignKey, String
from sqlalchemy.orm import relationship, Session
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
import database.settings
from database.base import Base

from database import Associations
class DAO:
    readxml = None

    def __init__(self):
        self.engine = create_engine(URL(**database.settings.DATABASE))
        self.session = sessionmaker(bind=self.engine)()  

    def __del__(self):
        self.session.close_all()


    def create_tables(self):
        attr = DAO.readxml.data_wed_attributes()
        attributes = {}

        for name, type_ in attr.items():
            if type_ == 'string':
                attributes[name] = Column(String(50))
            else:
                attributes[name] = Column(Integer)


        wed_state_colums = {
            '__tablename__' : 'wed_state',
            'id' : Column(Integer, primary_key = True),
            'instance_id' : Column(Integer, ForeignKey('instance.id')),
            'instance' : relationship("Instance", back_populates="wed_state"),
            'wed_trigger' : relationship("WED_trigger", secondary=Associations.wedState_wedTrigger, back_populates="wed_state"),
            'history_entry' : relationship("History_entry", uselist=False, back_populates="wed_state")
        }

        wed_state_colums = dict(list(wed_state_colums.items()) + list(attributes.items()))

        wed_state = type('WED_state', (Base,), wed_state_colums)
        import database.Interruption
        import database.History_entry
        import database.Instance
        import database.WED_attribute
        import database.WED_condition
        import database.WED_flow 
        import database.WED_transition
        import database.WED_trigger
        Base.metadata.create_all(self.engine)





# Testar
    def select_condition(self, wed_condition):
        result = self.session.execute(
            "SELECT id FROM wed_condition WHERE name = '" + wed_condition + "'"
        ).fetchone()
        return result

    def select_transition(self, wed_transition):
        result = self.session.execute(
            "SELECT id FROM wed_transition WHERE name = '" + wed_transition + "'"
        ).fetchone()
        return result

    def select_flow(self, wed_flow):
        result = self.session.execute(
            "SELECT id FROM wed_flow WHERE name = '" + wed_flow + "'"
        ).fetchone()
        return result        