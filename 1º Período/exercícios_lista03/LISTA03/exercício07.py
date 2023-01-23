from os import system, name

def exercício07():
    total = 0
    p = 0
    
    while True:
        p += 1
        codigo = int(input(f"Qual o código do {p}º produto: "))
        if codigo== 0: break
        
        if not codigo in (1, 2, 3, 5, 9):
            print ("\nCódigo inválido. Digite o código novamente\n")
            p -=1
        else:
            quantidade = int(input("\nQual a quantidade de produtos: "))
            
            if codigo == 1:
                total += quantidade*0.50
            elif codigo == 2:
                total += quantidade*1.00
            elif codigo == 3:
                total += quantidade*4.00
            elif codigo == 5:
                total += quantidade*7.00
            elif codigo == 9:
                total += quantidade*8.00
    
    system('cls' if name == 'nt' else 'clear')
    print ("\n\nRESULTADOS DO EXERCÍCIO 7")
    print ("="*50)
    print (f"TOTAL A PAGAR: R${total}")
    print ("="*50)
        
        
