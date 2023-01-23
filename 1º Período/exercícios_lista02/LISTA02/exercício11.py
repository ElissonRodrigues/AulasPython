from os import system, name

def exercício11():
	
	código = int(input("Qual o código de origem de produto: "))
	
	if código == 1:
		origem = "Sul"
	elif código == 2:
		origem = "Norte"
	elif código == 3:
		origem = "Leste"
	elif código == 4: 
		origem = "Oeste"
	elif 5 <= código <= 6 or 21 <= código <= 30:
		origem = "Nordeste"
	elif 7 <= código <= 9:
		origem = "Sudeste"
	elif 10 <= código <= 20:
		origem = "Centro-oeste"
	system('cls' if name == 'nt' else 'clear')
	
	print ("\n\nRESULTADOS DO EXERCÍCIO 11")
	print ("="*50)
	print (f"Esse produto é do {origem}")
	print ("="*50)
	