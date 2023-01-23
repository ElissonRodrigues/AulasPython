import os

def exercício16():
	co = float(input("Qual o comprimento do cateto oposto\n\n>>> "))
	ca = float(input("Qual o comprimento do cateto adjacente\n\n>> "))
	
	cal = (ca**2 + co**2) ** (1/2)
	
	os.system('cls' if os.name == 'nt' else 'clear')
	
	print ("\nRESULTADOS DO EXERCÍCIO 16")
	print ("="*50)
	print(f"o valor da hiptenusa é {cal:.2f}")
	print ("="*50)