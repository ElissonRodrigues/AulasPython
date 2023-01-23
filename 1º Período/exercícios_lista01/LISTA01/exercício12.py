from time import sleep 
import os
from traceback import format_exc

def exercício12():
	try:
		diagonal_maior = int(input("Qual a diagonal maior do losango\n\n>>> "))
		diagonal_menor = int(input("\nQual a diagonal manor do losango\n\n>>> "))
		
		os.system('cls' if os.name == 'nt' else 'clear')
		print ("\nRESULTADOS DO EXERCÍCIO 12")
		print ("="*50)
		print (f"""
a área do losango é {(diagonal_maior*diagonal_menor)/2} com base no seguinte cálculo: 
	
   ({diagonal_maior} x {diagonal_menor})          {diagonal_maior*diagonal_menor}
--------------- = ----------- = {(diagonal_maior*diagonal_menor)/2}
       2               2
	""")
		print ("="*50)
		
	except ValueError:
		print ("\nOops, você digitou algo errado, tente novamente.")
		sleep(2); exercício12()