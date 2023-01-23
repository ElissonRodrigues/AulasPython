salario = float(input('Qual o seu salário: ')) 

if salario <= 280:
    res =  (salario*0.20, 20)
elif 280 <= salario <= 700:
    res = (salario*0.15, 15)
elif 700 <= salario <= 1500:
    res = (salario*0.10, 10)
else:
    res = (salario*0.5, 5)

print (f"""
O seu salário sem o aumento é de R${salario}
O percentual de aumento foi de: {res[1]}%
O valor do aumento é de R${res[0]}
O novo salário é de R${salario+res[0]}
""")