perguntas = [
    "Telefonou para a vítima? ",
    "Esteve no local do crime? ",
    "Mora perto da vítima? ",
    "Devia para a vítima? ",
    "Já trabalhou com a vítima? ",
]

postivo = sum(map(lambda x: input(x).lower() == "sim", perguntas))

if postivo == 2:
    print("Você é suspeito(a)")
elif 3 <= postivo <= 4:
    print("Você é cúmplice")
else:
    print("Você é assassino")
