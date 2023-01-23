quant_mo = float(input('Qual a quantidade de nmorango em KG: '))
quant_ma = float(input('Qual a quantidade de maça em KG: '))

if quant_mo <= 5:
    preço_mo = quant_mo * 2.50
else:
    preço_mo = quant_mo * 2.20


if quant_ma <= 5:
    preço_ma = quant_ma * 1.80
else: 
    preço_ma = quant_ma * 1.50


total = preço_ma+preço_mo
kg_total = quant_ma+quant_mo

if kg_total > 8 or total > 25:
    total = total-(total*0.10)

print(f'Você vai pagar: {round(total)}')