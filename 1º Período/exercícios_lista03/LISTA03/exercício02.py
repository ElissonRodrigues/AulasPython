from os import system, name

def exercício02():
    while True: 
        n = int(input('Digite um numero de 1 a 9: '))
        if 1 <= n <= 9:
            inicio = int(input('\nCom qual numero a tabela deverá começar: '))
            final = int(input('\nCom qual numero a tabela deve terminar: '))
            break
        else:
            print ('\nVocê usou um valor inválido, tente novamente')
    
    tabuada=""
    
    for y in range(inicio, final+1):
        tabuada += f"\n{n} + {y} = {n+y} | {n} x {y} = {n*y}"
    
    system('cls' if name == 'nt' else 'clear')
    print ("\n\nRESULTADOS DO EXERCÍCIO 2")
    print ("="*50)
    print (tabuada)
    print ("="*50)