from time import sleep 
import os
from traceback import format_exc

def exercício03():
	try:
		n1 = int(input("\nInforme o primeiro número inteiro\n\n>>> "))
		n2 = int(input("\nAgora o segundo número inteiro\n\n>>> "))
		os.system('cls' if os.name == 'nt' else 'clear')
		
		print ("\nRESULTADOS DO EXERCÍCIO 3")
		print ("="*50)
		print (f"""
        Divisão Inteira: {n1} // {n2} = {n1//n2}
        Resto: {n1} % {n2} = {n1%n2}
        Divisão Real: {n1} / {n2} = {n1/n2}
		""".replace("        ", "")
		)
		print ("="*50)
		
	except ZeroDivisionError:
		print ("Oops, parece que você digitou um zero. O Zero não é divisível. Tente novamente.")
		sleep(2); exercício03()
	except ValueError:
		print ("\nOops, você digitou algo errado, tente novamente.")
		sleep(2); exercício03()
	except:
		print (format_exc())