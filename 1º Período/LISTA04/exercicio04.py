class MesExtenso:
    def __init__(self, DD, MM, YYYY) -> int:
        self.day = DD
        self.month = MM
        self.year = YYYY

    def formatar(self):
        month_name = {
            1: 'janeiro',
            2: 'fevereiro',
            3: 'março',
            4: 'abril',
            5: 'maio',
            6: 'junho',
            7: 'julho',
            8: 'agosto',
            9: 'setembro',
            10: 'outubro',
            11: 'novembro',
            12: 'dezembro'        
        }
        numérica = f'{self.day:02d}/{self.month:02d}/{self.year:04d}'
        escrito = f'{str(self.day)} de {month_name[self.month]} de {str(self.year)}'
        return numérica + ' - ' + escrito

data = [int(x) for x in input("Digite uma data qualquer no seguinte formato: DD/MM/AAAA (19/09/2021) => ").split("/")]

novo_formato = MesExtenso(data[0], data[1], data[2]).formatar()
print ()
print (novo_formato)