from models.connection_options.connection import Connection


connection = Connection()

print(connection.get_db_connection())

connection.connect()

print(connection.get_db_connection())

