from time import sleep 
import os
from traceback import format_exc

def exercício09():
	try:
		peso = int(input("Informe seu peso atual em quilos. Exemplo: 63\n\n>>> "))
		os.system('cls' if os.name == 'nt' else 'clear')
		
		print ("\nRESULTADOS DO EXERCÍCIO 9")
		print ("="*50)
		print (f"Seu peso em Quilos é {peso}KG\nSeu peso em gramas é {peso*1000}G")
		print ("="*50)
		
	except ValueError:
		print ("\nOops, você digitou algo errado, tente novamente.")
		sleep(2); exercício09()