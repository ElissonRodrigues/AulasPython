idades = []

while True:
    try:
        p = int(input('Qual a sua idade?: '))
        if p == 0: break

        idades.append(p)
    except TypeError:
        print ('\nOops, você digitou algo errado!\n')

media = sum(idades)/len(idades)

if 0 < media < 25:
    print (f'\nA classificação desse grupo é jovem')
elif 25 < media < 60:
    print ('\nA classificação desse grupo é adulto')
else:
    print ('\nA classificação desse grupo é idosa')