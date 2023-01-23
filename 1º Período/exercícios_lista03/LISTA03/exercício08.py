from time import sleep
from os import system, name

def exercício08():
    altura = int(input("Qual a altura  do retângulo: "))
    largura = int(input("Qual a largura: "))
    print ("\n")
    
    system('cls' if name == 'nt' else 'clear')
    print ("\n\nRESULTADOS DO EXERCÍCIO 8")
    print ("="*50)
    
    caractere  = "* "
    
    print (caractere*largura)
    for x in range(1, altura-1): print (caractere.ljust((largura*2)-2) + caractere)
    print (caractere*largura)
    
    #easter egg 
    
    if altura == 19 and largura == 5:
        #19/05 = Aniversário 
        altura = 16
        largura = 20
        print ("\n\n")
        print (caractere*largura)
        for x in range(1, altura-1): 
            if x >= 3 and x < altura-4:
                parte_e = round((largura-7)/2 - 2)
                if x == 3: print (caractere.ljust(largura-4) + "* " + "* "*parte_e + caractere.rjust(largura-parte_e-2))
                if x == (altura - 9): print (caractere.ljust(largura-5) + "* " + "* "*parte_e + caractere.rjust(largura-parte_e-1))
                else: print (caractere.ljust(round((largura/2) + 5)) + "* " + caractere.rjust(largura+3))
            elif x == altura - 4: print (caractere.ljust(largura-4) + "* " + "* "*parte_e + caractere.rjust(largura-parte_e-2)) #Ponta inferior do é
            else: print (caractere.ljust((largura*2)-2) + caractere) # Cantos das quinas Inferiores e Superiores
        print (caractere*largura)
    
        h_string = '456973736f6e20526f64726967756573'
        print ("\n")
        
        letra_a_letra = ""
        caixa = bytes.fromhex('3d').decode()
        n = 0
        for x in bytes.fromhex(h_string).decode():
            letra_a_letra += x
            n += 2
            print (caixa*n +"\n"+ letra_a_letra.center(37))
            print('\033[1A' + '\033[K', end='')
            print('\033[1A' + '\033[K', end='')
            sleep(0.20)
        
        print(caixa*39)
        print (letra_a_letra.center(37))
        
        h_string = '4f6272696761646f2070656c61732064696361732070726f666573736f7221'
        
        letra_a_letra= ""
        n = 0
        for x in bytes.fromhex(h_string).decode():
            n+=1
            letra_a_letra += x
            print (letra_a_letra.center(37)+"\n"+caixa*n)
            print('\033[1A' + '\033[K', end='')
            print('\033[1A' + '\033[K', end='')
            sleep(0.20)
            
        
        print (letra_a_letra.center(37))
        print (caixa*39)
        
        print ("\n\n")
        print ("="*50)
        