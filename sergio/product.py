class Product():
  productos = []
  def __init__(self, id, name, stock, colors):
    self.id = id
    self.name = name
    self.stock = stock   
    self.colors = colors

  def mostrar(self):
    print(f"Id: {self.id}")
    print(f"Name: {self.name}")
    print(f"Stock: {self.stock}")

    if self.colors != None:
      print("Colors:")
      for color in self.colors:
        print(f"  {color}")
    else:
      print("Sin color")

    print("")

  
  def actualizarStock(self, amount):
    self.stock -= amount
  def buscarPorId(id):
    for product in Product.productos:
      if product['id'] == id:
        return product