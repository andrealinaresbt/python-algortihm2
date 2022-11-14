from automovil import Automovil
from carros import Car
from motos import Bike

def mostrarAutomoviles(automoviles):
    for vehiculos in automoviles:
        vehiculos.mostrar()

def salidacarros(vehiculos, exited_car, horaSalida):
     for diccionarios in vehiculos:
        if exited_car in diccionarios['placa']:
            Automovil.salida(diccionarios, horaSalida)
            



# def mostrarAutomovilesRest():
#     for vehiculos2 in Automovil.automovil:
#         vehiculos2.mostrar()

def welcome():
    print('Welcome!')

def goodbye():
    print("Goodbye!")


def main():
    welcome()
    automovil= None
    automovil2= None
    automovil3= None
    automoviles =[]
    vehiculos = [ 
    { "tipo": "AUTOMOVIL", "placa": "ABC12D", "marca": "Chevrolet", "puesto": "A12", "entrada": "10:00:36", "minusvalido": False},
    { "tipo": "AUTOMOVIL", "placa": "IJK56M", "marca": "Mazda", "puesto": "A33", "entrada": "11:48:22", "minusvalido": False},
    { "tipo": "MOTOCICLETA", "placa": "EFG34H", "marca": "Suzuki", "puesto": "B10", "entrada": "10:20:15"},
]
    for vehicle in vehiculos:
        print(vehicle)
        minusvalido = vehicle.get("minusvalido")
        if vehicle['placa'] == 'ABC12D':
            automovil = (Car(vehicle['placa'],
             vehicle['marca'], vehicle['puesto'], vehicle['entrada'], 
             None, minusvalido))
        elif vehicle['placa'] =="IJK56M":
            automovil2 = (Car(vehicle['placa'],
             vehicle['marca'], vehicle['puesto'], vehicle['entrada'], 
             None, minusvalido))

        else:
            automovil3 =(Bike(vehicle['placa'],
             vehicle['marca'], vehicle['puesto'], vehicle['entrada'], 
             None))
    
    automoviles.append(automovil)
    automoviles.append(automovil2)
    automoviles.append(automovil3)
    

    while True:
        try:
            option = int(input('What do you want to do today? \n1. View cars. \n2. Log an exit. \n3. Exit.'))

            if option == 1:
                mostrarAutomoviles(automoviles)

            elif option ==3:
                goodbye()
                break


            elif option == 2:
               
                        exited_car = input('Please enter the plaque of the car you wish to log the exit of: ').upper()

                        for diccionarios in vehiculos:
                            if exited_car in diccionarios['placa']:
                            
                       
                                horaSalida= input('Please enter the time of exit: ')

                                diccionarios['puesto'] =None
                                diccionarios['horaSa'] =horaSalida
                               
                                

                                while True:

                                    option2= int(input('Do you wish to see what cars are left? \n1. Yes. \n2. No. \n---> '))
                                    if option2 == 1:
                                        mostrarAutomoviles(automoviles)
                                        texto = open('texto.txt', 'w')
                                        datos = texto.write(diccionarios)
                                        texto.close()
                                        
                                    if option2 == 2:
                                        break
                                

                            

                            
#                             minusvalido = vehicle.get("minusvalido")
        
#                             Automovil.automovil2.append(Car(vehicle['placa'],
#                                 vehicle['marca'], None, vehicle['entrada'], 
#              horaSa, minusvalido))

#                             mostrarAutomovilesRest()
# #preguntar por que no se guarda
                            

                        
                        # elif exited_car != vehicle['placa'] :
                        
                        #         print('Please enter a valid plaque')

                                
                        


        except Exception as e:
            print(e)
            print("Vulevalo a intentar")
            
        


main()