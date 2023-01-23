import socket
from dataclasses import asdict, dataclass, field
from threading import Thread
from json import loads, dumps
from database import cadastrar_venda, consultar_venda

host = "0.0.0.0"
port = 5555

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((host, port))
sock.listen(10)

print("Servidor iniciado!")


@dataclass
class ServerResponse:
    status: str = field(default="error")
    type: str = field(default="msg")
    msg: dict = field(default_factory=tuple)
    
    def __post_init__(self):
        if len(self.msg) == 0:
            self.msg = {}
        elif self.msg[0] == 0:
            self.msg = {"text": self.msg[1]}
        else:
            self.msg = {"result": self.msg[1]}


def vendas(client, address) -> None:
    while True:
        try:
            client_decoded_bytes = client.recv(1024).decode()

            if client_decoded_bytes:
                client_data = loads(client_decoded_bytes)

                if client_data["request_type"] == "cadastrar_venda":
                    cadastar = cadastrar_venda(
                        client_data["dados_venda"][0]["codigo_venda"],
                        dumps(client_data["dados_venda"][0]),
                    )

                    if cadastar: msg_response = ServerResponse(status="success", msg=(0, "Produto cadastrado com sucesso"))
                    else: msg_response = ServerResponse(msg=(0, "O código de venda já existe, tente outro"))

                    client.send(dumps(asdict(msg_response)).encode())

                elif client_data["request_type"] == "consultar_venda":
                    resultado = consultar_venda(client_data["codigo_venda"])

                    if resultado: msg_response = ServerResponse(status="success", type="data", msg=(1, resultado))
                    else: msg_response = ServerResponse(msg=(0, "O Codigo não foi encontrado"))

                    client.send(dumps(asdict(msg_response)).encode())

            else:
                client.close()

        except (socket.error, KeyboardInterrupt) as e:
            client.close()
            print(f"Conexão com ({address[0]}, {address[1]}) encerrada")
            break


while True:
    try:
        client, address = sock.accept()
        print(f"Conectado com ({address[0]}, {address[1]})")
        Thread(target=vendas, args=(client, address)).start()
    except KeyboardInterrupt:
        sock.close()
        break
    except Exception as e:
        print(e)
