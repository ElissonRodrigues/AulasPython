import os

def exercício21():
	a1 = int(input("Informe o primeiro Ângulo: "))
	a2 = int(input("Informe o segundo Ângulo: "))
	
	calc = 180 - (a1 + a2)
	
	os.system('cls' if os.name == 'nt' else 'clear')
	
	print ("\nRESULTADOS DO EXERCÍCIO 21")
	print ("="*50)
	print (f"\nO medida do terceiro ângulo é de {calc}º\n")
	print ("="*50)