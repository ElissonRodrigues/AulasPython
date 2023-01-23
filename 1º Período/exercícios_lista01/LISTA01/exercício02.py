from time import sleep 
import os
from traceback import format_exc

def exercício02():
	print ("\n\n[EXERCÍCIO 2] Eu vou usar 3 números reais para subtrair, multiplicar, dividir e somar. Informe esses números abaixo:\n\n") 
	
	try:
		n1 = eval(input("\nInforme o primeiro número\n\n>>> ").replace(",", "."))
		n2 = eval(input("\nAgora o segundo\n\n>>> ").replace(",", ""))
		n3 = eval(input("\nPor último, o terceiro\n\n>>> ").replace(",", "."))
		
		os.system('cls' if os.name == 'nt' else 'clear')
		print ("\nRESULTADOS DO EXERCÍCIO 2")
		print ("="*50)
		print (f"""
        Subtração: {n1}-{n2}-{n3} = {n1-n2-n3}
        Soma: {n1}+{n2}+{n3} = {n1+n3+n3}
        Multiplicação: {n1}x{n2}x{n3} = {n1*n2*n3}
        Divisão: {n1}÷{n2}÷{n3} = {n1/n2/n3}
		""".replace("        ", "")
		)
		print ("="*50)
		
		
	except (UnboundLocalError, NameError):
		print ("\nOops, você digitou um número errado, tente novamente.")
		sleep(2); exercício02()
	except:
		print (format_exc())