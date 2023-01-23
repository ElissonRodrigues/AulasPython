produtos = {

100: {"nome": "Cachorro quente", "preço":  1.20},
101: {"nome": "Bauru simples", "preço":  1.30},
102: {"nome": "Bauru com ovo", "preço":  1.50},
103: {"nome": "Hambúrguer", "preço":  1.20},
104: {"nome": "Cheeseburguer", "preço":  1.30},
105: {"nome": "Refrigerante", "preço":  1.00}

}

total = 0
comprados = []

while True:
	try:
		código = int(input("Digite o código do produto: "))
		
		if código == 0:
			break
		elif not código in list(produtos.keys()): 
			print ("\nCódigo inválido! Tente novamente\n")
		else: 
			quantidade = int(input("Digite a quantidade de produto: "))
			produtos[código]["quantidade"]=quantidade
			comprados.append(produtos[código])
			total += produtos[código]["preço"] * quantidade
	except:
		print ("Parece que você digitou algo errado, tente novamente")

print ("\n\n")
print ("========= CUPOM FISCAL =========")
print ()
print ("\n".join(map(lambda produto: f"{produto['quantidade']} {produto['nome']} - R$ {produto['preço']}", comprados)))
print ("\n")
print (f"Total do pedido: R$ {round(total, 2)}\n\n")
