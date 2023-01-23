import socket
import struct

host = "localhost"
port = 8081
operações= ["+", "-", "*", "/"]
recv_format = '!i'
send_format = '!i s i'

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = (host, port) 
sock.connect(server_address)

print ("\n\nConectado com sucesso. Para encerrar a conexão use 'sair' para o primeiro número!\n\n")

while True:
    try:
        n1 = input("Digite o primeiro número: ")
        if n1.lower() == "sair": sock.close(); break
        else: n1 = int(n1)
    
        n2 = int(input("Digite o segundo número: "))
        
        escolha = int(input("""
        Escolha uma das operações abaixo:
        
        1 - Soma
        2 - Subtração
        3 - Multiplicação
        4 - Divisão
    
        >>> """.replace("    ", "")))
        
        if 1 <= escolha <= 4: 
            sock.send(struct.pack(send_format, n1, operações[escolha-1].encode(), n2))
            
            print()
            pacote = sock.recv(struct.calcsize(recv_format))
            print (f"{n1} {operações[escolha-1]} {n2} = {pacote.decode()}")
            print ()
            
        else:
            print ("Escolha um número entre 1 e 4. Tente novamente!")
        
    except ValueError:
        print ("Oops, você digitou algo errado, tente novamente ")
