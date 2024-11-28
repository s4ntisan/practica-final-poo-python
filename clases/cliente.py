class Cliente: #2 paso
    def __init__(self,nombre,direccion,telefono):
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono
        self.historial_compras = [] #no lo paso por el constructor

    def actualizar_informacion(self, direccion = None, telefono = None): # El none hace que si no tienen un valor original van a estar sin valor o indefinidos
        if direccion:
            self.direccion = direccion
        if telefono:
            self.telefono = telefono

    def registrar_compra(self,compra): # Si recibe compra la agrega al historial
        self.historial_compras.append(compra)

    def mostrar_informacion(self):
        return f"Cliente: {self.nombre}, direccion: {self.direccion}, telefono: {self.telefono}"
