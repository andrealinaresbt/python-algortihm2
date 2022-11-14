class Bebida:
    almacen_actualizado= []
    
    def __init__(self, nombre, marca, disponible):
        self.nombre = nombre
        self.marca = marca
        self.disponible = disponible

    def mostrar(self):
        print (f'''Nombre ---> {self.nombre}
Marca ---> {self.marca}
Disponible ---> {self.disponible}
''')
    def noDisponible(self):
        self.disponible = False


