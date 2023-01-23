from os import system, name

def exercício09():
	p = float(input('Qual o preço do produto: '))
	
	aumento = 0
	porcentagem = 0
	
	if p <= 50: 
		aumento = p+p*0.05
		porcentagem = 10
	elif 50 <= p <= 100: 
		aumento = p+p*0.10
		porcentagem = 10
	elif p > 100: 
		aumento = p+p*0.15
		porcentagem = 15
	
	system('cls' if name == 'nt' else 'clear')
	
	print ("\n\nRESULTADOS DO EXERCÍCIO 9")
	print ("="*50)
	if aumento <= 80:
		print (f"Com o aumento de {porcentagem}% esse produto está custando R${aumento}\n\nA Classificado do produto é: barato")
	elif 80 <= aumento <= 120:
		print (f"Com o aumento de {porcentagem}% esse produto está custando R${aumento}\n\nA Classificado do produto é: normal")
	elif 120 <= aumento <= 200:
		print (f"com o aumento de {porcentagem}% esse produto está custando R${aumento}\n\nA Classificado do produto é: caro")
	elif aumento > 200:
		print (f"Com o aumento de {porcentagem}% esse produto está custando R${aumento}\n\nA Classificado do produto é: muito caro")
	print ("="*50)
	