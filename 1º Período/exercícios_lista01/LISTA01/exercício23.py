import os

def exercício23():
	valor_saque = int(input("Digite o valor do saque: "))
	
	notas_restantes = valor_saque
	
	quantidade_100 = valor_saque // 100
	notas_restantes -= 100 * quantidade_100
	quantidade_50 = notas_restantes % 100 // 50
	notas_restantes -= 50 * quantidade_50
	quantidade_20 = notas_restantes // 2 // 10
	notas_restantes -= 20 * quantidade_20
	quantidade_10 = notas_restantes // 10
	notas_restantes -= 10 * quantidade_10
	quantidade_5 = notas_restantes // 5
	notas_restantes -= 5 * quantidade_5
	
	os.system('cls' if os.name == 'nt' else 'clear')
	print ("\nRESULTADOS DO EXERCÍCIO 23")
	print ("="*50)
	print (f"""
Resultado do saque de R$ {valor_saque}

Notas de 100: {quantidade_100}
Notas de 50: {quantidade_50}
Notas de 20: {quantidade_20}
Notas de 10: {quantidade_10}
Notas de 5: {quantidade_5}
Valor restante: R$ {notas_restantes}
""")
	print ("="*50)
