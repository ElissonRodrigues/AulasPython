from time import sleep 
import os
from traceback import format_exc

def exercício10():
	try:
		base_maior = int(input("Informe a base maior do trapézio\n\n>>> "))
		base_menor = int(input("\nInforme a base menor do trapézio\n\n>>> "))
		altura = int(input("\nInforme a altura do trapézio\n\n>>> "))
		os.system('cls' if os.name == 'nt' else 'clear')
		
		print ("\nRESULTADOS DO EXERCÍCIO 10")
		print ("="*50)
		print (f"""
A área do trapézio é {(base_maior+base_menor) * altura / 2} com base no seguinte cálculo:
	
 ({base_maior}+{base_menor}) x {altura}        {(base_maior+base_menor) * altura}
--------------- = ----------- = {(base_maior+base_menor) * altura / 2}
       2               2

""")
		print ("="*50)
		
	except ValueError:
		print ("\nOops, você digitou algo errado, tente novamente.")
		sleep(2); exercício10()
	