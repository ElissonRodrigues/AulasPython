import os

def exercício20():
	lado = int(input("Qual o número de lados do polígono convexo: "))
	
	calc = lado*(lado-3)/2
	
	os.system('cls' if os.name == 'nt' else 'clear')
	
	print ("\nRESULTADOS DO EXERCÍCIO 20")
	print ("="*50)
	print (f"Esse polígono convexo tem {calc} diagonais")
	print ("="*50)