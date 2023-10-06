class Figura:
    def calcularArea(self):
        pass

class Circulo(Figura):
    def __init__(self, radio):
        self.radio = radio

    def calcularArea(self):
        return 3.1416 * (self.radio * self.radio)

figura_abstracta = Figura()

mi_circulo = Circulo(1)
area_circulo = mi_circulo.calcularArea()
print(f"El área del círculo es: {area_circulo}")
