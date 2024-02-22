from enum import Enum

class Tipo(Enum):
    VERTEBRADO = "Vertebrado"
    INVERTEBRADO = "Invertebrado"

class Animal:
    def __init__ (self, cantPatas, tipo):
        self.cantPatas = cantPatas
        self.tipo = tipo
    
    def comer (self):
        print ("Estoy comiendo")

class Perro(Animal):
    def __init__(self, cantPatas, tipo, nombre, raza):
        super().__init__(cantPatas, tipo)
        self.nombre = nombre
        self.raza = raza
    
    def correr (self):
        print ("Estoy corriendo")

class Aguila(Animal):
    def __init__(self, cantPatas, tipo):
        super().__init__(cantPatas, tipo)
    
    def volar (self):
        print ("Estoy volando")

perro1 = Perro (4, Tipo.VERTEBRADO.value, "Ciro", "Labrador")
perro2 = Perro (4, Tipo.VERTEBRADO.value, "Luna", "Caniche")
perro3 = Perro (4, Tipo.VERTEBRADO.value, "Lilo", "Salchicha")

aguila1 = Aguila (2, Tipo.VERTEBRADO.value)
aguila2 = Aguila (2, Tipo.VERTEBRADO.value)
aguila3 = Aguila (2, Tipo.VERTEBRADO.value)

perro1.comer()
perro2.correr()
perro3.comer()

aguila1.comer()
aguila2.volar()
aguila3.volar()