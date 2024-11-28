class Inventario:
    def __init__(self):
        self.lista_de_productos = []

    def agregar_producto(self,producto): #tiene la instancia y el producto nuevo
        self.lista_de_productos.append(producto)
    
    def actualizar_inventario(self, producto, cantidad):
        for prod in self.lista_de_productos:
            if prod.nombre == producto.nombre: #Si coincide el nombre (prod es cada una de las vueltas del bucle) con el nombre del producto que nos pasaron
                prod.actualizar_cantidad(cantidad) # pertenece a la clase producto

    def generar_alerta(self, umbral_minimo):
        alertas = [prod.nombre for prod in self.lista_de_productos if prod.cantidad < umbral_minimo] # Una alerta va a ser cuando el número de la cantidad de productos sea menor al umbral que pongamos
        return f"Productos por debajo del umbral: {", ".join(alertas)}" if alertas else "No hay ningun producto por debajo del umbral mínimo determinado" # Si hay alertas muestra:productos por debajo del humbral y join de alertas si no, muestra: no hay ningun producto...