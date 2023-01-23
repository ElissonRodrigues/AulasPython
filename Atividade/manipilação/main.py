from sys import exit as sair 
from os import system, name
from time import sleep
from gestão.alunos import Alunos

alunos = Alunos()

while True:
    opts = 0

    try:
        opts = int(input('''
        Escolha uma das opções abaixo:

        1 - Finalizar o programa
        2 - Cadastrar aluno
        3 - Mostrar relatório

        >>> '''.replace('        ', '')))

    except ValueError:
        print ('Escolha um numero entre 1 e 3')
        
    system('cls' if name == 'nt' else 'clear')
    
    if 1 <= opts <= 3:
        if opts == 1:
            sair()
        elif opts == 2:
            try:
                notas = []
                matricula = int(input("Matrícula do aluno: "))
                nome = input("Nome do aluno: ")
                curso = input("Nome do curso: ")
                
                a = 0
                print ()
                while a < 4:
                    try:
                        a += 1
                        n = float(input(f"Digite a {a}º nota: "))
                        print('\033[1A' + '\033[K', end='')
                        if 0 <= n <= 10: notas.append(n)
                        else: print ("Digite uma nota entre 0 e 10");sleep(3);print('\033[1A' + '\033[K', end=''); a -= 1
                            
                    except Exception as e:
                        print (f"\nNota inválida!")
                        print('\033[1A' + '\033[K', end='')
                        sleep(4)
                        print('\033[2A' + '\033[K', end='')
                        a-=1
                    
                alunos.cadastrar(
                        nome=nome, 
                        matricula=matricula, 
                        curso=curso,
                        notas=notas
                )
            except ValueError:
                system('cls' if name == 'nt' else 'clear')
                print ("O valor digitado é inválido!")
                print('\033[1A' + '\033[K', end='')
                sleep(4)
        else:
            system('cls' if name == 'nt' else 'clear')
            alunos.relatório()
    else:
        print ('Escolha um numero entre 1 e 3')