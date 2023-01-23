from os import system, name

def exercício05():
    faixa1, faixa2, faixa3, faixa4,  faixa5 = 0, 0, 0, 0, 0

    for x in range(1, 15+1):
        x = int(input(f"Qual a idade da {x}ª pessoa: "))
        
        if x <= 15: faixa1 += 1
        elif 16 <= x <= 30: faixa2 += 1
        elif 31 <= x <= 45: faixa3 += 1
        elif 46 <= x <= 60: faixa4 += 1
        else: faixa5 += 1
    
    system('cls' if name == 'nt' else 'clear')
    print ("\n\nRESULTADOS DO EXERCÍCIO 5")
    print ("="*50)
    print (f"Faixas etárias:\n\nPrimeira faixa: {faixa1}\nSegunda Faixa: {faixa2}\nTerceira faixa: {faixa3}\nQuarta faixa: {faixa4}\nQuinta Faixa: {faixa5}")
    print ("="*50)
    