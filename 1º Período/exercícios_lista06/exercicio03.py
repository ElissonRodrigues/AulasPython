"""
Faça um programa para gerenciar uma agenda de contados.
Para cada contato deverá ser guardado o seu nome, e-mail
e número de telefone. O programa deve apresentar ao usuário
um menu para que ele escolha a opção que deseja executar,
sendo possível escolher entre: adicionar um contato, buscar
um contato, listar todos os contatos, sair. Seu programa deve
garantir que cada contato possui um e-mail único e todas as
operações que necessitam de busca devem ser feitas através do e-mail.
"""


def imprimir_contato(contato):
    print("#")
    print(f"Nome: {contato[0]}")
    print(f"E-Mail: {contato[1]}")
    print(f"Telefone: {contato[2]}")


def buscar_por_email(email):
    contato = None
    arquivo = open("contatos.csv", "r", encoding="utf-8")

    # felipe;felipe@gmail.com;841234\n
    for linha in arquivo:
        campos = linha.strip().split(";")

        if campos[1] == email:
            contato = campos
            break

    arquivo.close()
    return contato


def ler_opcao():
    while True:
        print(50 * "-")
        print("0 - Sair do programa")
        print("1 - Adicionar contato")
        print("2 - Buscar contato")
        print("3 - Listar todos os contatos")

        try:
            opcao = int(input("Escolha uma opção: "))
            break
        except ValueError:
            print("O valor não é um número, tente novamente!")

    return opcao


def ler_telefone():
    while True:
        try:
            telefone = int(input("Digite o telefone do contato: "))
            break
        except ValueError:
            print("Não é um telefone válido, tente novamente!")

    return telefone


def main():
    while True:
        opcao = ler_opcao()

        if opcao == 0:
            print("Finalizando programa...")
            break
        elif opcao == 1:
            nome = input("Digite o nome do contato: ")
            email = input("Digite o e-mail do contato: ")
            telefone = ler_telefone()

            if buscar_por_email(email) is None:
                arquivo = open("contatos.csv", "a", encoding="utf-8")
                arquivo.write(f"{nome};{email};{telefone}\n")
                arquivo.close()

                print("Contato salvo com sucesso!")
            else:
                print("Este e-mail já está em uso!")
        elif opcao == 2:
            email = input("Digite o e-mail da busca: ")
            contato = buscar_por_email(email)

            if contato is None:
                print("E-mail não encontrado!")
            else:
                imprimir_contato(contato)
        elif opcao == 3:
            arquivo = open("contatos.csv", "r", encoding="utf-8")

            for linha in arquivo:
                campos = linha.strip().split(";")
                imprimir_contato(campos)

            arquivo.close()
        else:
            print("Opção inválida, tente novamente!")


if __name__ == "__main__":
    main()