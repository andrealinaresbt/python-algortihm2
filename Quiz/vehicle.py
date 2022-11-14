class Vehicle():
    vehiculo = []
    def __init__(self, placa, marca, puesto, horaEn, horaSalida):
      
        self.marca = marca
        self.placa = placa
        self.puesto = puesto
        self.horaEn = horaEn
        self.horaSalida = horaSalida

    def informacion(self):
        return (f'''Placa ---> {self.placa}
Marca ---> {self.marca}
Puesto ---> {self.puesto}
Hora de Entrada ---> {self.horaEn}
Hora de Salinda ---> {self.horaSalida}
''')

    def salida(self):
        self.puesto = None
        print (f'''Placa ---> {self.placa}
Marca ---> {self.marca}
Puesto ---> {self.puesto}
Hora de Entrada ---> {self.horaEn}
Hora de Salinda ---> {self.horaSalida}
''')



    


class Automovil(Vehicle):
    def __init__(self, placa, marca, puesto, horaEn, horaSalida, minusvalido):
        super().__init__(placa, marca, puesto, horaEn, horaSalida)
        self.minusvalido = minusvalido
  
    def informacion(self):
        return (f'''Placa ---> {self.placa}
Marca ---> {self.marca}
Puesto ---> {self.puesto}
Hora de Entrada ---> {self.horaEn}
Hora de Salinda ---> {self.horaSalida}
Minusvalido ----> {self.minusvalido}
''')
        

        


class Bike(Vehicle):
    def __init__(self, placa, marca, puesto, horaEn, horaSalida):
       super().__init__( placa, marca, puesto, horaEn, horaSalida)

    def salida(self):
        self.puesto = None
        print (f'''Placa ---> {self.placa}
Marca ---> {self.marca}
Puesto ---> {self.puesto}
Hora de Entrada ---> {self.horaEn}
Hora de Salinda ---> {self.horaSalida}
''')
