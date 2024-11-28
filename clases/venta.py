from datetime import datetime 

class Venta:
    def __init__(self, cliente, lista_de_productos):
        self.cliente = cliente
        self.lista_de_productos = lista_de_productos
        self.fecha = datetime.now() #cuando se ejecuta una venta pone la fecha del momento
        self.total = self.calcular_total() # es igual a un método que todavía no esta creado

    def calcular_total(self):
        return sum(producto.precio for producto in self.lista_de_productos)
    # recorremos producto en la lista de productos que nos van a pasar.
    # cada producto va a tener un precio, la sumatoria de los precios de c/u de los precios de la lista va a ser el total

    def registrar_venta(self):
        self.cliente.registrar_compra(self) # característica de clase cliente
        return f"Venta registrada: {self.mostrar_informacion()}" #mostrar informacion todavia no lo tenemos creado
    
    def mostrar_informacion(self):
        productos = ", ".join([producto.nombre for producto in self.lista_de_productos]) #hacemos un join, juntamos una lista de productos
    # Unimos los productos usando una , y espacio y los nombres los vamos a sacar de la lista de productos (tomamos de cada producto el nombre)
    # Queremos que vuelva un string de la lista separada por , y espacio.
        return f"Cliente: {self.cliente.nombre}, Productos: {productos}, Total: {self.total}"

