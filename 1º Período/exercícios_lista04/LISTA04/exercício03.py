produtos = {}
caro = {}
barato = {}
menor = 0
maior = 0

n = 0
while True:
    n += 1
    try:
        produto = input(f'Qual o nome do {n}º produto: ')
        if produto.lower() == 'sair':
            break

        preco = float(input(f'Qual o preco do {n}º produto: '))
        produtos[produto] = preco
    except ValueError:
        print('Oops, parece que você digitou algo errado, tente novamente\n\n')
        n -= 1

for x, y in produtos.items():
    if y > maior:
        maior = y
        caro.clear()
        caro[x] = y

    if menor == 0:
        barato[x] = y
        menor = y
    elif y < menor:
        menor = y
        barato.clear()
        barato[x] = y
    
    if y <= 20: 
        reajuste = 0.10 * y
        produtos[x] = y+reajuste
    else:
        reajuste = 0.05 * y
        produtos[x] = y+reajuste

print ('='*35)
print ('PRODUTO MAIS CARO E BARATO')
print ('='*35)
print (f'O Produto mais caro é: {list(caro.keys())[0]}, O seu preço é {round(list(caro.values())[0], 2)}')
print (f'O Produto mais barato é: {list(barato.keys())[0]}, O seu preço é {round(list(barato.values())[0], 2)}\n\n')

print ('='*35)
print ('PRODUTOS  COM 10 E 5% DE AUMENTO')
print ('='*35)
for x, y in produtos.items():
    print (f'Produto: {x}\nPreço reajustado: {round(y, 2)}')
print ('\n')

menor = 0
maior = 0

for x, y in produtos.items():
    if y > maior:
        maior = y
        caro.clear()
        caro[x] = y

    if menor == 0:
        barato[x] = y
        menor = y
    elif y < menor:
        menor = y
        barato.clear()
        barato[x] = y

print ('='*35)
print ('PRODUTO MAIS CARO E BARATO')
print ('='*35)
print (f'O Produto mais caro é: {list(caro.keys())[0]}, O seu preço reajustado é {round(list(caro.values())[0], 2)}')
print (f'O Produto mais barato é: {list(barato.keys())[0]}, O seu preço reajustado é {round(list(barato.values())[0], 2)}')
print ('='*35)
