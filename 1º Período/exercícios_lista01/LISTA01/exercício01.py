import os

#1. Faça um programa para calcular as seguintes expressões aritméticas (tente também calculá-las na mão para verificar a importância da precedência dos operadores):
#
# a) 10 + 20 x 30 (reescrever com sintaxe Python);
# b) 4²  ÷ 30 (reescrever com sintaxe Python);
# c) (9⁴ + 2) x 6 – 1 (reescrever com sintaxe Python);
# d) 10 % 3 * 10 ** 2 + 1 – 10 * 4 / 2 (já está na sintaxe Python).

def exercício01():
	os.system('cls' if os.name == 'nt' else 'clear')
	
	print ("\n\nRESULTADOS DO EXERCÍCIO 1")
	print ("="*50)
	print(f"""
    A) 10 + 20 x 30 = {10 + 20 * 30}
    B) 4² ÷ 30 = {4**2 / 30}
    C) (9² + 2) x 6 - 1 = {(9**2 + 2) * 6 - 1}
    D) 10 % 3 x10² + 1 - 10 x 4 % 2 = {10 % 3 * 10 ** 2 + 1 - 10 * 4 / 2}
	""".replace("    ", "")
	)
	print ("="*50)