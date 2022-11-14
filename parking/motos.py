from automovil import Automovil
class Bike(Automovil):
    def __init__(self, placa, marca, puesto, horaEn, horaSa):
        super().__init__(placa, marca, puesto, horaEn, horaSa)

    def mostrar(self):
        return super().mostrar()
    def salida(self):
        self.puesto = 'This is empty'
        return(f'''Placa ---> {self.placa}
Marca ---> {self.marca}
Puesto ---> {self.puesto}
Hora de Entrada ---> {self.horaEn}
Hora de Salinda ---> {self.horaSa}
''')
