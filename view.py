# importando sql lite para criar nossa view
import sqlite3 as lite


# criando a conexão com o banco de dados
con = lite.connect('dados_ferramentas.db')

#CRUD



# inserir dados na tabela
def inserir_form(i):
    with con: 
        cur = con.cursor()
        query = "INSERT INTO INVETARIO(nome, local, descricao, marca, data_do_emprestimo, data_da_devolucao, nome_funcionario, setor_de_trabalho, imagem) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?)"
        cur.execute(query, i)

    
# atualizar dados na tabela 
def atualizar_form(i):   
    with con: 
        cur = con.cursor()
        query = "UPDATE INVETARIO SET nome=?, local=?, descricao=?, marca=?, data_do_emprestimo=?, data_da_devolucao=?, nome_funcionario=?, setor_de_trabalho=?, imagem=? WHERE id=?"
        cur.execute(query, i)
    


# deletar dados na tabela
def deletar_form(i):
    with con: 
        cur = con.cursor()
        query = "DELETE FROM INVETARIO WHERE id=?"
        cur.execute(query, i)  
          
        
# ver dados na tabela 
def ver_form():  
    ver_dados = []
    with con: 
        cur = con.cursor()
        query = "SELECT * FROM INVETARIO"
        cur.execute(query)
        
        rows = cur.fetchall()
        for row in rows:
            ver_dados.append(row)
    return ver_dados        

            
        


# ver dados individuais na tabela
def ver_item(id):
    ver_dados_individual = []
    with con: 
        cur = con.cursor()
        query = "SELECT * FROM INVETARIO WHERE id=?"
        cur.execute(query, id)
        
        rows = cur.fetchall()
        for row in rows:
            ver_dados_individual.append(row)           
    
    