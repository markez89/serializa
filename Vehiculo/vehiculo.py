class Vehiculo:
    puertas= 0
    ruedas = 0
    color = 0
    nombre = ""

    def __init__ (self,puertas, ruedas, color, nombre):
        self.nombre = nombre
        self.puertas = puertas
        self.ruedas = ruedas
        self.color = color

    def getNombre(self):
        return self.nombre

    def getColor(self):
        return self.color

    def __str__ (self):
        return f"El nombre del coches es {self.nombre} tiene {self.puertas} puertas y su color es {self.color}"    
        
