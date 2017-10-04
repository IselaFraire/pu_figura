# -*- coding: utf-8 -*-
from lettuce import step, world
from figura import Figura

@step(u'cuando realizo la operacion')
def cuando_realizo_la_operacion(step):
    pass

@step(u'Dado que ingreso la base y altura del rectangulo "([^"]*)" y "([^"]*)"')
def dado_que_ingreso_la_base_y_altura_del_rectangulo_group1_y_group2(step, num1, num2):
    world.figura = Figura()
    world.figura.area_rectangulo(int(num1), int(num2))

@step(u'Dado que ingreso el radio "([^"]*)"')
def dado_que_ingreso_el_radio_group1(step, num1):
    world.figura = Figura()
    world.figura.area_circulo(int(num1))

@step(u'Dado que ingreso tres numero "([^"]*)", "([^"]*)", "([^"]*)"')
def dado_que_ingreso_tres_numero_group1_group2_group1(step, num1, num2, num3):
    world.figura = Figura()
    world.figura.area_trapecio(int(num1), int(num2), int(num3))

@step(u'Dado que ingreso el lado "([^"]*)"')
def dado_que_ingreso_el_lado(step, num1):
    world.figura = Figura()
    world.figura.area_cuadrado(int(num1))

@step(u'entonces obtengo el area "([^"]*)"')
def entonces_obtengo_el_area_group1(step, esperado):
    obtenido = world.figura.obtener_resultado()
    assert float(esperado) == world.figura.obtener_resultado(),\
    'El area esperada es '+esperado+" y el obtenido es"+str(obtenido)

