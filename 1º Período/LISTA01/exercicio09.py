tamanho = float(input('Qual o tamanho em metros quadrados da área a ser pintada: '))

litros = round(tamanho/3)
latas = round(litros/18)

if latas == 0: latas = 1

print (f'''
Você vai precisar compra {latas} {"latas" if latas > 1 else "lata" }
Para comprar {latas} {"latas" if latas > 1 else "lata" } você vai gastar R$ {latas*80}
''')
