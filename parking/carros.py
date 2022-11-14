from automovil import Automovil
class Car(Automovil):
    def __init__(self, placa, marca, puesto, horaEn, horaSa, minusvalido):
        super().__init__(placa, marca, puesto, horaEn, horaSa)
        self.minusvalido = minusvalido
    def mostrar(self):
        print (f'''Placa ---> {self.placa}
Marca ---> {self.marca}
Puesto ---> {self.puesto}
horaEn ---> {self.horaEn}
horaSa ---> {self.horaSa}''')

        if self.minusvalido == False:
            print('Minusvalido ---> No es minusvalido')
        else:
            print("Es minusvalido")
        print('')

    def salida(self, horaSalida):
        self.puesto = 'This is empty'
        print(f'''Placa ---> {self.placa}
Marca ---> {self.marca}
Puesto ---> {self.puesto}
Hora de Entrada ---> {self.horaEn}
Hora de Salinda ---> {horaSalida}
''')

    
