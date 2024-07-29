from models.connection_options.connection import Connection
from faker import Faker

connection = Connection()
connection.connect()
conn = connection.get_db_connection()
collection = conn.get_collection("myCollection")

data = {
        "name" : "Susan",
        "age" : "54"
    }

faker = Faker('en_US')
i = 0
data_many = []
while i < 100:

    name = faker.name()
    age = faker.random_int(min=1, max=100)

    data_many.append({
        "name" : name,
        "age" : age
    })
    
    i += 1

def insert_one(collection, data):

    collection.insert_one(data)
    
def insert_many(collection, data):

    collection.insert_many(data)


#insert_one(collection=collection, data=data)
insert_many(collection=collection,data=data_many)