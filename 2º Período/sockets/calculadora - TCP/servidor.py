import socket
from threading import Thread
import struct

host = "localhost"
port = 8081
recv_format = '!i s i'
send_format = '!i'

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((host, port))
sock.listen(10)

print ("Servidor iniciado!")

def calculadora(client, address):
    while True:
        try:
            print (f"Conectado com '{address}'")
            pacote = client.recv(struct.calcsize(recv_format))
            
            if pacote:
                n1, op, n2 = struct.unpack(recv_format, pacote)
                calculo = eval(f'{n1} {op.decode()} {n2}')
                
                client.send(str(calculo).encode())
            else:
                client.close()
                
        except (socket.error, KeyboardInterrupt) as e:
            client.close()
            print (f"CONEXÃO COM {address} encerrada")
            break

while True:
    try:
        client, address = sock.accept()
        Thread(target=calculadora, args=(client, address)).start()
    except KeyboardInterrupt:
        sock.close()
        break
    except Exception as e:
        print (e)
        