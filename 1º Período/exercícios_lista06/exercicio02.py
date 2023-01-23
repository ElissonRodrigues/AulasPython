import pandas as pd
from unidecode import unidecode

while True:

    disciplina = input('Digite a disciplina de ingresso: ').lower()
    if disciplina.lower() == "sair":
        break
    campus = input('Digite a Sigla do campus. EX: SC: ').upper()

    df = pd.read_csv('dados_servidores.csv', sep=';')
    query = df.query(f'campus=="{campus}" and categoria=="docente"').index

    if query.empty:
        print("SEM RESULTADOS PARA SUA BUSCA")
    else:
        empty = True
        print("\n\n")

        for ps in query:
            if unidecode(df.disciplina_ingresso[ps].lower()) == unidecode(disciplina):
                print("="*25)
                print(
                    f"\nProfessor(a): {df.nome[ps]}\nMatrícula: {df.matricula[ps]}\n")
                empty = False

        if empty:
            print(f'SEM RESULTADOS PARA SUA BUSCA')
        else:
            print("="*25)

        print()
