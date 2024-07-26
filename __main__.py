from pymongo import MongoClient

## starting with mongoDB

connection_string = "mongodb://admin:password@localhost:27017/?authSource=admin"
client = MongoClient(connection_string)
db_connection = client["myDatabase"]

print(db_connection)
print()

collection = db_connection.get_collection("myCollection")

print(collection)
print()

collection.insert_one({
    "name" : "Ashley",
    "age" : 16 

})
