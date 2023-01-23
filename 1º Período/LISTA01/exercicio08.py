sa = float(input("Quanto você ganha por hora trabalhada?: "))
ho = float(input("Quantas horas você trabalhou?: "))

salario_bruto = sa*ho

imp_renda = salario_bruto*0.11
inss = salario_bruto*0.08
sindicato = salario_bruto*0.05

salario_liquido = salario_bruto-imp_renda-inss-sindicato-imp_renda

print (f'''
O salário bruto é de R${salario_bruto}.
Foi descontado R${inss} do INSS.
Foi descontado R${imp_renda} para o Imposto de Renda.
Foi descontado R${sindicato} para o sindicato.

Seu salário liquido é de R${round(salario_liquido, 2)}
''')

