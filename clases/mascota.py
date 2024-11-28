class Mascota: #1 paso
    def __init__(self,nombre,edad,salud,precio):
        self.nombre = nombre
        self.edad = edad
        self.salud = salud
        self.precio = precio

    def actualizar_información(self, edad = None, salud = None, precio = None):
        if edad: # en principio es None, pero si nos la pasan
            self.edad = edad
        if salud: # en principio es None, pero si nos la pasan
            self.salud = salud
        if precio: # en principio es None, pero si nos la pasan
            self.precio = precio

    def mostrar_informacion(self):
        return f"Mascota: {self.nombre}, Edad: {self.edad}, Salud: {self.salud}, Precio: {self.precio}"
    
class Perro(Mascota):
    def __init__(self,nombre, edad, salud, precio, raza, nivel_de_energia):
        super().__init__(nombre,edad,salud,precio) # Propio de mascota. 
        self.raza = raza
        self.nivel_de_energia = nivel_de_energia

    def mostrar_caracteristicas(self):
        return f"Raza: {self.raza}, Nivel de energia: {self.nivel_de_energia}"
    
class Gato(Mascota):
    def __init__(self,nombre, edad, salud, precio, raza, independencia):
        super().__init__(nombre,edad,salud,precio) # Propio de mascota. 
        self.raza = raza
        self.independencia = independencia

    def mostrar_caracteristicas(self):
        return f"Raza: {self.raza}, Independencia: {self.independencia}"