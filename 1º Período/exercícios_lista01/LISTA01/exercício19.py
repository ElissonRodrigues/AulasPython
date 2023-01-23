import os

def exercício19():
	comprimento = float(input("Qual o comprimento do cômodo: "))
	largura = float(input("Qual a Largura do cômodo: "))
	
	area = comprimento * largura
	potência = area * 18
	
	os.system('cls' if os.name == 'nt' else 'clear')
	
	print ("\nRESULTADOS DO EXERCÍCIO 19")
	print ("="*50)
	print (f"\nSeu cômodo é de {area:.2f}m², a potência de iluminação deve ser de {potência:.2f}W\n")
	print ("="*50)