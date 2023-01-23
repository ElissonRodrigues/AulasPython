from os import system, name

def exercício06():
	salario = float(input('Qual o seu sálario ? '))
	print ("\n\nRESULTADOS DO EXERCÍCIO 06")
	print ("="*50)
	
	if salario <= 500:
		aumento = salario*0.30
		print (f'Você tem direito ao benéficio. Seu sálario atual é {salario}, com o reajuste de 30% você vai receber {salario+aumento:.2f} ')
	else:
		print ('Você não tem direito ao benefício ')
	print ("="*50)
	