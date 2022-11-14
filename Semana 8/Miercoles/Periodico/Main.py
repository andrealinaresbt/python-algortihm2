from redactor import Redactor, JefeRedactor
from seccion import Seccion

def get_redactores_deportes():
    return [
    Redactor("Pedro", 37483929),
    Redactor("Maria", 37483929),
    Redactor("Jose", 37483929),
    Redactor("Juan", 85093828)]

def get_redactores_farandula():
    return [
    Redactor("Ana", 37483929),
    Redactor("Landaeta", 37483929),
    Redactor("Andrea", 37483929),
    Redactor("Sebastian", 85093828)]
    
def get_redactores_entretenimiento():
    return [
    Redactor("Messi", 37483929),
    Redactor("Andres", 37483929),
    Redactor("Erika", 37483929),
    Redactor("Julia", 85093828)]

def procesar_articulo(Seccion):
    for escritor in Seccion.jefe_redactor.grupo_de_redactor:
        print("El escritor al mando en este momento es",escritor.nombre)
        articulo = escritor.escribir_articulo()
        print("El jefe que va a decidir es",Seccion.jefe_redactor.nombre)
        Seccion.jefe_redactor.decidir(articulo)
      

def main():
    
    #Jefes
    jefe_entretenimiento = JefeRedactor("Jose Quevedo", 12345, get_redactores_entretenimiento())
    jefe_deporte = JefeRedactor("Fabiana Pettruci", 12345, get_redactores_deportes())
    jefe_farandula = JefeRedactor("Javier Bouquett", 12345, get_redactores_farandula())

    #Seccion
    seccion_entretenimiento = Seccion("Entretenimiento", jefe_entretenimiento)
    seccion_deportes = Seccion("Deportes", jefe_deporte)
    seccion_farandula = Seccion("Farandula", jefe_farandula)

    procesar_articulo(seccion_entretenimiento)
    procesar_articulo(seccion_farandula)
    procesar_articulo(seccion_deportes)
    print('hello')
main()