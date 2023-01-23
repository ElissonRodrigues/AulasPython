from os import system, name

def exercício06():
    compras = []
    n = 0
    
    while 15 > n:
        n += 1
        system('cls' if name == 'nt' else 'clear')
        transação =  float(input(f"Qual o valor da {n}ª transição: "))
        tipo = input("\n\nQual o Tipo de transição:\n\nV = À visa\nP = A prazo\n\n>>> ").upper()
        
        if tipo in ("P", "V"): compras.append({"valor": transação, "tipo": tipo})
        else: print ('Tipo inválido! O tipo de transição deve ser: "P" ou "V". Tente novamente\n\n'); n-=1
    
    menor = 0
    maior = 0
    total_avista = 0
    total_aprazo = 0
    
    for transação in compras:
        if transação["tipo"] == "V": total_avista += transação["valor"]
        if transação["tipo"] == "P": total_aprazo += transação["valor"]
        
        if menor == 0: menor = transação["valor"] 
        
        if transação["valor"] < menor: menor = transação["valor"]
        if transação["valor"] > maior: maior = transação["valor"]
    
    system('cls' if name == 'nt' else 'clear')
    
    print ("\n\nRESULTADOS DO EXERCÍCIO 6")
    print ("="*50)
    print (f"""
    EXTRATO DA TRANSAÇÃO
    
    Valor total de pagamentos à vista: R${total_avista}
    Valor total de pagamentos a prazo: R${total_aprazo}
    Transação de menor valor: R${menor}
    Transação de maior valor: R${maior}
    
    TOTAL DAS TRANSAÇÕES: R${total_avista + total_aprazo:.2f}
    """.replace("    ", "")
    )
    print ("="*50)
    
    