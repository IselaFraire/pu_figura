class Figura(object):

    def __init__(self):
        self.resultado = 0

    def area_rectangulo(self, base, altura):
        self.resultado = base * altura

    def area_circulo(self,radius):
        self.resultado = round(3.1416 * radius ** 2, 2)

    def area_trapecio(self, base_mayor, base_menor, altura):
        self.resultado = (base_mayor + base_menor) * altura / 2.0

    def area_cuadrado(self, lado):
        self.resultado = lado ** 2

    def obtener_resultado(self):
        return self.resultado
