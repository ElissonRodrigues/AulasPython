from prettytable import PrettyTable
from requests import get

while True:
    sigla = input('\n\nDigite a sigla do seu estado, ex: RN, AC, SP: ').upper()
    print ()
    if not all([len(sigla) == 2, sigla.isalpha()]):
        print('Verifique a sigla do seu estado e tente novamente.')
    else:
        req = get(f'http://servicodados.ibge.gov.br/api/v1/localidades/estados/{sigla}/municipios')
        json = req.json()

        if json:
            x = PrettyTable(["Municipio", "Microrregião", "mesorregiao", "UF", "Regiao"])
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
            print ('Verifique a sigla do seu estado e tente novamente.')



