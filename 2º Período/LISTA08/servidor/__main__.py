from flask import Flask, request, jsonify
from .ferramentas.validadores import *
from servidor.database import *
from .ferramentas.api_models import *
from traceback import format_exc
from werkzeug.exceptions import BadRequest
from .res.strings import strings

app = Flask(__name__)
validar = Validar()


@app.route("/contato/cadastrar", methods=["POST"])
def cadastrar():
    """Cadastrar novo contato no servidor. 
    
    Exemplo: 

    from requests import post

    payload = {
        'nome': 'Elisson',
        'email': 'exempo@gmail.com',
        'telefone': '(84) 91111-1234',
        'nascimento': '19/05/1999'
    }
    req = post('http://127.0.0.1:5000/contato/cadastrar', json=payload)
    print (req.json())

    """    
    try:
        parametros = ["nome", "email", "telefone", "nascimento"]
        json = request.json

        if not set(parametros) - set(json):
            nome, email, telefone, nascimento = (json[k] for k in parametros)
            valido = validar.todos(email, telefone, nascimento)

            if checar_email(email):
                return ResponseMessage(message=strings['cadastramento']['email_cadastrado']).json(), 422

            elif valido[0]:
                cadastrado = adicionar_contato(nome, email, telefone, nascimento)
                if cadastrado:
                    return ResponseMessage(status="ok", message=strings['cadastramento']['cadastrado']).json(), 201
                else:
                    return ResponseMessage(message=strings['cadastramento']['nao_cadastrado']).json(), 500

            else:
                if valido[1] == "email":
                    return ResponseMessage(message=strings['cadastramento']['email_invalido']).json(), 400
                elif valido[1] == "telefone":
                    return ResponseMessage(message=strings['cadastramento']['telefone_invalido']).json(), 400
                elif valido[1] == "nascimento":
                    return ResponseMessage(message=strings['cadastramento']['nascimento_invalido']).json(), 400
                else:
                    return ResponseMessage(message=strings['cadastramento']["erro_desconhecido"]).json(), 400

        else:
            return ResponseMessage(message=strings['cadastramento']['faltando_parametros']).json(), 422

    except BadRequest:
       return ResponseMessage(message=strings['cadastramento']['faltando_parametros']).json(), 422
    except:
        print (format_exc())
        return {}, 404

@app.route("/contato/remover", methods=["DELETE"])
def remover():
    """Cadastrar novo contato no servidor. 
    
    Exemplo: 

    from requests import delete

    req = delete('http://127.0.0.1:5000/contato/remover?email=exemplo@gmail.com)
    print (req.json())

    """
    try:
        parametros = ["email"]
        json = request.args
        
        if not set(parametros) - set(json):
            email = json["email"]

            if validar.email(email):
                deletado = deletar_contato(email)

                if deletado:
                    return ResponseMessage(status='ok',message=strings['descadastramento']['removido']).json()
                else:
                    return ResponseMessage(message=strings['descadastramento']['erro_ao_remover']).json(), 422
            else:
                return ResponseMessage(message=strings['descadastramento']['email_invalido']).json(), 404

        else:
            return ResponseMessage(message=strings['descadastramento']['faltando_parametros']).json(), 400

    except BadRequest:
       return ResponseMessage(message=strings['descadastramento']['faltando_parametros']).json(), 422
    except:
        print (format_exc())
        return {}, 500

