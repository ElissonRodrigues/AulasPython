from traceback import format_exc

def questions():
	try:
		invalid_text = '\n\033[1;31mNumero é maior que dez, tente novamente\033[m'
		
		n1 = float(input('\n\ndigite a primeira nota: '))
		if n1 > 10 : print (invalid_text); return
		n2 = float(input('\n\ndigite a segunda: '))
		if n2 > 10 : print (invalid_text); return
		n3 = float(input('\n\ndigite a terceira: '))
		if n3 > 10 : print (invalid_text); return
		n4 = float(input('\n\ndigite a quarta: '))
		if n4 > 10 : print (invalid_text); return
		faltas = int(input('\n\nQual o numero de faltas: '))
		return (n1, n2, n3, n4, faltas)
	except ValueError:
		print ('\n\n\033[1;31mOops, parece que você não digito a nota. Digite a nota para continuar\033[m');return
	except:
		print (format_exc())

while True:
	response = questions() 
	if response: n1, n2, n3, n4, faltas = response;break 

if 0 <= faltas <= 60: 
    media = (2*n1+2*n2+3*n3+3*n4)/10
    
    print (f'\n\nSua média é {media}, e você possui {faltas} Faltas\n\n')
    
    if 9 <= media <= 10: 
        print ('\n\n\033[32mVocê está aprovado com louvor\033[32m\n\n')
    elif 7 <= media <= 9:
        print ("\033[32mVocê está aprovado\033[32m\n\n")
    elif 3 <= media < 7: 
        print ('\033[31mVocê está em recuperação\033[m\n\n')

else: 
    print ('\n033Você está reprovado por faltas\033[m\n\n')
