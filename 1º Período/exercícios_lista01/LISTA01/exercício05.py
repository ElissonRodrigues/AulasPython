from time import sleep 
import os
from traceback import format_exc

def exercício05():
	try:
		n1 = int(input("\nInforme a primeira nota\n\n>>> "))
		n2 = int(input("\nAgora a segunda nota\n\n>>> "))
		
		os.system('cls' if os.name == 'nt' else 'clear')
		
		print ("\nRESULTADOS DO EXERCÍCIO 5")
		print ("="*50)
		print (f"""
A sua média ponderada é {(n1*2+n2*3) / 5} com base no seguinte cálculo:

  ({n1}x2+{n2}x3)        {n1*2+n2*3}
------------- = ---------  = {(n1*2+n2*3) / 5}
      5             5
""")
		print ("="*50)
		
	except ValueError:
		print ("\nOops, você digitou algo errado, tente novamente.")
		sleep(2); exercício05()