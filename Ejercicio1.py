class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def hacerSonido(self):
        print(f"{self.nombre} está haciendo un sonido")

class Perro(Animal):
    def ladrido(self):
        print(f"{self.nombre} esta ladrando")

animal = Animal("Animal Genérico")
animal.hacerSonido()

perro = Perro("Cujo")
perro.hacerSonido()
perro.ladrido()
