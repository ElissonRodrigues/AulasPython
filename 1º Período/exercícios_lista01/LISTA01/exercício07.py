import os

def exercício07():
	salário  = float(input("\nQual é o seu salário:\n\nR$ "))
	vendas  = float(input("\nQual seu número de vendas:\n\n>>> "))
	
	comissão = vendas * 0.04
	salário_final = salário + comissão

	os.system('cls' if os.name == 'nt' else 'clear')
		
	print ("\nRESULTADOS DO EXERCÍCIO 8")
	print ("="*50)
	print (f"\nSua comissão por vendas é de R$ {comissão}, O seu salário final com a comissão é de R$ {salário_final:.2f}\n")
	print ("="*50)