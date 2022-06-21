

class Data:
    
    def __init__(self, dia, mes, ano):
        self.dia = dia
        self.mes = mes
        self.ano = ano
    
    def formatada(self):
        if self.dia < 10 and self.mes <10:
            print(f'0{self.dia}/0{self.mes}/{self.ano}')
        elif self.dia < 10 and self.mes >=10:
            print(f'0{self.dia}/{self.mes}/{self.ano}')
        elif self.dia >=10 and self.mes <10:
            print(f'{self.dia}/0{self.mes}/{self.ano}')
        else:
            print(f'{self.dia}/{self.mes}/{self.ano}')
