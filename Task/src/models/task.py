from peewee import *
from ..database.database import *;

class baseModel(Model):

    class Meta:
        database = dataBase.getInstance()
    
    def InitializeDB(self):
       dataBase.getInstance().connect()
       dataBase.getInstance().create_tables([Task])
    
class Task(baseModel):
    descryption = CharField()
    completed = BooleanField()

      



