paes = int(input("Digite o total de pães: ")
envelhecidos = int(input("Dos {paes}, quantos são envelhecidos"))

unidade = 0.25 
total_sem_desconto = paes * unidade
preco_paes_envelhecidos = envelhecidos * 0.5
preco_paes_novos = (paes - envelhecidos) * unidade
preco_total_com_desconto = preco_paes_envelhecidos + preco_paes_novos

print (f"Preço total sem desconto: R$ {total_sem_desconto}")
