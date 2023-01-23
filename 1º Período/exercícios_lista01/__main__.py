from time import sleep
from glob import glob
import os
from traceback import format_exc
from pathlib import Path

files = sorted(glob("exercícios_lista01/LISTA01/*.py"))

texto = '\n\n' + '-'*13 + " Iniciando exercícios " + '-'*13 + '\n'
print (f"\n\033[1;97;42m{texto}\033[m\n\n")

sleep(1)

for name in files:
	with open(name) as a:
		patt = Path(a.name)
		plugin_name = patt.stem
		exec (f"from exercícios_lista01.LISTA01.{plugin_name} import {plugin_name}")
		print("Imported => " + plugin_name)

def executar_tudo():
	for name in files:
		with open(name) as a:
			patt = Path(a.name)
			plugin_name = patt.stem
			texto = '-'*10 + f" Executando {plugin_name}.py " + '-'*10
			print (f"\n\033[1;36;41m{texto}\033[m\n\n")
			exec (f"{plugin_name}()")
			
	print ("\nRetornando ao menu principal..."); sleep(3)
	print('\033[1A' + '\033[K', end='')

#GESTÃO DE EXERCÍCIOS
def main():
	try:
		execution_value = input(f'\n\n\033[1;31mDigite o número do exercício da Lista NÚMERO 1 que você deseja executar\033[m\n\nDisponibilidade: 1 ao {len(files)}. \n\n\033[1mDigite \033[1;32m"Todos"\033[m \033[1mpara executar todos os exercícios ou \033[1;32m"Sair"\033[m \033[1mpara encerrar o script.\033[m \n\n>>> ')
		if execution_value.isalnum(): execution_value = int(execution_value)
	except ValueError: pass
	
	try:		
		if type(execution_value) is int and len(str(execution_value)) <= 2 and execution_value > 0 and not execution_value > len(files) or type(execution_value) is str:
			if type(execution_value) is str:
				if "sair" in execution_value.lower(): return False
				elif "todos" in execution_value.lower(): executar_tudo()
				else: print ("\n\nOops, parece que você digitou algo errado, tente novamente em 3 segundos");sleep(3); return
			else: 
				if execution_value == 0: execution_value = 1
				if execution_value < 10: execution_value = f"0{execution_value}"
				
				os.system('cls' if os.name == 'nt' else 'clear')
				texto = '-'*10 + f" Executando exercício{execution_value}.py " + '-'*10
				print (f"\n\033[1;36;41m{texto}\033[m\n\n")
				
				exec (f"exercício{execution_value}()")
				print ("\nRetornando ao menu principal..."); sleep(3)
				print('\033[1A' + '\033[K', end='')
				
		else: 
			print ("\n\nVerifique o valor digitando e tente novamente em 5 segundos")
			sleep(5);return
	except:
		print (format_exc())
	
if __name__ == '__main__':
	while True: 
		contunuar = main()
		if contunuar == False: break