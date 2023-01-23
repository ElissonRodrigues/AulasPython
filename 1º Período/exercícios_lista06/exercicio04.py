from sys import exit as sair
import pandas as pd
from time import sleep
from os import system, name
from pandas.errors import EmptyDataError
from unidecode import unidecode

sleep_time = 4
pd.set_option('display.max_columns', None) # coluna
pd.set_option('display.max_rows', None) # linha

def menu(escolha=-1):
    while True:
        try:
            escolha = int(input('''
            Escolha sua opção:
        
            0 – Sair do programa
            1 – Cadastrar um novo produto
            2 – Listar todos os produtos cadastrados
            3 – Listar todos os produtos entre uma faixa de preços
            4 – Mostrar um produto a partir de seu código
            
            >>> '''.replace('    ', '')))
        except ValueError:
            system('cls' if name == 'nt' else 'clear')
            print ('O valor digitado é inválido! Tente novamente.')
            sleep(sleep_time)

        if 0 <= escolha <= 4:
            system('cls' if name == 'nt' else 'clear')
            
            try:
                if escolha == 0:
                    sair()
                elif escolha == 1:
                    try:
                        codigo = int(input('digite o código do produto: '))
                        nome = input('\nDigite o nome do produto: ').capitalize()
                        preço = float(input('\nDigite o preço do produto: R$ '))
                        quantidade_estoque = int(input(f'\nQual a quantidade de {nome} você tem em estoque: '))
                        fornecedor = input("\nQual o fornecedor: ")
                        cadastrar_produto(codigo=codigo, nome=nome, preço=preço, quantidade_estoque=quantidade_estoque, fornecedor=fornecedor)
                    except ValueError:
                        print ('\n\nO valor digitado é inválido! Tente novamente.')
                        sleep(sleep_time)

                elif escolha == 2:
                    lista_produtos()
                    
                elif escolha == 3: 
                    try:
                        fx = []
                        maximo = float(input("Qual o preço máximo que você deseja buscar: R$ "))
                        fx.append(maximo)
                        mínimo = float(input("Agora digite o preço mínimo: R$ "))
                        fx.append(mínimo)
                        
                        faixa_produtos(max(fx), min(fx))
                    except ValueError:
                        print ('O valor digitado é inválido! Tente novamente.')
                        sleep(sleep_time)
                        
                else:
                    código_produto(int(input("Digite o código do produto: ")))
                    
            except ValueError:
                print ('O valor digitado é inválido! Tente novamente.')

def cadastrar_produto(**kargs):
    try:
        df1 = pd.read_csv('estoque.csv')

        if df1.query(f"codigo=={str(kargs.get('codigo'))}").index.empty:

            data = {
                
                'codigo': [kargs.get('codigo')],
                'nome': [kargs.get('nome')],
                'preço': [kargs.get('preço')],
                'quantidade_estoque': [kargs.get('quantidade_estoque')],
                'fornecedor': [kargs.get('fornecedor')]
            }

            df2 = pd.concat([df1, pd.DataFrame(data)])
            df2.to_csv('estoque.csv', index=False)
            
            system('cls' if name == 'nt' else 'clear')
            print("PRODUTO CADASTRADO!")
            sleep(sleep_time)
        else:
            print ('esse produto já está cadastrado!')
        
    except EmptyDataError:
        data = {
            
            'codigo': [kargs.get('codigo')],
            'nome': [kargs.get('nome')],
            'preço': [kargs.get('preço')],
            'quantidade_estoque': [kargs.get('quantidade_estoque')],
            'fornecedor': [kargs.get('fornecedor')]
        }

        df = pd.DataFrame(data)
        df.to_csv('estoque.csv', index=False)
        
        system('cls' if name == 'nt' else 'clear')
        print("PRODUTO CADASTRADO!")

def lista_produtos():
    try:
        df = pd.read_csv('estoque.csv')
        print (df)
        sleep(sleep_time)
        
    except EmptyDataError:
        print ("\nNenhum produto cadastrado na base de dados!.\n\n>>> Use a opção 1 para cadastro alguns produtos ")
        sleep(sleep_time)

def faixa_produtos(maior, menor):
    try:
        df = pd.read_csv('estoque.csv')
        print ()
        search = df.query(f"{menor} <= preço <= {maior}")
        system('cls' if name == 'nt' else 'clear')
        
        if search.index.empty:
            print (f"\nNenhum produto na faixa de preço de {menor} a {maior} R$")
        else:
            print (search)
            
        sleep(sleep_time)
    except EmptyDataError:
        print ("\nNenhum produto cadastrado na base de dados!.\n\n>>> Use a opção 1 para cadastro alguns produtos ")
        sleep(sleep_time)
        
def código_produto(código):
    try:
        df = pd.read_csv('estoque.csv')
        search = df.query(f"codigo=={código}")
        system('cls' if name == 'nt' else 'clear')
        
        if search.index.empty:
            print (f"\n\nNenhum produto encontrado com o código: {código}")
        else:
            print (search)
    except EmptyDataError:
        print ("\nNenhum produto cadastrado na base de dados!.\n\n>>> Use a opção 1 para cadastro alguns produtos ")
        sleep(sleep_time)        
    
    sleep(sleep_time)
    
menu()
