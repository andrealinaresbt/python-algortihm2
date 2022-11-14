#print(type(8))
#Para definir una clase, se pone Class y el nombre con la 1era letra en mayuscula (Convenio)
class Perro():
    def __init__(self, raza, color, edad, escala):  
        self.raza = raza
        self.color = color
        self.__edad = edad
        self.escala = escala
    """
Se define el constructor arriba, es el que define los atributos de la clase, 
los crea automaticamente al crear 
un objeto

"""
    def informacion(self):
        return(f'''Este Perro tiene las siguientes caracteristicas:
Raza: {self.raza} -- Color: {self.color} -- Edad: {self.__edad} annos y el perro es {self.escala}''')


buldog = Perro('Buldog', 'Marron', 7, 'Grande')
a = buldog.informacion()

#En b se cambia un atributo

buldog.escala = 'mediano'
b = buldog.informacion()
print(b)

#Debido a que edad esta privado, no se puede alterar fuera de la clase

# buldog.__edad = 9
# print(buldog.informacion())


#Encapsulamiento: indica que tan accesible es modificar los atributos de una clase.      
#En algoritmos, se usan atributos y metodos publicos y privado

#Con control k control c, comentas todo lo seleccionado

#Herencia: 

#Modulos: archivos externos de python que los usas en otro archivo

"""
3 formas de importar un archivo o lo necesario del archivo:

Se importa el archivo Pruebas y se utiliza la funcion sumar de dicho archivo python

1. import Pruebas 
print(Pruebas.sumar(4,8))

Se importa el archivo Pruebas, se denota como j y se utiliza mas adelante como j

2. import Pruebas as j
print(j.resta(4,8))

Se importa solamente la funcion multiplicar del archivo Pruebas

3. from Pruebas import multiplicar
print(multiplicar(4,8))

"""

