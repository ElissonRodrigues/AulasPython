from os import system, name

sequência= ["primeiro", "segundo", "terceiro", "quarto","quinto"]
atleta = []

atleta["nome"]=input("Qual é o seu nome? ").capitalize()
atleta["saltos"]=[]

for x in range(1, 6):
    system('cls' if name == 'nt' else 'clear')
    
    if not atleta.get('nome'): break
    salto = float(input(f"Qual a distância do {x}º Salto: "))
    atleta["saltos"].append(salto)

if atleta.get('nome'):
    system('cls' if name == 'nt' else 'clear')
    print (f"Atleta: {atleta['nome']}")
    print ("\n".join(map(lambda enu: f'{sequência[enu[0]]} salto: {enu[1]} m', enumerate(atleta["saltos"]))))
    
    print (f"\n\nResultado:")
    print (f"Saltos: {' - '.join([str(x) for x in atleta['saltos']])}")
    print (f"Média dos saltos: {sum(atleta['saltos'])/len(atleta['saltos']):.2f} metros")
else:
    print ("\n\nSEM DADOS")

    
    
    
    
    