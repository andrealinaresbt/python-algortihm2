class AnunciosComercial:
    def __init__(self, imagen, seccion):
        self.imagen = imagen
        self.seccion = seccion

class AnuncioClasificado:
    def __init__(self, precio, fechaPUB, cantidad_dias, tipo):
        self.precio = precio
        self.fechaPUB = fechaPUB
        self.cantidad_dias = cantidad_dias
        self.tipo = tipo

class AnuncioVehiculo(AnuncioClasificado):
    def __init__(self, precio, fechaPUB, cantidad_dias, marca, modelo, ano):
        super().__init__(precio, fechaPUB, cantidad_dias, "Vehiculo")
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        
class AnuncioVivienda(AnuncioClasificado):
    def __init__(self, precio, fechaPUB, cantidad_dias, metros, cuartos, banos, puestos, politicas):
        super().__init__(precio, fechaPUB, cantidad_dias, "Vivienda")
        self.metros = metros
        self.cuartos = cuartos
        self.banos = banos
        self.puestos = puestos
        self.acepta_politicas = politicas
        
