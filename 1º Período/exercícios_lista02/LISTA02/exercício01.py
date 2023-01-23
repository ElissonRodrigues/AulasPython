from os import system, name

def exercício01():
	notas = []
	
	def questões(n): n = float(input(f"Qual a sua {n}ª nota: ")); notas.append(n)
	for x in range(1, 5): questões(x); print('\033[1A' + '\033[K', end='')
	
	média = (notas[0] + notas[1] + notas[2] + notas[3]) / len(notas)
	
	system('cls' if name == 'nt' else 'clear')
	
	print ("\n\nRESULTADOS DO EXERCÍCIO 1")
	print ("="*50)
	if média >= 7: print (f"\nVocê foi aprovado. Sua média é {média}\n")
	else: print (f"\nVocê foi reprovado. Sua média é: {média}\n")
	print ("="*50)
	