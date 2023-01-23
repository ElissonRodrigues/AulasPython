from math import factorial as ft

vetor_base = []
loop = 0

def factorial(vetor):
	vetor.sort()
	return [{x: ft(x)} for x in set(vetor)]

tamanho = int(input("Quantos números você quer digitar?: "))

while loop < tamanho:
	loop += 1
	try:
		n = int(input(f"Digite o {loop}º número: "))
		vetor_base.append(n)
	except: 
		print ("O número que você digitou é inválido!")
		loop -= 1

texto = "".join(map(lambda x: f"{list(x.keys())[0]} = {x[list(x.keys())[0]]}\n", factorial(vetor_base)))

print (f"""
Sua lista de número é: {', '.join(map(str, vetor_base))}

Os números dessa lista com seu fatorial: 

{texto}
""")

	
	