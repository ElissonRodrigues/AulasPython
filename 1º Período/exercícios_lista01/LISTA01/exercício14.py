def exercício14():
	
	numero = int(input("Qual tabuada de multiplicação e adição você deseja? Exemplo: 10\n\n>>> "))
	
	size = 25
	
	print ("="*size + "\nTABUADA DE MULTIPLICAÇÃO" + "\n" + "="*size)
	for x in range(10): print(f"{numero} x {x+1} = {numero*(x+1)}")
	print ("="*size + "\n\n")
	
	print ("="*size + "\nTABUADA DE ADIÇÃO" + "\n" + "="*size)
	for x in range(10): print(f"{numero} + {x+1} = {numero+(x+1)}")
	print ("="*size + "\n\n")
	
	print ("="*size + "\nTABUADA DE SUBTRAÇÃO" + "\n" + "="*size)
	for x in range(10): print(f"{numero} - {x+1} = {numero-(x+1)}")
	print ("="*size + "\n\n")

	print ("="*size + "\nTABUADA DE DIVISÃO" + "\n" + "="*size)
	for x in range(10): print(f"{numero} ÷ {x+1} = {numero/(x+1):.2f}")
	print ("="*size + "\n\n")
	