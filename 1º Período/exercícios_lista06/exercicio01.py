import pandas as pd


while True:
    try:
        mt = int(input('Digite a matricula: '))
        if mt == 0:
            break
    
        df = pd.read_csv('dados_alunos.csv', sep=';')
    
        query = df.query(f"matricula=='{mt}'").index
    
        if query.empty:
            print('Aluno não encontrado')
        else:
            print(f'''
            HISTORICO DO ALUNO 
        
            Nome: {df.nome[query[0]]}
            Matrícula: {df.matricula[query[0]]}
            Curso: {df.curso[query[0]]}
            Campus: {df.campus[query[0]]}
            Situação: {df.situacao[query[0]]}
        
            '''.replace('        ', ''))
    except ValueError:
        print ('\n\nO valor digitado é inválido! Tente novamente.')

# 20092114080403
