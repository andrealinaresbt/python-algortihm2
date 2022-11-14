#nombre apellido cedula
#profesor clases que da cuantas materias
#cuantas clases ve y carnet
#imprimr datos del profesor y estudiante

class Persona():
    def __init__(self, nombre, apellido, cedula):
        self.nombre = nombre
        self.apellido = apellido
        self.cedula = cedula

    def informacion(self):
        print(f'''Nombre: {self.nombre}
Apellido: {self.apellido} 
Cedula: {self.cedula}''')

a = Persona('Andrea', 'linares', 3049304934)
a.informacion()

class Profesor(Persona):
    def __init__(self, nombre, apellido, cedula, clasesDadas, cantidadMateria):
        super().__init__(nombre, apellido, cedula)
        self.clasesDadas = clasesDadas
        self.cantidadMateria = cantidadMateria

    def informacionProfe(self):
        return(f'''Clases dadas: {self.clasesDadas}
Cantidad de materias: {self.cantidadMateria} 
''')

def datosProfe():
    name = input('Ingrese el nombre de la persona: ')
    while name.isalpha() == False:
        name = input('Ingrese un nombre valido: ')

    apellido = input('Ingrese el apellido de la persona: ')
    while apellido.isalpha() == False:
        apellido = input('Ingrese un apellido valido: ')

    cedula = input('Ingrese la cedula de la persona: ')
    while cedula.isnumeric() == False:
        cedula = input('Ingrese una cedula valida: ')
    
    claseDada = input('Ingrese las clases que da de la persona: ')
    while claseDada.isalpha() == False:
       claseDada = input('Ingrese clases validas: ')

    cantidadMateria = input('Ingrese las cantidad de clases que da de la persona: ')
    while cantidadMateria.isnumeric() == False:
       cantidadMateria = input('Ingrese una cantidad valida: ')


    x = Profesor(name, apellido, cedula, claseDada, cantidadMateria)
    print(x.informacion())
    print(x.informacionProfe())



datosProfe()



