
import math

class AreaFiguras():

    def area_rectangulo(self, base, height):
        return base * height

    def area_cuadrado(self, side):
        return side ** 2

    def area_trapecio(self, mayor_base, minor_base, height):
        return (mayor_base + minor_base) * height / 2.0

    def area_circulo(self,radius):
        return round(3.1416 * radius ** 2, 2)
