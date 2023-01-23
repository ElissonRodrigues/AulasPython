import socket

host = "localhost"
port = 8082
data_payload = 2048

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
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
            dic = {'n1': n1, 'n2': n2, 'op': escolha}
            sock.sendto(str(dic).encode(), server_address)
            
            print()
            print (sock.recv(data_payload).decode())
            print ()
            
        else:
            print ("Escolha um número entre 1 e 4. Tente novamente!")
        
    except ValueError:
        print ("Oops, você digitou algo errado, tente novamente ")
