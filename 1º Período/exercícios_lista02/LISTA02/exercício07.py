from os import system, name

def exercício07():
	salario = float(input('Qual o seu sálario ? '))
	
	if salario <= 300: reajuste = (salario*0.35, 35)
	else: reajuste = (salario*0.15, 15)
	
	system('cls' if name == 'nt' else 'clear')
	
	print ("\n\nRESULTADOS DO EXERCÍCIO 7")
	print ("="*50) 
	print (f'Você vai receber R${reajuste[0]+salario} com reajuste de {reajuste[1]}%')
	print ("="*50)
	