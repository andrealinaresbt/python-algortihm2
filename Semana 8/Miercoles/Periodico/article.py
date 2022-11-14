class Articulo:
    def __init__(self,titulo,cuerpo,fecha,resumen,imagenes,redactor):
        self.titulo = titulo
        self.cuerpo = cuerpo
        self.fecha_publicacion = None
        self.fecha_creacion = fecha
        self.resumen = resumen
        self.imagenes = imagenes
        self.redactor = redactor