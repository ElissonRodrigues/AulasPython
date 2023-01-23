from time import sleep 
import os
from traceback import format_exc

def exercício13():
	s1 = int(input("Qual o primeiro salário fictício? "))
	s2 = int(input("Qual o segundo salário? "))
	
	salário = s1//s2
	
	print ("\nRESULTADOS DO EXERCÍCIO 13")
	print ("="*50)
	print (f"A quantidade de salário mínimo é: {salário}")
	print ("="*50)