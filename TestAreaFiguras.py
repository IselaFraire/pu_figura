# coding=utf-8
import unittest
from areasfiguras import AreaFiguras

class TestAreasFiguras(unittest.TestCase):

    def setUp(self):
        self.area = AreaFiguras()

    def test_area_rect_5_6_igual_30(self):
        self.assertEquals(self.area.area_rectangulo(5, 6), 30)

    def test_area_square_10_igual_100(self):
        self.assertEquals(self.area.area_cuadrado(10), 100)

    def test_area_circle_10_igual_314(self):
        self.assertEquals(self.area.area_circulo(10), 314.16)

    def test_area_trap_5_6_5_igual_27(self):
        self.assertEquals(self.area.area_trapecio(5, 6, 5), 27.5)

    def tearDown(self):
        pass

if __name__ == '__main__': # pragma: no cover
    unittest.main()
