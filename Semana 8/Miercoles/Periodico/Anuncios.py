class AnuncioComercial:
    def __init__(self,imagen,seccion):
        self.seccion = seccion
        self.imagen = imagen


class AnuncioClasificados:
    def __init__(self,precio,fecha_publicacion,dias,tipo):
        self.precio = precio
        self.fecha_de_publicacion = fecha_publicacion
        self.cantidad_de_dias = dias
        self.tipo = tipo

class AnuncioVehiculo(AnuncioClasificados):
    def __init__(self, precio, fecha_publicacion, dias, marca, modelo, año):
        super().__init__(precio, fecha_publicacion, dias, "Vehiculo")
        self.marca = marca 
        self.modelo = modelo
        self.año = año

class AnuncioVivienda(AnuncioClasificados):
    def __init__(self, precio, fecha_publicacion, dias,m2,cuartos,baños,puestos,politicas):
        super().__init__(precio, fecha_publicacion, dias, "Vivienda")
        self.m2 = m2
        self.cuartos = cuartos
        self.baños = baños
        self.puestos = puestos
        self.acepta_politica = politicas