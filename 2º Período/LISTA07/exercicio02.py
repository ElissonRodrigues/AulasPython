from requests import get
from re import sub
from os import system, name
from traceback import format_exc
from prettytable import PrettyTable

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
                    print ('\n'.join(f'{x.upper()}: {json[x] if json[x] else "N/A"}' for x in json.keys()))

                    req = get(f"http://servicodados.ibge.gov.br/api/v1/localidades/estados/{json['uf']}/municipios")
                    json = req.json()

                    print ('\n\n')
                    print ('DADOS ADICIONAIS:')
                    print('\n\n')
                    if json:
                        x = PrettyTable(["Municipio", "Microrregião", "Mesorregiao", "UF", "Regiao"])
                        x.align["Municipio"] = "l"
                        x.align["Microrregião"] = "c"
                        x.align["UF"] = "l"
                        x.align["Regiao"] = "l"
            
                        x.padding_width = 1
            
                        for y in json:
                            regiao = f"{y['microrregiao']['mesorregiao']['UF']['regiao']['sigla']} - {y['microrregiao']['mesorregiao']['UF']['regiao']['nome']}"
                            municipio = y['nome']
                            microrregiao = y['microrregiao']['nome']
                            mesoregiao = y['microrregiao']['mesorregiao']['nome']
                            uf = f"{y['microrregiao']['mesorregiao']['UF']['sigla']} - {y['microrregiao']['mesorregiao']['UF']['nome']}" 
            
                            x.add_row([municipio, microrregiao, mesoregiao, uf, regiao])

                        print (x)

                else:
                    print ('\n\nVerifique o cep e tente novamente')
                    
    except KeyboardInterrupt:
        print ("\n\nEncerrando script... Até breve :)")
        break
    except:
        print (format_exc())
