import mysql.connector
from flask import current_app, g

def init_db():
    try:
        db = mysql.connector.connect(
            host=current_app.config['MYSQL_HOST'],
            user=current_app.config['MYSQL_USER'],
            password=current_app.config['MYSQL_PASSWORD']
        )
        cursor = db.cursor()

        # Criar banco de dados
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {current_app.config['MYSQL_DB']}")

        # Selecionar o banco de dados
        db.database = current_app.config['MYSQL_DB']

        # Criar tabelas (se necessário)
        cursor.execute('''CREATE TABLE IF NOT EXISTS ferramentas (
                            id INT AUTO_INCREMENT PRIMARY KEY,
                            nome VARCHAR(255),
                            local VARCHAR(255),
                            descricao TEXT,
                            marca VARCHAR(255),
                            data_do_emprestimo DATE,
                            data_da_devolucao DATE,
                            nome_funcionario VARCHAR(255),
                            setor_de_trabalho VARCHAR(255),
                            imagem VARCHAR(255)
                        )''')

        db.commit()
        cursor.close()
        db.close()
    except mysql.connector.Error as err:
        print(f"Erro: {err}")

def get_db():
    if 'db' not in g:
        g.db = mysql.connector.connect(
            host=current_app.config['MYSQL_HOST'],
            user=current_app.config['MYSQL_USER'],
            password=current_app.config['MYSQL_PASSWORD'],
            database=current_app.config['MYSQL_DB']
        )
    return g.db

def close_db(e=None):
    db = g.pop('db', None)
    if db is not None:
        db.close()
