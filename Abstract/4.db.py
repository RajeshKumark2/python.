from abc import ABC, abstractmethod 

class DatabaseConnection(ABC):
    @abstractmethod
    def connect(self): 
        pass 

    @abstractmethod
    def disconnect(self): 
        pass

    @abstractmethod 
    def excute_query(self, query): 
        pass 

class MySQLConnection(DatabaseConnection):
    def connect(self):
        print("Connecting to Mysql DB")

    def disconnect(self):
        print("Disconnecting from MySQL DB")

    def excute_query(self, query):
        print(f"Excuting MySQL Query: {query}")

class MongoDBConecction(DatabaseConnection): 
    def connect(self):
        print("Connecting to MongoDB")

    def disconnect(self): 
        print("Disconnecting from MongoDB")

    def excute_query(self, query): 
        print(f"Excuting MongoDB query: {query}")

def rnu_db(db:DatabaseConnection): 
    db.connect() 
    db.excute_query("SELECT * FROM users")
    db.disconnect()

rnu_db(MySQLConnection())
rnu_db(MongoDBConecction())
