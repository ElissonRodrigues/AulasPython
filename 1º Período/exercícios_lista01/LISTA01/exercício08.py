from time import sleep 
import os
from traceback import format_exc

def exercício08():
	try:
		peso = int(input("Informe seu peso atual em quilos. Exemplo: 63\n\n>>> "))
		
		emagreceu = 15
		engordou = 20
		
		valor_engordou = peso*15/100
		valor_emagreceu = peso*20/100
		os.system('cls' if os.name == 'nt' else 'clear')
		
		print ("\nRESULTADOS DO EXERCÍCIO 8")
		print ("="*50)
		print (f"Seu peso atual é {peso}\nSe engordar 15%, o seu peso será {peso+valor_engordou}\nSe emagreceu 20%, O seu peso será {peso-valor_emagreceu}")
		print ("="*50)
		
	except ValueError:
		print ("\nOops, você digitou algo errado, tente novamente.")
		sleep(2); exercício08()