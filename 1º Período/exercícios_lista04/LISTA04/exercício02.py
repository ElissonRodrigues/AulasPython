lista_alunos = {}
n = 0

while True:
    n+=1 
    try:
        nome = input(f'Qual o nome do {n}º aluno(a): ')
        if nome.lower() == 'sair': break

        media = int(input(f'Qual a média do {n}º aluno(a): '))

        if 0 <= media <= 9:
            lista_alunos[nome]=media
        else:
            print ('Media invalida! Tente novamente')
            n-=1
    except ValueError:
        print ('Oops, parece que você digitou algo errado, tente novamente\n\n')
        n-=1
        
print ('='*25)
print (lista_alunos)

for aluno, media in lista_alunos.items():
    if media < 2:
        print (f'{aluno.upper()}\nMédia: {media}\nStatus: Reprovado\n')
    elif 2 <= media < 6: 
        print (f'{aluno.upper()}\nMédia: {media}\nStatus: Recuperação\n')
    else:
        print (f'{aluno.upper()}\nMédia: {media}\nStatus: Aprovado\n')
print ('='*25)