from os import system, name

def exercício03():
	n1 = int(input('Digite o primeiro número: '))
	n2 = int(input('Digite o segundo número: '))
	
	def maior(y,z):
		mai = y
		mai = y if y > z else z
		return mai

	def menor(y, z):
		men = y
		men = y if y < z else z
		return men
	
	system('cls' if name == 'nt' else 'clear')
	
	print ("\n\nRESULTADOS DO EXERCÍCIO 3")
	print ("="*50)
	print (f'\nO Maior número é {maior(n1, n2)} o menor é {menor(n1, n2)}')
	print ("="*50)
	