import mysql.connector

db = None

def init_db():
    global db
    # criando a conexão com o banco de dados
    db =   mysql.connector.connect(
        host="localhost",
        user="root",
        password="Elisangela@77",
        database="ferramenta_db"
    )
