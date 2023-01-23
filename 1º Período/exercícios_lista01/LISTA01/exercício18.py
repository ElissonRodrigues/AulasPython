import os

def exercício18():
	temp_c = int(input("Qual a temperatura em Celsius: "))
	
	convert = (9/5)*temp_c+32
	
	os.system('cls' if os.name == 'nt' else 'clear')
	
	print ("\nRESULTADOS DO EXERCÍCIO 18")
	print ("="*50)
	print (f"\n{temp_c}Cº é equivalente a {convert:.2f}Fº\n")
	print ("="*50)