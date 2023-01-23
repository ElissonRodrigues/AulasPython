from os import system, name

def exercício02():
	n1 = float(input("Qual a sua primeira nota\n\n>>> "))
	n2 = float(input("Qual a sua segunda nota\n\n>>> "))
	
	if n1 > 10 or n2 > 10: print("Apenas notas de 10 a 0 são aceitas"); return
	
	média = (n1+n2)/2
	
	system('cls' if name == 'nt' else 'clear')
	
	print ("\n\nRESULTADOS DO EXERCÍCIO 2")
	print ("="*50)
	print (f"\nSua média é de {média}\n\n")
	if 0  <= média <= 4:
		print ("Você está reprovado\n")
	elif 4 <= média <= 7: 
		print ("Você está em recuperação\n")
	elif 7 <= média <= 10:
		print ("Você está aprovado\n") 
	print ("="*50)
	