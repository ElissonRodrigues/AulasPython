import socket
from time import sleep
from colors import TextColor
from json import dumps, loads
from os import system, name

host = "0.0.0.0"
port = 5555

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = (host, port)
sock.connect(server_address)

while True:
    try:
        sleep(2)
        escolha = int(input("""
        Escolha uma das operações abaixo:
        
        0 – Sair do programa
        1 – Cadastrar uma venda
        2 – Mostrar uma venda a partir de seu código
    
        >>> """.replace("        ", "")))

        if 0 <= escolha <= 2:
            if escolha == 0:
                sock.close()
                break

            elif escolha == 1:
                system("cls" if name == "nt" else "clear")
                print("Informe os seguites dados:\n\n")

                client_response = {
                    "request_type": "cadastrar_venda",
                    "dados_venda": [
                        {
                            "codigo_venda": int(input("Código de venda: ")),
                            "valor_venda": float(input("Valor da venda: ")),
                            "dia_venda": int(input("Dia da venda: ")),
                            "mes_venda": int(input("Mês da venda: ")),
                            "ano_venda": int(input("Ano da venda: ")),
                        }
                    ],
                }

                sock.send(dumps(client_response).encode())
                server_response = loads(sock.recv(1024).decode())
                print()
                if server_response["status"] == "success":
                    print(TextColor(server_response["msg"]["text"]).setColor("green"))
                else:
                    print(TextColor(server_response["msg"]["text"]).setColor("red"))

            elif escolha == 2:
                system("cls" if name == "nt" else "clear")
                codigo_venda = int(input("código de venda: "))

                client_response = {
                    "request_type": "consultar_venda",
                    "codigo_venda": codigo_venda,
                }

                sock.send(dumps(client_response).encode())
                server_response = loads(sock.recv(1024).decode())

                if (
                    server_response["status"] == "success"
                    and server_response["type"] == "data"
                ):
                    json_data = loads(server_response["msg"]["result"][1])
                    print()
                    print("=" * 22)
                    print("RESUMO DA VENDA".center(21))
                    print("=" * 22)

                    print(
                        f"\nCódigo da venda: {json_data['codigo_venda']}\nValor da venda: R${json_data['valor_venda']}\nDia da venda: {json_data['dia_venda']}\nMês da venda: {json_data['mes_venda']}\nAno da venda: {json_data['ano_venda']}\n"
                    )
                    print("=" * 22)
                else:
                    print()
                    print(TextColor(server_response["msg"]["text"]).setColor("red"))

        else:
            print(TextColor("\nEscolha um número entre 0 e 2. Tente novamente!").setColor("red"))

    except ValueError:
        print(TextColor("\nOops, você digitou algo errado. Tente novamente").setColor("red"))
    except KeyboardInterrupt:
        sock.close()
        break
