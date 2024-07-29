from models.connection_options.connection import Connection


connection = Connection()
connection.connect()
conn = connection.get_db_connection()
collection = conn.get_collection("myCollection")