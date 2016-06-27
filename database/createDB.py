from database.DAO import *
from database.Readxml import *

dao = DAO()

dao.drop_tables()
dao.create_tables()
dao.insert()