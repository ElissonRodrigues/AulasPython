from re import sub

texto = input("digite um texto qualquer: ").lower()
texto = sub("[!'?,:;@%&#.]", "", texto).split() # Tratamento da string

for x in set(texto):
    quantidade = texto.count(x)
    print(f'A Palavra "{x}" aparece {quantidade} {"vez" if quantidade <= 1 else "vezes"}')
    