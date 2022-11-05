class Product():
    productos = []
    def __init__(self, id, name, stock, color):
        self.id = id
        self.name = name
       
        self.stock = stock
        self.color = color

    def mostrar(self):
        print(f'id: {self.id}')
        print(f'name: {self.name}')
        print(f'stock: {self.stock}')
       
    #por default vou a asumir que es none, hasta que le pase un parametro
        if self.color != None:
            print('colors:')
            for color in self.color:
                print(f' {color}')
        else:
            print('Sin color')

        print('')
