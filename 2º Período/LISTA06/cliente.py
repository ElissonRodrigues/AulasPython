from database import *
from time import sleep
from datetime import datetime
from validadores import Validar

validar = Validar()
sleep_time = 3

while True:
    try:
        escolha = int(input(
            """
            Escolha uma das opções abaixo: 

            0. Sair do programa
            1. Adicionar contato
            2. Remover contato
            3. Atualizar telefone do contato
            4. Consultar contato por e-mail
            5. Listar contatos
            6. Consultar contato por nome 
            
            >>> """.replace("    ", "")
            )
        )

        if escolha == 0:
            break

        elif escolha == 1:
            nome = input("Digite o nome do contato: ")
            email = input("Digite o e-mail: ")
            telefone = input("Diogite o telefone, ex: (84) 98725-3954: ")
            nascimento = input("Digite a data de nascimneto. Ex: 19/05/1999: ")

            valido = validar.todos(email, telefone, nascimento)

            if checar_email(email):
                print("\n\nEsse endereço de email já está cadastrado!")
                sleep(sleep_time)

            elif valido[0]:
                agendado = adicionar_contato(nome, email, telefone, nascimento)
                if agendado:
                    print(f"\n\n{nome} foi adicionado a agenda")
                else:
                    print("Não foi possivél adicionar o contato a agenda. Tente novamente!")
            else:
                if valido[1] == "email":
                    print("\nVerifique o endereço de e-mail e tente novamente\n")
                elif valido[1] == "telefone":
                    print("\nVerifique o telefone e tente novamente!\n")
                elif valido[1] == "nascimento":
                    print("\nVerifique a data de nascimento e tente novamente\n")
                else:
                    print("\nVerifique os dados informados e tente novamente\n")

            sleep(sleep_time)

        elif escolha == 2:
            email = input("Digite o e-mail: ")
            if validar.email(email):
                if deletar_contato(email):
                    print("\n\nO contato foi deletado da agenda")
                else:
                    print(
                        "Não foi possível deletar esse contato, verifique o email digitado e tente novamente!"
                    )
            else:
                print(
                    "\n\nendereço de email invalido!\n\nInforme um endereço de email válido e tente novamente."
                )

            sleep(sleep_time)

        elif escolha == 3:
            email = input("Digite o email: ")
            novo_telefone = input("Digite o novo número de telefone, ex: (84) 98725-3954: ")

            if validar.telefone(novo_telefone) and validar.email(email):
                atualizado = atualizar_conatato(email, novo_telefone)

                if atualizado:
                    print(f'\n\nO número desse contato foi atualizado para "{novo_telefone}"')
                else:
                    print("\n\nNão foi possível atualizar o telefone. Verifique o endereço de email")
            else:
                print("\n\nendereço de email ou telefone invalido, tente novamente.")

            sleep(sleep_time)

        elif escolha in [4, 5, 6]:

            if escolha == 6:
                nome = input("Digite o nome do contato que você deseja buscar: ").lower().strip()
                contatos = busca_contato(nome)
            elif escolha == 4:
                email = input("Digite o email: ")

                if validar.email(email):
                    contatos = buscar_email(email)
                else:
                    print("\n\nEndereço de E-mail inválido!")
                    contatos = None
            else:
                contatos = dados_contato()

            if contatos:
                print("=" * 30)
                for contato in contatos:
                    cadastro = datetime.strptime(contato[5], "%Y-%m-%d %H:%M:%S").strftime(
                        "%d/%m/%Y %H:%M:%S"
                    )
                    print(
                        f"\nNome: {contato[1].capitalize()}\nE-mail {contato[2]}\nTelefone: {contato[3]}\nNascimento: {contato[4]}\nCadastro: {cadastro}"
                    )
                    print("=" * 30)
            elif contatos == None:
                pass
            else:
                if escolha == 5:
                    print(
                        "\n\nSem contatos na agenda. utilize a opção 01 para adicionar um novo conatato."
                    )
                elif escolha == 4:
                    print(f"\n\nNenhum contato com o e-mail: {email}")
                else:
                    print(f'\n\nSem resultados para "{nome}"')

            sleep(sleep_time)

        else:
            print("\n\nEscolha inválida! tente novamente.")
            sleep(sleep_time)

    except ValueError:
        print("Oops.. Parece que você digitou algo errado! tente novamente.")
        sleep(sleep_time)
    except KeyboardInterrupt:
        print("\n\nScript encerrado! Volte sempre :)\n\n")
        break
