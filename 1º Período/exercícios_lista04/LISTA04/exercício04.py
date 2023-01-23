lista1 = [] 
lista2 = []

tamanho1 = int(input('Quantas pessoas você deseja adicionar a lista1: '))
tamanho2 = int(input('Quantas pessoas você deseja adicionar a lista2: '))

for x in range(1, tamanho1+1):
    n = input(f'Qual o nome da {x}ª pessoal: ')
    lista1.append(n)

print ('\nSEGUNDA LISTA\n')
for x in range(1, tamanho2+1):
    n = input(f'Qual o nome da {x}ª pessoal: ')
    lista2.append(n)

print ('\nLISTA 1')
print (lista1)

print ('LISTA 2')
print (lista2)

print ('LISTA 3')
lista3 = lista1 + lista2
lista3.sort()

print (lista3)

