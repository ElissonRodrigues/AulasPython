from time import sleep 
import os
from traceback import format_exc

def exercício04():
	try:
		a = int(input("\n[A] Informe o primeiro número\n\n>>> "))
		b = int(input("\n[B] Agora o segundo número\n\n>>> "))
		
		a_previous = a
		b_previous = b 
		
		a = b_previous
		b = a_previous
		
		os.system('cls' if os.name == 'nt' else 'clear')
		print ("\nRESULTADOS DO EXERCÍCIO 4")
		print ("="*50)
		print (f'A era {a_previous}, agora A é {a}\nB era {b_previous}, agora B é {b}')
		print ("="*50)
		
	except ValueError:
		print ("\nOops, você digitou algo errado, tente novamente.")
		sleep(2); exercício04()