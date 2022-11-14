from product import Product

class Flower(Product):
  def __init__(self, id, name, stock, colors):
    super().__init__(id, name, stock, colors)