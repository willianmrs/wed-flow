from database.DAO import *
from database.Readxml import *
import database.settings

dao = DAO()
readxml = Readxml('xml/B1.xml')
readxml.set_dao(dao)
dao.set_readxml(readxml)

dao.create_tables()
dao.insert()