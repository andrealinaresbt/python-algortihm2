import random
from Articulo import Articulo

class Redactor:
    def __init__(self, nombre, ID):
        self.nombre = nombre
        self.ID = ID
        #self.seccion = seccion #como esto puede ser una clase, lo que le mando es un objeto.
        #no corre porque para seccion necesito un grupo de redactor
    def escribir(self):
        print('Estoy escribiendo un articulo')
        article = Articulo(
            input("Title: "), input("Cuerpo: "), input("Fecha: "), input("Resumen: "), input("Imagen: "), input("Redactor: "), self.nombre)
        print('Termine el articulo', article.titulo)
        return article
        
class JefeRedactor(Redactor): #hereda los metodos y atributos pero puede que no use los metodos
    def __init__(self, nombre, ID, GrupoDeRedactores):
        super().__init__(nombre, ID)
        self.GrupoDeRedactores = GrupoDeRedactores

    def supervisar(self): #si esta dentro de una clase hay que agregar el self.
        print("Todo esta bien con los redactores")

    def decidir(self, articulo):
        if random.random() > 0.5:
            print("El articulo", articulo, "fue aprobado")
        else:
            print("El  articulo", articulo, "no fue aprobado")

