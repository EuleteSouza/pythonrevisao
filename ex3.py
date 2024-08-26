# programação orientada a objetos

"""
Programação Orientada a Objetos
- Flask e Django

Programação Estruturada com OO
-Flet

Programação Funcional
-Lambda
- cientistas, matematicos, estatisticos, etc...


"""

class Aluno():
    def __init__(self,ch,faltas):
        self.ch = ch
        self.faltas = faltas

    def calcular_faltas(self):
        percent_ch = self.ch * (25/100)
        msg = ''
        if self.faltas > percent_ch:
            msg = 'retido'
        else:
            msg = 'não retido'

        return f"faltas-hs permitidas: {percent_ch} você faltou: {self.faltas} horas, resultado: {msg} por faltas"
                
    
    