números = []
adição = 0
multiplicação = 1

tamanho = int(input("Quantos números você quer digitar? "))

for x in range(1, tamanho+1):
  n = float(input(f"Digite o {x}º número: "))
  números.append(str(n))
  adição += n
  multiplicação *= n

print (f"{' + '.join(números)} = {adição}")
print (f"{' x '.join(números)} = {multiplicação}")
