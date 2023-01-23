números = []
contados = []
tamanho = int(input("Quantos números você quer digitar? "))

for x in range(1, tamanho+1):
  n = input(f"\nDigite o {x}º número: ")
  números.append(n)

for x in números:
  if not x in contados:
    q = números.count(x)
    contados.append(x)
    print (f'{x} aparece {q} {"vez" if q <= 1 else "vezes"}')
  