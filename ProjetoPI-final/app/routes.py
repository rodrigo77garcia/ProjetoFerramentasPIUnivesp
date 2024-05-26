# utilizando o Flask
from flask import Flask, redirect, request, jsonify, render_template, current_app, url_for
from .db import get_db
from flask import Blueprint, render_template
from datetime import datetime

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
   
    nome                   = request.form.get('nome')
    local                  = request.form.get('local')
    descricao              = request.form.get('descricao')
    marca                  = request.form.get('marca')
    data_do_emprestimo_str = request.form.get('data_do_emprestimo')
    data_da_devolucao_str  = request.form.get('data_da_devolucao')
    nome_funcionario       = request.form.get('nome_funcionario')
    setor_de_trabalho      = request.form.get('setor_de_trabalho')
    imagem                 = request.form.get('imagem') 
    
    # Debug: Print values to check if they are correctly received
    print(f"Received: nome={nome}, local={local}, descricao={descricao}, marca={marca}, data_do_emprestimo={data_do_emprestimo_str}, data_da_devolucao={data_da_devolucao_str}, nome_funcionario={nome_funcionario}, setor_de_trabalho={setor_de_trabalho}, imagem={imagem}")
    data_do_emprestimo = datetime.strptime(data_do_emprestimo_str, '%Y-%m-%d') if data_do_emprestimo_str else None
    data_da_devolucao  = datetime.strptime(data_da_devolucao_str, '%Y-%m-%d') if data_da_devolucao_str else None
    
    db = get_db()
    cursor = db.cursor()
    
    
    query  = """
    INSERT INTO ferramentas (nome,local,descricao,marca,data_do_emprestimo,data_da_devolucao,nome_funcionario,setor_de_trabalho,imagem)
    VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)
    """
    try:
        cursor.execute(query, (nome, local, descricao, marca, data_do_emprestimo, data_da_devolucao, nome_funcionario, setor_de_trabalho, imagem))
        db.commit()
    except Exception as e:
        db.rollback()
        print(f"Error: {e}")
        return jsonify({"message": "Erro ao adicionar a ferramenta", "error": str(e)}), 500
    finally:
        cursor.close()

    return jsonify({"message": "Ferramenta adicionada com sucesso"}), 201


######################################################################################
    
# atualizar dados na tabela 
# Rota para atualizar uma ferramenta existente
@bp.route('/update/<int:id>', methods=['GET', 'POST'])
def update_ferramenta(id):
    db = get_db()
    cursor = db.cursor()
    cursor.execute('SELECT * FROM ferramentas WHERE id = %s', (id,))
    ferramenta = cursor.fetchone()

    if ferramenta is None:
        # Caso o ID não exista, redirecionar para a lista de ferramentas com uma mensagem de erro
        cursor.close()
        return redirect(url_for('routes.listar_ferramentas'))

    if request.method == 'POST':
        nome = request.form.get('nome')
        local = request.form.get('local')
        descricao = request.form.get('descricao')
        marca = request.form.get('marca')
        data_do_emprestimo = request.form.get('data_do_emprestimo')
        data_da_devolucao = request.form.get('data_da_devolucao')
        nome_funcionario = request.form.get('nome_funcionario')
        setor_de_trabalho = request.form.get('setor_de_trabalho')
        imagem = request.form.get('imagem')

        query = """
        UPDATE ferramentas
        SET nome = %s, local = %s, descricao = %s, marca = %s, data_do_emprestimo = %s, data_da_devolucao = %s, nome_funcionario = %s, setor_de_trabalho = %s, imagem = %s
        WHERE id = %s
        """
        cursor.execute(query, (nome, local, descricao, marca, data_do_emprestimo, data_da_devolucao, nome_funcionario, setor_de_trabalho, imagem, id))
        db.commit()
        cursor.close()
        return redirect(url_for('routes.listar_ferramentas'))

    return render_template('update_ferramenta.html', ferramenta=ferramenta)

    

###########################################################################################################################################################################
# deletar dados na tabela
# Rota para deletar uma ferramenta
@bp.route('/delete/<int:id>', methods=['GET', 'POST'])
def delete_ferramenta(id):
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM ferramentas WHERE id = %s", (id,))
    ferramenta = cursor.fetchone()

    if ferramenta is None:
        # Caso o ID não exista, redirecionar para a lista de ferramentas com uma mensagem de erro
        cursor.close()
        return redirect(url_for('routes.listar_ferramentas'))

    if request.method == 'POST':
        cursor.execute("DELETE FROM ferramentas WHERE id = %s", (id,))
        db.commit()
        cursor.close()
        return redirect(url_for('routes.listar_ferramentas'))
    
    cursor.close()
    return render_template('delete_ferramenta.html', ferramenta=ferramenta)


  
          
############################################################################################        
# ver dados na tabela 
# Rota para listar todas as ferramentas
@bp.route('/ferramentas', methods=['GET'])
def listar_ferramentas():
    db = get_db()
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM ferramentas")
    ferramentas = cursor.fetchall()
    cursor.close()
    print(ferramentas)  # Linha para depurar
    
    return render_template('listar_ferramentas.html', ferramentas=ferramentas)    

##################################################################################  


##################################################################################
# ver dados individuais na tabela
# Rota para listar uma ferramenta individualmente
@bp.route('/ferramentas/<int:id>', methods=['GET'])
def listar_ferramentasID(id):
    db = get_db()
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM ferramentas WHERE id = %s", (id,))
    ferramenta = cursor.fetchone()
    cursor.close()
    if ferramenta:
        return jsonify(ferramenta)
    else:
        return jsonify({"message": "Ferramenta não encontrada"}), 404


#################################################################################
# Conectar e desconectar ao banco de dados automaticamente
@bp.before_app_request
def before_request():
    db = get_db()
    if not hasattr(current_app, 'db'):
        current_app.db = db

@bp.teardown_app_request
def teardown_request(exception):
    if hasattr(current_app, 'db'):
        current_app.db.close()

