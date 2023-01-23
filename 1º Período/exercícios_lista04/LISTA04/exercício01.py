quant = int(input('qual a quantidade de numeros que você deseja: '))
numeros_digitados = []

for x in range(1, quant+1):
    n = int(input(f'Digite o {x}° número: '))
    numeros_digitados.append(n)

por2 = ""
por3 = ""
por23 = ""
nao_divi = ""

for y in numeros_digitados:
    if y % 2 == 0: por2 += f'{y}, '
    elif y % 3 == 0: por3 += f'{y}, '
    elif y % 2 == 0 and y % 3 == 0: por23 += f'{y}, '

print (f'Numeros divisíveis por 2: {por2[:-2]}')
print (f'Numeros divisíveis por 3: {por3[:-2]}')
print (f'Numeros divisíveis por 2 e 3: {por23[:-2]}')