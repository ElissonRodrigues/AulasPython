nota1= float(input("Digite a primeira nota: "))
nota2= float(input("Digite a segunda nota: "))
media= nota1+nota2/2

if 0 <= media <= 4:
    resultado = ("E", "REPROVADO" )
elif 4 <= media <= 6:
    resultado = ("D", "REPROVADO" )
elif 6 <= media <= 7.5:
    resultado = ("C", "APROVADO" )
elif 7 <= media <= 9:
    resultado = ("B", "APROVADO" )
else:
    resultado = ("A", "APROVADO COM DISTINÇÃO" )

print (
f""""
NOTAS: {nota1} - {nota2} 
MEDIA: {media}
CONCEITO: {resultado[0]} 
SITUAÇÃO:{resultado[1]}
""")


