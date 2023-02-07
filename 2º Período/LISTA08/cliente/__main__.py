from requests import get, put, delete, post
from prettytable import PrettyTable
from time import sleep

base_url = 'http://127.0.0.1:5000'

while True:
    try:
        escolha = int(input('''
            Escolha sua opção:

            0 – Sair do programa
            1 – Cadastrar um novo contato
            2 – Remover um contato a partir do e-mail
            3 – Recadastrar os dados do contato a partir do identificador
            4 – Listar todos os contatos cadastrados
            5 – Mostrar contatos a partir de seu nome considerando similaridade

            >>> '''.replace('    ', ''))
        )


        if not escolha in [0, 1, 2, 3, 4, 5]:
            print (f'Escolha uma das opçoões entre 0 e 5')
        else:
            if escolha == 0:
                break
            elif escolha == 1:
                nome = input('Digite o nome do contato: ').strip()
                email = input('Digite o E-mail do contato: ').strip()
                telefone = input('Digite o telefone do contato, ex: (84) 00232-1202: ').strip()
                nascimento = input('Digite da data de nascimento, ex: 19/05/1999: ').strip()

                payload = {
                    'nome': nome,
                    'email': email,
                    'telefone': telefone,
                    'nascimento': nascimento
                }

                req = post(f'{base_url}/contato/cadastrar', json=payload)

                print()
                print (req.json()['message'])
                sleep(4)

            elif escolha == 2:
                email = input('Digite o E-mail do contato que deseja excluir: ')
                req = delete(f'{base_url}/contato/remover?email={email}')

                print (req.json()['message'])

            elif escolha == 3:
                id_ = int(input('Digite o id do contato que deseja atualizar os dados: ').strip())
                nome = input('Digite o nome do contato: ').strip()
                email = input('Digite o E-mail do contato: ').strip()
                telefone = input('Digite o telefone do contato, ex: (84) 00232-1202: ').strip()
                nascimento = input('Digite da data de nascimento: ').strip()

                payload = {
                    'id': id_,
                    'nome': nome,
                    'email': email,
                    'telefone': telefone,
                    'nascimento': nascimento
                }

                req = put(f'{base_url}/contato/atualizar', json=payload)

                print()
                print (req.json()['message'])

            elif escolha == 4:
                req = get(f'{base_url}/contato/lista')

                if req.status_code in [200, 201]:
                    json = req.json()
                    
                    x = PrettyTable(["ID", "Nome", "E-mail", "Telefone", "Nascimento"])
                    
                    x.align["ID"] = "c"
                    x.align["Nascimento"] = "c"
                    x.align["Telefone"] = "c"
                    x.align["Nome"] = "c"
                    x.align["E-mail"] = "c"

                    x.padding_width = 1
                    
                    for y in json: x.add_row([y['id_'], y['nome'], y['telefone'], y['nascimento'], y['email'] ])

                    print(x)
                    sleep(4)
                else:
                    print('\n\nSem contatos cadastrados.')

            elif escolha == 5:
                busca = input('Digite o nome do contato que você deseja buscar: ')

                req = get(f'{base_url}/contato/busca?nome={busca}')

                if req.status_code in [200, 201]:
                    json = req.json()
                    
                    x = PrettyTable(["ID", "Nome", "E-mail", "Telefone", "Nascimento"])
                    
                    x.align["ID"] = "c"
                    x.align["Nascimento"] = "c"
                    x.align["Telefone"] = "c"
                    x.align["Nome"] = "c"
                    x.align["E-mail"] = "c"

                    x.padding_width = 1
                    
                    for y in json: x.add_row([y['id_'], y['nome'], y['telefone'], y['nascimento'], y['email'] ])

                    print(x)
                    sleep(4)

                else:
                    print (f'Nenhum resultado para "{busca}"')

    except Exception as e:
        print (f"\nOcorreu um erro. Tente novamente!\n\nDetalhes: {e}")
