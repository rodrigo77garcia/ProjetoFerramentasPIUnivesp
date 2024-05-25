# utilizando o Flask
from flask import Flask, request, jsonify, render_template, current_app
# importando mysql para criar nossa view
from .db import db
from flask import Blueprint, render_template

bp = Blueprint('routes', __name__)

@bp.route('/')
def index():
    return render_template('index.html')



###########################################################
#CRUD
###########################################################

################################################################################################################################################
# adicionar dados na tabela
# Rota para adicionar uma ferramenta
@bp.route('/add', methods=['POST'])
def add_ferramenta():
    #data               = request.form.get
    nome               = request.form.get('nome')
    local              = request.form.get('local')
    descricao          = request.form.get('descricao')
    marca              = request.form.get('marca')
    data_do_emprestimo = request.form.get('data_do_emprestimo')
    data_da_devolucao  = request.form.get('data_da_devolucao')
    nome_funcionario   = request.form.get('nome_funcionario')
    setor_de_trabalho  = request.form.get('setor_de_trabalho')
    imagem             = request.form.get('imagem') 
    
    
    
    cursor = db.cursor()
    query  = """
    INSERT INTO ferramentas (nome, local, descricao, marca, data_do_emprestimo, data_da_devolucao, nome_funcionario, setor_de_trabalho, imagem)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    cursor.execute(query, (nome, local, descricao, marca, data_do_emprestimo, data_da_devolucao, nome_funcionario, setor_de_trabalho, imagem))
    db.commit()
    cursor.close()
    
    return jsonify({"message": "Ferramenta adicionada com sucesso"}), 201


######################################################################################
    
# atualizar dados na tabela 
# Rota para atualizar uma ferramenta existente
@bp.route('/ferramentas/<int:id>', methods=['PUT'])
def update_ferramenta(id):
    #data               = request.form.get
    nome               = request.form.get('nome')
    local              = request.form.get('local')
    descricao          = request.form.get('descricao')
    marca              = request.form.get('marca')
    data_do_emprestimo = request.form.get('data_do_emprestimo')
    data_da_devolucao  = request.form.get('data_da_devolucao')
    nome_funcionario   = request.form.get('nome_funcionario')
    setor_de_trabalho  = request.form.get('setor_de_trabalho')
    imagem             = request.form.get('imagem')

    cursor = db.cursor()
    query  = """
    UPDATE ferramentas
    SET nome = %s, local = %s, descricao = %s, marca = %s, data_do_emprestimo = %s, data_da_devolucao = %s, nome_funcionario = %s, setor_de_trabalho = %s, imagem = %s
    WHERE id = %s
    """
    cursor.execute(query, (nome, local, descricao, marca, data_do_emprestimo, data_da_devolucao, nome_funcionario, setor_de_trabalho, imagem, id))
    db.commit()
    cursor.close()
    
    return jsonify({"message": "Ferramenta atualizada com sucesso"}), 200
    

###########################################################################################################################################################################
# deletar dados na tabela
# Rota para deletar uma ferramenta
@bp.route('/ferramentas/<int:id>', methods=['DELETE'])
def delete_ferramenta(id):
    cursor = db.cursor()
    cursor.execute("DELETE FROM ferramentas WHERE id = %s", (id,))
    db.commit()
    cursor.close()

    return jsonify({"message": "Ferramenta deletada com sucesso"}), 200
  
          
############################################################################################        
# ver dados na tabela 
# Rota para listar todas as ferramentas
@bp.route('/ferramentas', methods=['GET'])
def get_ferramentas():
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM ferramentas")
    ferramentas = cursor.fetchall()
    cursor.close()
    return jsonify(ferramentas)    

##################################################################################  


##################################################################################
# ver dados individuais na tabela
# Rota para listar uma ferramenta individualmente
@bp.route('/ferramentas/<int:id>', methods=['GET'])
def get_ferramenta(id):
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM ferramentas WHERE id = %s", (id,))
    ferramenta = cursor.fetchone()
    cursor.close()
    if ferramenta:
        return jsonify(ferramenta)
    else:
        return jsonify({"message": "Ferramenta não encontrada"}), 404


#################################################################################
            
    
    