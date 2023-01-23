from os import system, name

def exercício01():
    quantidade = 0
    adição = 0
    
    while True: 
        n = int(input('Digite um numero inteiro: '))
        if n == 0: break
        adição += n
        quantidade += 1
    
    system('cls' if name == 'nt' else 'clear')
    print ("\n\nRESULTADOS DO EXERCÍCIO 1")
    print ("="*50)
    print (f'Você digitou {quantidade} numeros, a soma dos numeros digitados é {adição} e a média é {adição/quantidade:.2f}')
    print ("="*50)