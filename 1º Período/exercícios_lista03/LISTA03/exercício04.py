from os import system, name

def exercício04():

    n = int(input("Sequência: "))
    
    e1 = 0
    e2 = 1
    
    system('cls' if name == 'nt' else 'clear')
    print ("\n\nRESULTADOS DO EXERCÍCIO 4")
    print ("="*50)
    print (f"| {e1} | {e2} | ", end="")
    
    for x in range(n-2):
        e3 = e1 + e2
        e1 = e2
        e2 = e3
    
        print (f"{e3} | ", end="")
     
    print ("")
    print ("="*50)