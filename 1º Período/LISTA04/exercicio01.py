from os import system, name

notas = []

while True:
    n = float(input('Digite um numero qualquer [use -1 para sair]: '))
    if n == -1: break

    if 0 <= n <= 10: 
        notas.append(n)
        system('cls' if name == 'nt' else 'clear')  
    else:
        system('cls' if name == 'nt' else 'clear')
        print ('\nDigite uma nota entre 0 e 10!\n')
    
media = sum(notas)/len(notas)

print (f'''
1 - Quantidade de valores digitados: {len(notas)}
2 - Valores na ordem em que foram informados: {", ".join([str(x) for x in notas])}
3 - Valores na ordem inversa à que foram informados: {", ".join([str(x) for x in notas[::-1]])}
4 - Média aritmética dos valores: {media:.2f}
5 - Quantidade de valores acima da média: {", ".join([str(x) for x in notas if x > media])}
6 - Quantidade de valores abaixo da média:  {", ".join([str(x) for x in notas if x < media])}
''')
    
