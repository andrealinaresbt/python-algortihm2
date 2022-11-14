from product import Product

class Vendedor():
  ordenado = []
  def __init__(self, id, customer, amount):
    self.productId = id
    self.customer = customer
    self.amount = amount

  def mostrar(self):
    print(f"productId: {self.productId}")
    print(f"Customer: {self.customer}")
    print(f"Amount: {self.amount}")
    print("")

  def ActualizarStockProduct(self):
    self.mostrar()

    producto = Product.buscarPorId(self.productId)

    producto.actualizarStock(self.amount)
    
  
  def llenarOrdenado(asc, desc):
    pointerAsc = 0
    pointerDesc = -1

    while (pointerAsc < len(asc)) or (pointerDesc * -1) <= len(desc): #Voy a seguir, hasta haber recorrido las 2 listas
      if (pointerDesc * -1) > len(desc): #Si termine de recorrer el descendente, pero todavia me falta en ascendete
        Vendedor.ordenado.append(Vendedor(asc[pointerAsc][ "product_id"], asc[pointerAsc]["customer_id"], asc[pointerAsc]["amnt"]))
        pointerAsc += 1

      elif pointerAsc == len(asc): #Si termine de recorrer el ascendente, pero todavia me falta en descente
        Vendedor.ordenado.append(Vendedor(desc[pointerDesc][ "product_id"], desc[pointerDesc]["customer_id"], desc[pointerDesc]["amnt"]))
        pointerDesc -= 1
      else:
      
        if asc[pointerAsc]["amnt"] <= desc[pointerDesc]["amnt"]: #Si mi pointer en ascendente es <= a mi pointer en descente  ---> meto el ascendente
          Vendedor.ordenado.append(Vendedor(asc[pointerAsc][ "product_id"], asc[pointerAsc]["customer_id"], asc[pointerAsc]["amnt"]))
          pointerAsc += 1
        else:  #Si mi pointer en ascendente es > a mi pointer en descente  ---> meto el descendente
          Vendedor.ordenado.append(Vendedor(desc[pointerDesc][ "product_id"], desc[pointerDesc]["customer_id"], desc[pointerDesc]["amnt"]))
          pointerDesc -= 1

      ultimoVendedor = Vendedor.ordenado[-1]
      ultimoVendedor.ActualizarStockProduct()