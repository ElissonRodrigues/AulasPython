import os

def exercício17():
	raio = float(input("Qual o raio da circunferência\n\n>>> "))
	PI = 3.14
	cir = 2*PI*raio
	area = PI*raio**2
	volume = (4*PI*raio**3)/3
	
	os.system('cls' if os.name == 'nt' else 'clear')
	
	print ("\nRESULTADOS DO EXERCÍCIO 17")
	print ("="*50)
	print (f"A circunferência é de {cir:.2f}cm a area é de {area:.2f}cm² e o volume é {volume:.2f}mm")
	print ("="*50)