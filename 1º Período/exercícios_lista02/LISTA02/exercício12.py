from os import system, name

def exercício12():

	codigo = int(input('Qual o codigo do produto: '))
	quantidade = int(input('\nQual a quantidade de produtos: '))
	preco_unitario = 0
	
	if codigo > 40: print ('Codigo invalido!'); return
	
	elif 1 <= codigo <= 10: 
	    preco_unitario = 10
	elif 11 <= codigo <= 20: 
	    preco_unitario = 15
	elif 21 <= codigo <= 30: 
	    preco_unitario = 20
	elif 31 <= codigo <= 40: 
	    preco_unitario = 30
	
	preco_total = quantidade*preco_unitario
	
	if preco_unitario <= 250:
	    desconto = preco_unitario*0.05
	elif 250 <= preco_unitario <= 500:
	    desconto = preco_unitario*0.10
	elif preco_unitario > 500: 
	    desconto = preco_unitario*0.15
	
	system('cls' if name == 'nt' else 'clear')
	
	print ("\n\nRESULTADOS DO EXERCÍCIO 12")
	print ("="*50)
	print (f'Preço unitário: R${preco_unitario}\nPreço total da nota: R${preco_total:.2f}\nValor de desconto: R${desconto}\nPreço total com desconto {preco_total-desconto:.2f}')
	print ('='*50)
	