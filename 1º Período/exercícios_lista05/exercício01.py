from time import sleep 

count = 0
notas = []

def média(código, *args):
	if código.upper() == "A": return (sum(args))/len(args)
	elif código.upper() == "P": return (args[0]*5 + args[1]*3 + args[2]*2)/(5+3+2)
	else: return -1
	
código = input("Escolha uma das opções abaixo:\nA - Média aritmética\nP - Média ponderada\n\n>>> ")

while count < 3:
	count += 1
	n = float(input(f"Digite a {count}ª nota: "))
	
	if 0 <= n <= 10:
		notas.append(n)
	else:
		print ("\nNota inválida! tente novamente\n\n")
		sleep(2)
		count -= 1

print (f"O resultado é: {média(código, *notas):.2f}")
		