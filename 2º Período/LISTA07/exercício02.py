from requests import get
from re import sub
from os import system, name
from traceback import format_exc

base_url = 'https://viacep.com.br/ws/{}/json'

while True:
    cep = sub('[-,_/]', '', input('\n\nDigite o seu CEP: ').strip())

    if len(cep) > 8:
        print ('Cep inválido! Digite um cep valído e tente novamente.')
    else:
        try:
            req = get(base_url.format(cep))
            
            if req.status_code in [200, 201]:
                json = req.json()

                if not 'erro' in json.keys():
                    system('cls' if name == 'nt' else 'clear')
                    print ('\n'.join(map(lambda x: f'{x[1].upper()}: {json[x[1]] if json[x[1]] else "N/A"}', enumerate(json.keys()))))
                else:
                    print ('Verifique o cep e tente novamente')
        except:
            print (format_exc())
            
            
    