from requests import get, put, delete, post
from prettytable import PrettyTable

base_url = 'http://127.0.0.1:5000'
while True:
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
            nome = input('Digite o nome do contato: ')
            email = input('Digite o E-mail do contato: ')
            telefone = input('Digite o telefone do contato, ex: (84) 00232-1202: ')
            nascimento = input('Digite da data de nascimento: ')

            payload = {
                'nome': nome,
                'email': email,
                'telefone': telefone,
                'nascimento': nascimento
            }

            req = post(f'{base_url}/contato/cadastrar', json=payload)

            print()
            print (req.json()['message'])

        elif escolha == 2:
            email = input('Digite o E-mail do contato que deseja excluir: ')
            req = delete(f'{base_url}/contato/remover?email={email}')

            print (req.json()['message'])

        elif escolha == 3:
            id_ = int(input('Digite o id do contato que deseja atualizar os dados: '))
            nome = input('Digite o nome do contato: ')
            email = input('Digite o E-mail do contato: ')
            telefone = input('Digite o telefone do contato, ex: (84) 00232-1202: ')
            nascimento = input('Digite da data de nascimento: ')

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

                print (f"Nome: {json['nome']}\n{json['telefone']}\n{json['nascimento']}\nEmail: {json['email']}")
            else:
                print('Verifique o ID informado.')

        elif escolha == 5:
            busca = input('Digite o nome do contato que você deseja buscar: ')

            req = get(f'{base_url}/contato/busca?nome={busca}')
            if req.status_code in [200, 201]:
                json = req.json()
                
                
                x = PrettyTable(["ID", "Nome", "Telefone", "Nascimento", "E-mail", "Regiao"])

                x.align["ID"] = "c"
                
                print ('\n\n'.join(map(lambda x: f"Nome: {x['nome']}\n{x['telefone']}\n{x['nascimento']}\nEmail: {x['email']}", json)))

            else:
                print (f'Nenhum resultado para "{busca}"')







