from bebida import Bebida
from refresco import Refresco
from alcohol import Alcohol

def welcome():
    print('----------WELCOME TO EL BODEGON----------')

def viewInventory(almacen_desactualizado):
    for elementos in Bebida.almacen_actualizado:
        elementos.mostrar()
            
def goodbye():
    print('\n Thank you for coming! See you soon <3 (Sergio no me raspes)')

def eliminar(bebidaBorrar):
            bebidaBorrar.noDisponible()
            

def main():
    welcome()
    bebidaGrado= []
    MayorGrado = None
    MenorAzucar =None
    refrescoAzucar =[]

    almacen_desactualizado = {
            "Alcohol":
        [
        	{ "nombre": "Linaje", "marca": "Santa Teresa", "grado": 40, "tipo": "Ron", "disponible": True },
        	{ "nombre": "Black Label 18", "marca": "Jonnie Walker", "grado": 43, "tipo": "Whisky", "disponible": True },
        	{ "nombre": "Solera Verde", "marca": "Polar", "grado": 6, "tipo": "Cerveza", "disponible": True }
        ],
    
        "Refresco":
        [
        	{ "nombre": "Maltin Polar", "marca": "Polar", "azucar": 7, "sabor": "Malta", "disponible": True },
        	{ "nombre": "Pepsi", "marca": "Pepsico", "azucar": 7, "sabor": "Cola", "disponible": True },
        	{ "nombre": "Chinoto", "marca": "The Coca-Cola Company", "azucar": 4, "sabor": "Limon", "disponible": True }
        ] 
}

    for key,value in almacen_desactualizado.items():
        if key == 'Alcohol':
            for caracteristicas in value:
                Bebida.almacen_actualizado.append(Alcohol(caracteristicas['nombre'], caracteristicas['marca'], 
            caracteristicas['disponible'], caracteristicas['grado'], caracteristicas['tipo']))
           
        elif key == 'Refresco':
            for caracteristicas in value:
                Bebida.almacen_actualizado.append(Refresco(caracteristicas['nombre'], caracteristicas['marca'], 
            caracteristicas['disponible'], caracteristicas['azucar'], caracteristicas['sabor']))
            
    while True:
        try:
            option = int(input('Hello, what do you want to do today? \n1. View inventory. \n2. Delete drink from inventory. \n3. Exit. \n4. Bono \n---> '))
            
            if option == 1:
                viewInventory(almacen_desactualizado)

            if option == 2:
                print("This is the index of the available drinks")
                for i in range(len(Bebida.almacen_actualizado)):
                    
                    print(f'{i}:')
                    Bebida.almacen_actualizado[i].mostrar()
                    
                while True:
                    path = int(input("Choose the number of the drink you wish to delete: "))
                    if path in range(len(Bebida.almacen_actualizado)):
                        eliminar(Bebida.almacen_actualizado[path])
                        viewInventory(almacen_desactualizado)
                        break 

                    else:
                        print('This is not an accepted value.')
                            
                        
                

            if option ==3:
                goodbye()
                break

            if option ==4:
                for key,value in almacen_desactualizado.items():
                    if key == 'Alcohol':
                        for values in value:
                            grados =values.get('grado')
                            bebidaGrado.append(grados)
                    
                        for values in bebidaGrado:
                            if bebidaGrado[0] > bebidaGrado[1]:
                                pass
                            elif bebidaGrado[1] < bebidaGrado[2]:
                                pass
                            elif bebidaGrado[1] > bebidaGrado[2]:
                                MayorGrado = bebidaGrado[1]
                                

                            
                                print(f"La bebida de mayor grado es {MayorGrado}")

                    if key == 'Refresco':
                        for values in value:
                            cantidadAzucar =values.get('azcuar')
                            refrescoAzucar.append(grados)
                    
                        for values in refrescoAzucar:
                            
                            if refrescoAzucar[2] < refrescoAzucar[0] and refrescoAzucar[1] < refrescoAzucar[0]:
                                MenorAzucar = refrescoAzucar[2]
                                

                            
                                print(f"El refresco de menor azucar es {MenorAzucar}")
                        

            

        except Exception as e:
            print(e)
            print("Vulevalo a intentar")
            

main()