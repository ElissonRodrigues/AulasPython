sa = float(input("Quanto você ganha por hora trabalhada?: "))
ho = float(input("Quantas horas você trabalhou?: "))

print(f'Você trabalhou por {ho} {"horas" if ho > 1 else "hora"}, portanto seu salário será de R$ {round(sa*ho)}')
