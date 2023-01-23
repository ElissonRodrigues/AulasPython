import socket
from threading import Thread

operações= ["+", "-", "*", "/"]

host = "localhost"
port = 8082
data_payload = 2048

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((host, port))

print ("Servidor iniciado!")

def calculadora(msg, address):
    print (f"Conectado com '{address}'")
            
    if msg:
        dados = eval(msg)
                
        n1 = dados['n1']
        n2 = dados['n2']
        op = operações[int(dados['op'])-1]
                
        calc = eval(f"{n1} {op} {n2}")
        msg = f"{n1} {op} {n2} = {calc}"
                
        sock.sendto(str(msg).encode(), address)

while True:
    try:
        msg, address = sock.recvfrom(data_payload)
        if msg: Thread(target=calculadora, args=(msg, address)).start()
    except KeyboardInterrupt:
        sock.close()
        break
    except Exception as e:
        print (e)