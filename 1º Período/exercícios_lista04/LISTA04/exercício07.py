alunos = []
aprovados = ""
reprovados = ""
recuperação = ""

tamanho = int(input("Quantos alunos você pretende adição ao sistema? "))

for x in range(1, tamanho+1):
  a = input(f"\nDigite o nome do {x}º aluno(a): ")
  alunos.append({"nome": a, "notas": []})
  
  y = 0
  while y < 4:
    y += 1
    n = float(input(f"Qual foi a {y}º nota de {a.upper()}? "))
    
    if 0 <= n <= 10:
      alunos[len(alunos)-1]['notas'].append(n)
    else:
      print ("\n\nNota inválida! Digite uma nota entre 0 e 10.\n\n")
      y -= 1

print ("")
print ("="*30)
print ("BOLETIM DOS ALUNOS")
print ("="*30)
for aluno in alunos:
  media = sum(aluno["notas"])/len(aluno["notas"])
  
  if media >= 7:
    situação = "Aprovado"
    aprovados += f"{aluno['nome']}\n"
  elif 3 <= media <= 7:
    situação = "Recuperação"
    recuperação += f"{aluno['nome']}\n"
  else: 
    situação = "Reprovado"
    reprovados += f"{aluno['nome']}\n"
    
  print (f"""
ALUNOS(A): {aluno["nome"]}
NOTAS: {' , '.join([str(x) for x in aluno['notas']])}
MÉDIA: {media}
SITUAÇÃO: {situação}\n
""")
print ("="*30)

print (f"""
ALUNOS APROVADOS:

{aprovados if aprovados else 'Nenhum aluno foi aprovado'}

ALUNOS EM RECUPERAÇÃO:

{recuperação if recuperação else 'Nenhum aluno em recuperação'}

ALUNOS REPROVADOS:

{reprovados if reprovados else 'Nenhum aluno foi reprovado'}
""")
print ("="*30)