@app.route('/contato/atualizar', methods=["PUT"])
def recadastrar():
    """Atualizar contato já existente na base de dados. 
    
    Exemplo: 

    from requests import put

    payload = {
        'id': 2,
        'nome': 'Nome exem',
        'email': 'exemplo@gmail.com',
        'telefone': '(84) 91111-1234',
        'nascimento': '19/05/1999'
    }
    req = put('http://127.0.0.1:5000/contato/atualizar', json=payload)
    print (req.json())

    """    
    try:
        parametros = ["id", "nome", "email", "telefone", "nascimento"]
        json = request.json

        if not set(parametros) - set(json):
            id_ = int(json['id']) 

            if not checar_id(id_):
                return ResponseMessage(message='Nenhum contato encontrado com esse ID').json(), 404
            else:
                _, nome, email, telefone, nascimento = (json[k] for k in parametros)

                valido = validar.todos(email, telefone, nascimento)

                if valido[0]:
                    atualizado = atualizar_contato(id_, nome, email, telefone, nascimento)
                    if atualizado:
                        return ResponseMessage(status="ok", message=strings['atualizar_contato']['atualizado']).json()
                    else:
                        return ResponseMessage(message=strings['atualizar_contato']['nao_atualizado']).json(), 500

                else:
                    if valido[1] == "email":
                        return ResponseMessage(message=strings['cadastramento']['email_invalido']).json(), 400
                    elif valido[1] == "telefone":
                        return ResponseMessage(message=strings['cadastramento']['telefone_invalido']).json(), 400
                    elif valido[1] == "nascimento":
                        return ResponseMessage(message=strings['cadastramento']['nascimento_invalido']).json(), 400
                    else:
                        return ResponseMessage(message=strings['cadastramento']["erro_desconhecido"]).json(), 400
                        
        else:
            return ResponseMessage(message=strings['cadastramento']['faltando_parametros']).json(), 400
    except BadRequest:
       return ResponseMessage(message=strings['descadastramento']['faltando_parametros']).json(), 400
    except:
        print (format_exc())
        return {}, 500

@app.route('/contato/lista',  methods=["GET"])
def contatos():
    """Retorna uma lista com todos os contatos cadastrados se existir contatos na base de dados

    from requests import get 

    req = get('http://127.0.0.1:5000/contato/lista')

    req.json()
    >>> [{'email': 'exemplo@gmail.com', 'id_': 1, 'nascimento': '19/05/1999', 'nome': 'Nome exem', 'telefone': '(84) 91111-1234'}]

    """    
    try:
        agenda = listar_contato()

        if agenda: 
            lista_contatos = []
            for x in agenda:
                lista_contatos.append(ContactData(
                    nascimento=x[4],
                    id_=x[0], 
                    nome=x[1], 
                    email=x[2], 
                    telefone=x[3], 
                    uri={'endpoint': f'/busca/{x[0]}'}).json()
                )     

            return jsonify(lista_contatos)
        else:
            return ResponseMessage(message=strings['contatos']['sem_contatos']).json(), 404
    except: 
        print (format_exc())
        return {}, 500

@app.route('/contato/busca', methods=["GET"])
def buscar_nome():
    """Faz uma busca na base de dados atraves do nome informado

    from requests import get 

    req = get('http://127.0.0.1:5000/contato/busca?nome=ex')

    req.json()
    >>> [{'email': 'exemplo@gmail.com', 'id_': 1, 'nascimento': '19/05/1999', 'nome': 'Nome exem', 'telefone': '(84) 91111-1234'}]

    Returns:
        json: retorna um json com o resultado da consulta
    """    
    try:
        parametros = ['nome']
        json = request.args
        if not set(parametros) - set(json):
            nome = json['nome']

            resultado = busca_contato(nome)

            if resultado:
                lista_contatos = []
                for x in resultado:
                   lista_contatos.append(ContactData(
                    nascimento=x[4],
                    id_=x[0], 
                    nome=x[1], 
                    email=x[2], 
                    telefone=x[3], 
                    uri={'endpoint': f'/busca/{x[0]}'}).json()
                )
                
                return jsonify(lista_contatos)
            else:
                return ResponseMessage(message=strings['contatos']['sem_contatos']).json(), 404
        else:
            return ResponseMessage(message=strings['busca']['faltando_parametros']).json(), 400

    except BadRequest:
       return ResponseMessage(message=strings['busca']['faltando_parametros']).json(), 400
    except:
        print (format_exc())
        return {}, 500

@app.route('/contato/busca/<int:cid>', methods=["GET"])
def buscar_cid(cid):
    """Busca de  contato via ID

    from requests import get

    resultado = get('http://127.0.0.1:5000/contato/busca/2')
    print (resultado.json())
    """  
    try:
        
        x = buscar_id(int(cid))

        if x:
            return ContactData(id_=x[0], nome=x[1], email=x[2], telefone=x[3], nascimento=x[4], uri={'endpoint': f'/busca/{x[0]}'}).json()
        else:
            return ResponseMessage(message=strings['busca']['id_invalido']).json(), 404

    except BadRequest:
       return ResponseMessage(message=strings['busca']['faltando_parametros']).json(), 400
    except:
        print (format_exc())
        return {}, 500

app.run(debug=False)
