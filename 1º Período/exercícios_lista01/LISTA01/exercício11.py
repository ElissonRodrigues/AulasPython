from time import sleep 
import os
from traceback import format_exc

def exercício11():
	try:
		lado = int(input("Digite o lado do quadrado\n\n>>> "))
		os.system('cls' if os.name == 'nt' else 'clear')
		
		print ("\nRESULTADOS DO EXERCÍCIO 11")
		print ("="*50)
		print (f"\nA área do quadrado é {lado*lado}\n")
		print ("="*50)
		
	except ValueError:
		print ("\nOops, você digitou algo errado, tente novamente.")
		sleep(2); exercício11()