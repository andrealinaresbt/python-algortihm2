import random
from article import Articulo

class Redactor:
    def __init__(self,nombre,ci):
        self.nombre = nombre
        self.cedula =  ci

    def escribir_articulo(self):
        print("Estoy escribiendo un articulo")
        articulo = Articulo(
            input("Titulo: "),
            input("Cuerpo: "),
            input("Fecha: "),
            input("Resumen: "),
            input("Imagenes: "),
            self.nombre
            )
        print("Termine el articulo",articulo.titulo)
        return articulo

class JefeRedactor(Redactor):
    def __init__(self, nombre, ci,grupo):
        super().__init__(nombre, ci)
        self.grupo_de_redactor = grupo
    
    def supervisar(self):
        print("Todo esta bien con los redactores")

    def decidir(self,articulo):
        if random.random() > 0.5:
            print("El articulo",articulo.titulo,"fue aprobado")
            Articulo.fecha_publicacion = "HOY"
        else:
            print("El articulo",articulo.titulo,"no fue aprobado")

