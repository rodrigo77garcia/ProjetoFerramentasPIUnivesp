import mysql.connector

def create_database():
    # Conecta ao servidor MySQL
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Elisangela@77"     
    )

    # Cria um cursor para executar comandos SQL
    cursor = connection.cursor()

    # Verifica se o banco de dados já existe
    cursor.execute("SHOW DATABASES LIKE 'ferramenta_db'")
    db_exists = cursor.fetchone()

    if db_exists:
        print("O banco de dados 'ferramenta_db' já existe.")
    else:
        # Comando SQL para criar o banco de dados
        create_database_query = "CREATE DATABASE ferramenta_db"

        # Executa o comando SQL para criar o banco de dados
        cursor.execute(create_database_query)
        print("Banco de dados 'ferramenta_db' criado com sucesso.")

    # Fecha o cursor e a conexão
    cursor.close()
    connection.close()

def create_tables():
    # Conecta ao banco de dados 'ferramenta_db'
    connection = mysql.connector.connect(
        host="localhost",
        user="seu_usuario",       # Substitua 'seu_usuario' pelo seu usuário MySQL
        password="sua_senha",     # Substitua 'sua_senha' pela sua senha MySQL
        database="ferramenta_db"
    )

    # Cria um cursor para executar comandos SQL
    cursor = connection.cursor()

    # Comando SQL para criar a tabela 'ferramentas'
    create_table_query = """
    CREATE TABLE IF NOT EXISTS ferramentas (
        id INT AUTO_INCREMENT PRIMARY KEY,
        nome VARCHAR(30) NOT NULL,
        local VARCHAR(30),
        descricao VARCHAR(50),
        marca VARCHAR(50),
        data_do_emprestimo DATE,
        data_da_devolucao DATE,
        nome_funcionario VARCHAR(30) NOT NULL,
        setor_de_trabalho VARCHAR(30),
        imagem VARCHAR(30)
    )
    """

    # Executa o comando SQL para criar a tabela 'ferramentas'
    cursor.execute(create_table_query)

    # Commit para salvar as alterações no banco de dados
    connection.commit()

    # Fecha o cursor e a conexão
    cursor.close()
    connection.close()

# Chama as funções para criar o banco de dados e as tabelas
create_database()
create_tables()

print("Processo de criação de banco de dados e tabelas concluído.")
