from os import system, name

def exercício10():
	
	altura = float(input("Qual é a sua altura: "))
	sexo = input("\nQual é o seu sexo:\n\nM = Masculino\nF = Feminino\n\n>>> ").lower()
	
	if sexo == "m":
		cálculo = (72.7*altura) - 58
	elif sexo == "f":
		cálculo = (62.1*altura) - 44.7
	else: 
		print ("Oops, parece que você não digitou algo errado");return
	
	system('cls' if name == 'nt' else 'clear')
	
	print ("\n\nRESULTADOS DO EXERCÍCIO 10")
	print ("="*50)
	print (f"O seu peso ideal é {cálculo:.2f}K")
	print ("="*50)
	