from os import system, name

def exercício04():

    n1 = int(input('Digite o primeiro número: '))
    n2 = int(input('Digite o segundo número: '))
    n3 = int(input('Digite o terceiro número: '))

    def maior(x,y,z):
        mai = x
        if y > x: mai = y
        if z > x: mai = z
        return mai

    def menor(x,y,z):
        men = x
        if y < x: men = y
        if z < x: men =z 
        return men

    system('cls' if name == 'nt' else 'clear')
    
    print ("\n\nRESULTADOS DO EXERCÍCIO 4")
    print ("="*50)
    print (f'O Maior número é {maior(n1, n2, n3)} o menor é {menor(n1, n2, n3)}')
    print ("="*50)
    