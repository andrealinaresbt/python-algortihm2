from bebida import Bebida
class Refresco (Bebida):
    def __init__(self, nombre, marca, disponible, azucar, sabor):
        super().__init__(nombre, marca, disponible)
        self.azucar = azucar
        self.sabor = sabor
    def mostrar(self):
         print (f''' ----REFRESCO ----
Nombre ---> {self.nombre}
Marca ---> {self.marca}
Disponible ---> {self.disponible}
Azucar ---> {self.azucar}
Sabor ---> {self.sabor}
''')
    
    def name(self):
        return super().name()