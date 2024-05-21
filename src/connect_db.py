from sqlalchemy import create_engine

def connect():
    database = create_engine('mysql+mysqlconnector://eric:eric@localhost:3306/clientes')
    print("Connected to MySQL database successfully.")
    return database