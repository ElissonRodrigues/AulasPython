from time import sleep 
import os
from traceback import format_exc

def exercício06():
	try:
		p1 = float(input("\n[10% de desconto] Informe o preço atual do produto\n\n>>> ").replace(",", "."))
		desconto = 10
		#valor_do_desconto = p1*0.10
		valor_do_desconto = p1*desconto/100
		
		os.system('cls' if os.name == 'nt' else 'clear')
		print ("\nRESULTADOS DO EXERCÍCIO 6")
		print ("="*50)
		print (f"O preço atual é: {p1}\nSeu desconto é de {desconto}%\nO preço com {desconto}% de desconto é {p1 - valor_do_desconto:.2f}")
		print ("="*50)
		
	except (NameError):
		print ("\nOops, você digitou um número errado, tente novamente.")
		sleep(2); exercício06()
	except ValueError:
		print ("\nOops, você digitou algo errado, tente novamente.")
		sleep(2); exercício06()
	except:
		print (format_exc())
