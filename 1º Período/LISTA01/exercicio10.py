tamanho = float(input("Qual o tamanho em MBs: "))
velocidade = float(input("Qual a velocidade Mbps: "))

resultado = tamanho/(velocidade*60)

print (f"Tempo para download: {round(resultado)} minutos")