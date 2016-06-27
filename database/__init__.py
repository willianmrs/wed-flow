from database.DAO import *
from database.Readxml import *

dao = DAO()
readxml = Readxml('xml/B1.xml')

Readxml.dao = dao
DAO.readxml = readxml