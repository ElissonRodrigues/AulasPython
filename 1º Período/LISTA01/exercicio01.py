from time import sleep

l = 0
notas = []
while l < 4:
    try:
        l += 1
        n = float(input(f'Qual a nota do {l}º bimestre: '))
        if not 0 <= n <= 10: l -= 1; raise ValueError
        notas.append(n)
    except:
        print('Oops, você não informou a nota correta, tente novamente.')
        print ()
        n -= 1
        sleep(2)

media = sum(notas)/len(notas)
print (f'Sua média é {round(media)}')