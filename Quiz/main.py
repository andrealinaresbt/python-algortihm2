from vehicle import Vehicle
from vehicle import Automovil
from vehicle import Bike

def welcome():
    print('--------WELCOME--------')

def mostrarCarros():
    for carros in Vehicle.vehiculo:
        carros.informacion()

def main():
    vehiculo = []
    vehiculo2=[]
    vehiculo3 = []
    caracteristicas1 =[]
    caracteristicas2 = []
    listaVehiculo =[]
    moto =[]
    welcome()
    vehiculos = [ 
    { "tipo": "AUTOMOVIL", "placa": "ABC12D", "marca": "Chevrolet", "puesto": "A12", "entrada": "10:00:36", "minusvalido": False},
    { "tipo": "AUTOMOVIL", "placa": "IJK56M", "marca": "Mazda", "puesto": "A33", "entrada": "11:48:22", "minusvalido": False},
    { "tipo": "MOTOCICLETA", "placa": "EFG34H", "marca": "Suzuki", "puesto": "B10", "entrada": "10:20:15"},
]

    hola = []
    hola.extend((1,2,3,4))
    print(vehiculos[0])
    
   
#  como hacer para agregar lo de minusvalido
    while True:
        option = int(input('''What would you like to do today?
        1. Register an entrance.
        2. Register an exit.
        3. Show vehicles.
        4. Exit
        ----> '''))

        if option == 1:
        
                    vehiculo = vehiculos[0]
                    caracteristicas1.extend((vehiculo['placa'], vehiculo['marca'], vehiculo['puesto'], vehiculo['entrada'], vehiculo['minusvalido'],  None))
                    # print(vehiculo)
                    # listaVehiculo['uno']= caracteristicas1
                    # print(listaVehiculo)
                    # break
                    
                    vehiculo2  = vehiculos[1]
                    print(vehiculo2)
                    caracteristicas2.extend((vehiculo2['placa'], vehiculo2['marca'], vehiculo2['puesto'], vehiculo2['entrada'], vehiculo2['minusvalido'],  None))
                    # print(vehiculo)
                    # listaVehiculo['dos'] = caracteristicas2
                    vehiculo3  = vehiculos[2]
                    moto.extend((vehiculo['placa'], vehiculo['marca'], vehiculo['puesto'], vehiculo['entrada'],  None))
                    # carros = Vehicle(caracteristicas1)
                    print(caracteristicas1)
                    caracteristicas2 = tuple(caracteristicas2)
                    listaVehiculo.append(Automovil(caracteristicas2))
                    print(listaVehiculo)


                    #vehiculo = Vehicle(vehiculos)
                    # print(vehiculo.informacion())
                    # print(carro)
                    # print(carro)
                    # print(carro)
                    # print(carro)
                    # print(carro)
            #         Vehicle.vehiculo.append(Automovil(moviles["placa"], moviles["marca"], moviles["puesto"], moviles['entrada'], None, moviles['minusvalido']))
            #     else:
            #         Vehicle.vehiculo.append(Bike(moviles["placa"], moviles["marca"], moviles["puesto"], moviles["entrada"], None))
            # print('Success')

            
        elif option == 2:
            mostrarCarros()
            plateNumber = input("Enter the plate number of the vehicle you wish to retire: \n").upper()
            if plateNumber == 'ABC12D':
                horaSalida = input('Please enter the exit time: ')
                for moviles in vehiculos:
                    pass


        elif option ==3:
            pass
        else:
            print('Thank you for coming!')
            break

        #llamas al  objeto y en vez de a la clase y creas la lista en el main.
        #del() para eliminar el atributo
main()


                    # vehiculo.extend((moviles['placa'], moviles['marca'], moviles['puesto'], moviles['entrada'], moviles['minusvalido'],  None))
                    # print(vehiculo)
                    # listaVehiculo['uno']= vehiculo
                    # print(listaVehiculo)
                    # break

                        
                    
                         #   listaVehiculo['dos'] = vehiculo

             #   print(listaVehiculo)
                    
                
                # vehiculo.extend((moviles['placa'], moviles['marca'], moviles['puesto'], moviles['entrada'], moviles['minusvalido'],  None))
                # print(vehiculo)
                        
                    
            