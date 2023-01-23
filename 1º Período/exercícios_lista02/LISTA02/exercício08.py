from os import system, name

def exercício08():
	saldo_medio = float(input('Qual o seu saldo médio: '))
	
	credito = 0 
	
	if saldo_medio > 400: 
	    credito = saldo_medio*0.30
	elif 400 <= saldo_medio >= 300:
	    credito = saldo_medio*0.25
	elif 300 <= saldo_medio >= 200:
	    credito = saldo_medio*0.20
	elif saldo_medio < 200: 
	    credito = saldo_medio*0.10
	
	system('cls' if name == 'nt' else 'clear')
	
	print ("\n\nRESULTADOS DO EXERCÍCIO 8")
	print ("="*50)
	print (f'seu credito é de R${credito:.2f}')
	print ("="*50)
	