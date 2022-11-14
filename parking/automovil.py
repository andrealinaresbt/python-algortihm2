class Automovil():
   
    def __init__(self, placa, marca, puesto, horaEn, horaSa):
        self.placa = placa
        self.marca = marca
        self.puesto = puesto
        self.horaEn = horaEn
        self.horaSa = horaSa

    def mostrar(self):
        print(f'''Placa ---> {self.placa}
Marca ---> {self.marca}

horaEn ---> {self.horaEn}
horaSa ---> {self.horaSa}''')
        if self.puesto == None:
            print("None")
        else:
            print(f'Puesto ---> {self.puesto}')

    def salida(self, horaSalida):
        self.puesto = 'this is empty'
        return(f'''Placa ---> {self.placa}
Marca ---> {self.marca}
Puesto ---> {self.puesto}
Hora de Entrada ---> {self.horaEn}
Hora de Salinda ---> {horaSalida}
''')

        






