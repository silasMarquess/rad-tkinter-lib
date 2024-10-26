from peewee import *
import os;
from dotenv import load_dotenv


class dataBase():
    load_dotenv();
    __db : None;
    @staticmethod
    def getInstance():
       dataBase.__db = PostgresqlDatabase(os.getenv('DATABASE'),
                                          user=os.getenv('DB_USER'),
                                          password=os.getenv('PASSWORD'),
                                          host=os.getenv('END_POINT'),
                                          port=os.getenv('PORT'))
       return dataBase.__db;
     
   
    

