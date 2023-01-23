números = []
multiplicação = ""
divisão = ""

tamanho = int(input("Quantos números você quer digitar? "))

for x in range(1, tamanho+1):
  n = float(input(f'Digite o {x} número'))
  números.append(n)

números.sort()
maior = max(números)
menor = min(números)

print (f"\n\nLista em ordem crescente: {números}\nO Maior Número é: {maior}\nO Menor Número é {menor}\n")

for x in números:
  multiplicação += f'{x} x {maior} = {x*maior:.2f}\n'
  divisão += f'{x} ÷ {menor} = {x/maior:.2f}\n'

print (f"\n\nMultiplicação com o maior número:\n\n{multiplicação}\n\nDivisão com o menor número:\n\n{divisão}")