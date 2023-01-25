from requests import post, get
from prettytable import PrettyTable
from getpass import getpass
from os import system, name

tentativas_login = 3

def login(user: str, password: str) -> dict[int, dict]:    
    payload = {
        'username': user,
        'password': password
    }
    login_req = post('https://suap.ifrn.edu.br/api/v2/autenticacao/token/',  json=payload)
    json = login_req.json()

    return {'status': login_req.status_code, 'response': json}

def main():
    logado = False
    login_data = {}
    
    for tentativa in range(1, tentativas_login+1):
        username = input("Digite o número da sua Matrícula: ")
        password = getpass("Digite a sua senha: ")
        login_user = login(username, password)
        
        if login_user["status"] in [200, 201]:
            logado = True
            login_data.update(login_user["response"])
            break 
        else:
            print ("\nVerifique o nome de usuário e senha informados")
            
            escolha = input("\n\nDeseja tentar novamente?\n\nS - SIM\nN - NÃO\n\n>>> ")
            
            if escolha.upper() in ["S", "SIM"]:
                system('cls' if name == "nt" else "clear")
                print (f"\nTentativa {tentativa}/{tentativas_login}\n\n") if tentativa < tentativas_login else ""
            else:
                logado = None
                break
            
    if logado:
        system('cls' if name == "nt" else "clear")
        
        while True:
            periodo_letivo = input("\n\nInforme o período letivo para consultar deus dados. Exemplo: 2022.2: ")
            
            if all([len(periodo_letivo.split(".")) == 2, periodo_letivo.replace(".", "").isnumeric()]):
                headers={"Authorization": f"Bearer {login_data['access']}"}
                req = get(f'https://suap.ifrn.edu.br/api/v2/minhas-informacoes/boletim/{periodo_letivo.split(".")[0]}/{periodo_letivo.split(".")[1]}/', headers=headers)
                
                x = PrettyTable(["Disciplina", "Frequência", "Faltas", "Notas"])
    
                x.align["Disciplina"] = "l"
                x.align["Frequência"] = "c"
                x.align["Notas"] = "c"
                
                x.padding_width = 1
                
                print ()
                for boletim in req.json():
                    nota1 = str(boletim["nota_etapa_1"]["nota"]) if boletim["nota_etapa_1"]["nota"] else '00'
                    nota2 = str(boletim["nota_etapa_2"]["nota"]) if boletim["nota_etapa_2"]["nota"] else '00'
                    nota3 = str(boletim["nota_etapa_3"]["nota"]) if boletim["nota_etapa_3"]["nota"] else '00'
                    nota4 = str(boletim["nota_etapa_4"]["nota"]) if boletim["nota_etapa_4"]["nota"] else '00'
                   
                    numero_faltas = str(boletim["numero_faltas"]).zfill(2) if boletim["numero_faltas"] else '00'
                    frequencia = str(round(boletim["percentual_carga_horaria_frequentada"])).zfill(2)
                    
                    notas = ", ".join(map(lambda y: y, [nota1, nota2, nota3, nota4][:boletim["quantidade_avaliacoes"]]))
                    disciplina = boletim["disciplina"]
                    
                    x.add_row([disciplina, frequencia, numero_faltas, notas])
                    
                print (x)
                
                escolha = input("\n\nFazer uma nova consulta?\n\nS - SIM\nN - NÃO\n\n>>> ")
                
                if escolha.upper() in ["S", "SIM"]: print ("\n\n")
                else: break
                
            else:
                print ("\n\nVerifique o período letivo informado e tente novamente!")
    elif logado == False:
        print ("\n\nInfelizmente não foi possível validar suas informações, tente novamente mais tarde!")
    else:
        print ("\n\nObrigado por utilizar o script SUAP. Até Mais!")

if __name__ == '__main__':
    main()
