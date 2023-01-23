from os import system, name
    
#INPUT DO USUÁRIO
def user_input():
    n1 = int(input("\nDigite o primeiro número: "))
    n2 = int(input("\nDigite o segundo número: ")) 
    
    system('cls' if name == 'nt' else 'clear')
    print ("\n\nRESULTADOS DO EXERCÍCIO 5")
    print ("="*50)
    return (n1, n2)

#QUESTÕES
def opção01():
    number_strings = ""
    numeros = []
    adição = 0
        
    def pergunta(n):  nu = int(input(f'Qual é o {n}º número: ')); numeros.append(nu)
    quantidade = int(input('\nVocê quer fazer a média de quantos números: '))
    print ("\n")
    
    for x in range(1, quantidade+1): pergunta(x); print('\033[1A' + '\033[K', end='')
    for x in numeros: adição += x; number_strings += f"{x}" if number_strings  == "" else f", {x}"
    
    system('cls' if name == 'nt' else 'clear')
    print ("\n\nRESULTADOS DO EXERCÍCIO 5")
    print ("="*50)
    print (f"\nA Média entre {number_strings} é {adição/len(numeros):.2f}\n")
    
def opção02():
    n1, n2 = user_input()
    if n1 > n2: print (f"\nA diferença entre {n1} e {n2} é de {n1-n2}\n")
    else: print (f"\nA diferença entre {n2} e {n1} é de {n2-n1}\n")
    
def opção03():
    n1, n2 = user_input()
    print (f"\nO Produto de {n1} e {n2} é {n1*n2}\n")
    
def opção04():
    n1, n2 = user_input()
    print (f"\nA Divisão de {n1} por {n2} é {n1/n2:.2f}\n")
    
def opção05():
    n1, n2 = user_input()
    print (f"\n{n1} elevado á {n2} é {n1**n2:.2f}\n")
    
def opção06():
    n1, n2 = user_input()
    print (f"\nA raiz quadrada de {n1} é {n1 ** (1/2):.2f}, já a raiz quadrada de {n2} é {n2 ** (1/2):.2f}\n")
    
def opção07():
    n1, n2 = user_input()
    print (f"\nA raiz cúbica de {n1} é {n1 ** (1/3):.2f}, já a raiz cúbica de {n2} é: {n2 ** (1/3):.2f}\n")
    
#EXECUÇÃO PRINCIPAL

def exercício05():
	while True:
		escolha = int(input('''
        O que o você deseja fazer: 
        
        0 = Finalizar questão
        1 = Média entre os números digitados 
        2 = Diferença do maior pelo menor
        3 = Produto entre os números digitados
        4 = Divisão do primeiro pelo segundo
        5 = O primeiro número elevado ao segundo número
        6 = Raiz quadrada de cada um dos números
        7 = Raiz cúbica de cada um dos números
        
        >>> '''.replace('        ', '')))
		if escolha == 0: break
		elif escolha in (1, 2, 3, 4, 5, 6, 7): exec (f'opção0{escolha}()');  print ("="*50)
		else: print ('Escolha inválida, tente novamente')
		