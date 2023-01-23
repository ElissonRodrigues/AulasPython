from os import system,  name

numeros= []

print ("\nUse -1 para encerrar o código\n")
while True:
    numeros.sort()

    for p, v in enumerate(numeros): 
        print (" ".join(map(lambda number: str(number), numeros[:p+1])))

    n = int(input("\nDigite um número inteiro qualquer: "))
    if n == -1: break 
    if not n in numeros: numeros.append(n)
    system('cls' if name == 'nt' else 'clear')
