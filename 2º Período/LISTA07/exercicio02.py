from requests import get
from re import sub
from os import system, name
from traceback import format_exc

base_url = 'https://viacep.com.br/ws/{}/json'

while True:
    try:
        cep = sub('[-,_/]', '', input('\n\nDigite o seu CEP: ').strip())
    
        if not len(cep) == 8:
            print ('\n\nCep inválido! Digite um cep valído e tente novamente.')
        else:
            req = get(base_url.format(cep))
            
            if req.status_code in [200, 201]:
                json = req.json()
    
                if not 'erro' in json.keys():
                    system('cls' if name == 'nt' else 'clear')
                    print ('\n'.join(map(lambda x: f'{x.upper()}: {json[x] if json[x] else "N/A"}', json.keys())))
                else:
                    print ('\n\nVerifique o cep e tente novamente')
                    
    except KeyboardInterrupt:
        print ("\n\nEncerrando script... Até breve :)")
        break
    except:
        print (format_exc())
