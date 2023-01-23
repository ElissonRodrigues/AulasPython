n1 = int(input('Digite o primeiro número inteiro: '))
n2 = int(input('Digite o segundo número inteiro: '))

n3 = eval(input('Digite o segundo número real: '))

a = (n1*2)*(n2/2)
b = (n1*3)+n3
c = n3**2

print(f'''
O produto do dobro do primeiro com metade do segundo é {a}
A soma do triplo do primeiro com o terceiro é {b}
O terceiro elevado ao cubo é {c}
''')
