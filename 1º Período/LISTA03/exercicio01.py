perguntas = {
    "Nome: ": "len('{}')  > 3",
    "Idade: ": "0 <= int('{}') <= 150",
    "Salário: ": "{} > 0",
    "Sexo: ": "'{}'.lower() in ['m', 'f']",
    "Estado Civil: ": "'{}'.lower() in ['s', 'c', 'v', 'd']",
}

warning = [
    "o nome deve ter mais que 3 caracteres",
    "a Idade deve está entre 0 e 150 anos",
    "o salário deve ser maior que 0",
    "o sexo deve ser: m ou f",
    "o estado civil deve ser: s, c, v ou d",
]

count = 0

while True:
    if len(list(perguntas.keys())) == 0:
        break

    key = list(perguntas.keys())[0]
    value = perguntas[key]

    resp = input(key)

    if eval(value.format(resp)):
        perguntas.pop(key)
        count += 1
    else:
        print(f"\nOops, {warning[count]}\n")
