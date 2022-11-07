#ejemplo 1
def main():
    archivo = open('hola.txt', 'w')
    datos = archivo.write('Hola amigos')
    archivo.close()
    print(datos)
    

main()