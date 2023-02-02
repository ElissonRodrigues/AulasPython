from flask import Flask, request
from .ferramentas.validadores import *
from servidor.database import *
from .ferramentas.api_models import *
from traceback import format_exc
from werkzeug.exceptions import BadRequest
from .strings import strings

app = Flask(__name__)
validar = Validar()


@app.route("/cadastrar_contato", methods=["POST"])
def cadastrar():
    """Cadastrar novo contato no servidor. 
    
    Exemplo: 

    from requests import post

    payload = {
        'nome': 'Nome exemplo',
        'email': 'exemplo@gmail.com',
        'telefone': '(84) 91111-1234',
        'nascimento': '19/05/1999'
    }
    req = post('http://127.0.0.1:5000/cadastrar_contato', json=payload)
    print (req.json())

    """    
    try:
        parametros = ["nome", "email", "telefone", "nascimento"]

        json = request.json

        if len(json.keys()) == len(parametros) and all([x in json.keys() for x in parametros]):
            nome = json["nome"]
            email = json["email"]
            telefone = json["telefone"]
            nascimento = json["nascimento"]

            valido = validar.todos(email, telefone, nascimento)

            if valido[0]:
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

@app.route("/remover_contato", methods=["DELETE"])
def remover():
    try:
        parametros = ["email"]
        json = request.args

        if len(json.keys()) == len(parametros) and all([x in json.keys() for x in parametros]):
            email = json["email"]

            if validar.email(email):
                deletado = deletar_contato(email)

                if deletado:
                    return ResponseMessage(status='ok',message=strings['descadastramento']['removido']).json()
                else:
                    return ResponseMessage(message=strings['descadastramento']['erro_ao_remover']).json(), 422
            else:
                return ResponseMessage(message=strings['descadastramento']['email_invalido']).json()

        else:
            return ResponseMessage(message=strings['descadastramento']['faltando_parametros']).json()

    except BadRequest:
       return ResponseMessage(message=strings['descadastramento']['faltando_parametros']).json(), 422
    except:
        print (format_exc())

@app.route('/recadastrar_contato', methods=["PUT"])
def recadastrar():
    """Atualizar contato já existente na base de dados. 
    
    Exemplo: 

    from requests import post

    payload = {
        'id': 1,
        'nome': 'Nome exem',
        'email': 'exemplo@gmail.com',
        'telefone': '(84) 91111-1234',
        'nascimento': '19/05/1999'
    }
    req = post('http://127.0.0.1:5000/recadastrar_contato', json=payload)
    print (req.json())

    """    
    try:
        parametros = ["id", "nome", "email", "telefone", "nascimento"]
        json = request.json

        if len(json.keys()) == len(parametros) and all([x in json.keys() for x in parametros]):
            id_ = int(json['id']) 

            if not checar_id(id_):
                return ResponseMessage(message='Nenhum contato encontrado com esse ID').json()
            else:
                nome = json["nome"]
                email = json["email"]
                telefone = json["telefone"]
                nascimento = json["nascimento"]
               

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
            return ResponseMessage(message=strings['cadastramento']['faltando_parametros']).json(), 422
    except BadRequest:
       return ResponseMessage(message=strings['descadastramento']['faltando_parametros']).json(), 422
    except:
        print (format_exc())

@app.route('/contatos',  methods=["GET"])
def contatos():
    try:
        agenda = listar_contato()

        if agenda: 
            return ResponseMessage(message=strings['contatos']['lista'].format(agenda[0], agenda[1], agenda[2], agenda[3], agenda[4])).json()
        else:
            return ResponseMessage(message=strings['contatos']['sem_contatos']).json()
    except: 
        print (format_exc())

app.run(debug=False)
