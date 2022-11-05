from flower import Flower
from semilla import Semilla
from prodtuct import Product

def mostrarProducts():
    for product in Product.productos:
        product.mostrar()

def main():
        
    products = [
    { 'id': 1, 'name': 'Rose', 'type': 'flower', 'stock': 160, 'colors': ['red', 'white', 'pink'] },
    { 'id': 2, 'name': 'Tulip', 'type': 'flower', 'stock': 34, 'colors': ['white', 'yellow'] },
    { 'id': 3, 'name': 'Sunflower seeds', 'type': 'seeds', 'stock': 50 },
    { 'id': 4, 'name': 'Sunflower', 'type': 'flower', 'stock': 77, 'colors': ['yellow'] },
    { 'id': 5, 'name': 'Lavender seeds', 'type': 'seeds', 'stock': 100, 'colors': ['purple'] },
    { 'id': 6, 'name': 'Carnation', 'type': 'flower', 'stock': 89, 'colors': ['yellow', 'burgundy', 'purple', 'pink', 'red', 'white'] },
    ]
    
    vendor_1 = [
    { 'product_id': 5, 'customer_id': 333, 'amnt': 1 },
    { 'product_id': 5, 'customer_id': 1010, 'amnt': 2 },
    { 'product_id': 3, 'customer_id': 1111, 'amnt': 3 },
    { 'product_id': 2, 'customer_id': 222, 'amnt': 6 },
    { 'product_id': 6, 'customer_id': 444, 'amnt': 7 },
    { 'product_id': 1, 'customer_id': 1111, 'amnt': 20 },
    ]
    
    vendor_2 = [
    { 'product_id': 6, 'customer_id': 888, 'amnt': 10 },
    { 'product_id': 1, 'customer_id': 123, 'amnt': 5 },
    { 'product_id': 2, 'customer_id': 321, 'amnt': 4 },
    { 'product_id': 4, 'customer_id': 555, 'amnt': 2 },
    { 'product_id': 1, 'customer_id': 777, 'amnt': 1 },
    ]
    
    for product in products:
        color = product.get('colors')
        if product["type"] == "flower":
            Product.productos.append(Flower(product['id'], 
                product['name'], 
                product['stock'], 
                color))
        else:
            Product.productos.append(Semilla(product['id'], 
                product['name'],  
                product['stock'], 
                color))

    while True:
        try:
            respuesta = int(input('1. View inventory. \n2. Modulo de distribucion de inventario. \n3. Salir.'))

            if respuesta == 1:
                mostrarProducts()
            elif respuesta ==2:
                pass
            else:
                print('---------------------- GOODBYE-----------------------')
                break
        except Exception as e:
            print(e)
            print('Vuelve a intentar.')


    
        

main()