from os import system, name

def exercício13():
	preço = int(input("Qual o preço do produto: "))
	categoria = input("\nQual a categoria ?\n\nLimpeza\nAlimentação\nVestuário\n\n>>> ").lower()
	situação = input("\nQual a situação do Produto: \n\nR = Precisa de refrigeração\nS = Não Precisa de refrigeração\n\n>>> ").lower()
	
	if preço <= 25:
		if categoria  == "limpeza":
			aumento = preço*0.05
		elif categoria == "alimentação":
			aumento == preço*0.08
		elif categoria == "vestuário":
			aumento = preço*0.10
		else:
			aumento = preço
	
	elif preço > 25:
		if categoria  == "limpeza":
			aumento = preço*0.12
		elif categoria == "alimentação":
			aumento = preço*0.15
		elif categoria == "vestuário":
			aumento = preço*0.18
		else:
			aumento = preço
	
	if categoria == "alimentação" or situação == "r":
		imposto = preço*0.05
	else:
		imposto = preço*0.08
		
	preco_total = preço + aumento + imposto 
	
	def classificação(preço_total):
		if preço_total <= 50: return "Barato"
		elif 50 <= preço_total <= 120: return "Normal"
		elif preço_total >= 120: return "Caro"
	
	system('cls' if name == 'nt' else 'clear')
	
	print ("\n\nRESULTADOS DO EXERCÍCIO 13")
	print ("="*50)
	print (f"Preço Original: R${preço:.2f}\nValor do aumento: R${aumento:.2f}\nValor do imposto: R${imposto:.2f}\nPreço total a pagar: R${preco_total:.2f}\nClassificação de preço: {classificação(preco_total)}")
	print ("="*50)
	