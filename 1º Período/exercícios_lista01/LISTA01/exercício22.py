import os

def exercício22():
	h = int(input("Qual é a hora ? "))
	m = int(input("Agora infome os minutos "))
	
	h_para_m = h*60
	total_m = h_para_m + m
	total_s = total_m*60
	
	os.system('cls' if os.name == 'nt' else 'clear')
	
	print ("\nRESULTADOS DO EXERCÍCIO 22")
	print ("="*50)
	print (f"\n{h} Hora em minutos é {h_para_m}, o total de minutos é {total_m}, já o total de segundos é {total_s} segundos.\n")
	print ("="*50)
	