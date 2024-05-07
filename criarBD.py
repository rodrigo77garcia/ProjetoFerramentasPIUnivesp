# importando sql lite para criar nosso banco de dados
import sqlite3 as lite

# criando a conexão com o banco de dados
con = lite.connect('dados_ferramentas.db')

# criando tabela
with con:
    cur = con.cursor()
    cur.execute("CREATE TABLE INVETARIO(id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT, local TEXT, descricao TEXT, marca TEXT, data_do_emprestimo DATE,  data_da_devolucao DATE, nome_funcionario TEXT, setor_de_trabalho TEXT, imagem TEXT)")
    