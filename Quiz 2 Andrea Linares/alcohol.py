from bebida import Bebida

class Alcohol (Bebida):
    def __init__(self, nombre, marca, disponible, grado, tipo):
        super().__init__(nombre, marca, disponible)
        self.grado = grado
        self.tipo = tipo
    def mostrar(self):
         print (f''' ----ALCOHOL----
Nombre ---> {self.nombre}
Marca ---> {self.marca}
Disponible ---> {self.disponible}
Grado ---> {self.grado}
Tipo ---> {self.tipo}
''')
    
    def name(self):
        return super().name()
