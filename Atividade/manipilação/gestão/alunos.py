import pandas as pd
from os import system, name
from time import sleep
from pandas.errors import EmptyDataError

class Alunos:
    def __init__(self):
        self.db_path = 'dados_alunos.csv'
        #self.db_path = 'database.csv'

    def cadastrar(self,**kargs):
        
        data = {
            "nome": [kargs.get("nome")],
            "matricula": [kargs.get("matricula")],
            "notas": [{"nota1": kargs.get("notas")[0], "nota2": kargs.get("notas")[1], "nota3": kargs.get("notas")[2], "nota4": kargs.get("notas")[3]}],
            "curso": [kargs.get("curso")]
       }
            
        try:
            df1 = pd.read_csv(self.db_path)
            
            if df1.query(f"matricula=={str(kargs.get('matricula'))}").index.empty:
                df2 = pd.concat([df1, pd.DataFrame(data)])
                df2.to_csv(self.db_path, index=False)
                print (f'{kargs.get("nome")} foi cadastrado! ')
                sleep(4)
            else:
                print (f'{kargs.get("nome")} já está cadastrado')
        
        except EmptyDataError:
            
            df = pd.DataFrame(data)
            df.to_csv(self.db_path, index=False)
            print (f'{kargs.get("nome")} foi cadastrado! ')
    
    def relatório(self):
        try:
            df = pd.read_csv(self.db_path)
            
            #print ("="*30)
            print ("RELATÓRIOS DOS ALUNOS")
            #print ("="*30)
            
            for x in df.values:
                nota = eval(x[2])
                
                def calc_média():
                    média = (nota['nota1']+nota['nota2']+nota['nota3']+nota['nota4'])/4
                    if média >= 7:
                        return (média, 'Aprovado')
                    elif 3 <= média <= 7:
                        return  (média, 'Recuperação')
                    else: 
                        return (média, 'Reprovado')
                
                situação = calc_média()
                
                print (f"""
                Nome: {x[1]} - {x[0]}
                Curso: {x[3]}
                Notas: {nota['nota1']}, {nota['nota2']}, {nota['nota3']}, {nota['nota4']}
                Situação: {situação[0]:.2f} - {situação[1]}
                """.replace("                ", ""))
                print ("="*30)
                
            sleep(4)
            
        except:
            print ("Ocorreu um erro, tente novamente")
        
        
        
        
            