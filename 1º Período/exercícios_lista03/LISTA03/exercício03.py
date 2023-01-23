from os import system, name

def exercício03():
    resultado=1
    n = int(input("Fatorial de: ") )
    
    if n < 0: 
        print ("O Número digitado é inválido, digite um número maior ou igual a 0\n")
    else:
        for x in range(1, n+1): resultado *= x
        system('cls' if name == 'nt' else 'clear')
        print ("\n\nRESULTADOS DO EXERCÍCIO 3")
        print ("="*50)
        print(f'O Fatorial de {n} é {resultado}')
        print ("="*50)