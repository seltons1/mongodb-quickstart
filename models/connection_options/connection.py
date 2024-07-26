from .mongo_db_configs import mongo_db_info
from pymongo import MongoClient

class Connection():

    def __init__(self) -> None:
        
        self.__connection_string = f"""mongodb://{mongo_db_info['USER']}:{mongo_db_info['PASSWORD']}@{mongo_db_info['HOST']}:{mongo_db_info['PORT']}/?authSource=admin"""
        self.__database_name = mongo_db_info["DB_NAME"]
        self.__client = None
        self.__db_connection = None

    def connect(self):
        self.__client = MongoClient(self.__connection_string)
        self.__db_connection = self.__client[self.__database_name]
    
    def get_db_connection(self):
        return self.__db_connection
    
    def get_db_client(self):
        return self.__client


