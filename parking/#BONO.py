archivo = open('lista.txt', 'r')
datos = archivo.read()
archivo.close()
print(datos)

vehiculos =[ 
    { "tipo": "AUTOMOVIL", "placa": "ABC12D", "marca": "Chevrolet", "puesto": "A12", "entrada": "10:00:36", "minusvalido": False},
    { "tipo": "AUTOMOVIL", "placa": "IJK56M", "marca": "Mazda", "puesto": "A33", "entrada": "11:48:22", "minusvalido": False},
    { "tipo": "MOTOCICLETA", "placa": "EFG34H", "marca": "Suzuki", "puesto": "B10", "entrada": "10:20:15"},
]

archivo2 = open('Hola.txt', 'w')
datos2 = archivo2.write(str(vehiculos))
archivo2.close()
print(datos2)