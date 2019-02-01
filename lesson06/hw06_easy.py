# coding: utf-8

__author__ = 'Введенская Алла'


# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.

import math


class Triangle:
	def __init__(self, A, B, C):
		def side_len(x, y):
			return math.sqrt((x[0] - y[0]) ** 2 + (x[1] - y[1]) ** 2)
 
		self.A = A
		self.B = B
		self.C = C

		self.AB = side_len(self.A, self.B)
		self.BC = side_len(self.B, self.C)
		self.CA = side_len(self.C, self.A)
 
	def area_Triangle(self):
		per = self.per_Triangle() / 2
 
		return math.sqrt(per * (per - self.AB) * (per - self.BC) * (per - self.CA))
 
	def per_Triangle(self):
		return self.AB + self.BC + self.CA
 
	def hei_Triangle(self):
		return self.area_Triangle() / (self.AB / 2)
 
 
triagle = Triangle((0, 2), (6, 8), (10, 1))
 
print(f"Площадь треугольника = {triagle.area_Triangle()}")
print(f"Высота треугольника = {triagle.hei_Triangle()}")
print(f"Периметр треугольника = {triagle.per_Triangle()}")

# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.


class Trapeze():
	def __init__(self, A, B, C, D):
		def side_len(x, y):
			return math.sqrt((x[0] - y[0]) ** 2 + (x[1] - y[1]) ** 2)   
  
  
		self.A = A
		self.B = B
		self.C = C
		self.D = D

		self.AB = side_len(self.A, self.B)
		self.BC = side_len(self.B, self.C)
		self.CD = side_len(self.C, self.D)
		self.DA = side_len(self.D, self.A)

 
	def check_Trapeze(self):
		if self.BC == self.DA and self.AB != self.CD or self.BC != self.DA and self.AB == self.CD:
			return "Трапеция равнобочная"
		else:
			return "Трапеция не равнобочная"

	def per_Trapeze(self):
		self.per = (self.AB + self.BC + self.CD + self.DA)
		return self.per

	def area_Trapeze(self):
		self.katet = int(math.fabs(self.BC - self.DA)) 
		self.Pythagoras = round(math.sqrt(int((self.AB ** 2) - (self.katet ** 2))), 2) 
		self.half_sum = int(self.BC + self.DA) / 2  
		self.area = self.half_sum * self.Pythagoras
		return self.area


trapeze1 = Trapeze((0, 0), (2, 4), (7, 4), (9, 0))

trapeze2 = Trapeze((0, 1), (2, 4), (6, 5), (8, 1))


print()
print(trapeze1.check_Trapeze())
print(f"Длина сторон трапеции: \nAB = {trapeze1.AB}, \nBC = {trapeze1.BC}, \nCD = {trapeze1.CD}, \nDA = {trapeze1.DA}")
print(f"Периметр трапеции = {trapeze1.per_Trapeze()}")
print(f"Площадь трапеции = {trapeze1.area_Trapeze()}")
print()
print(trapeze2.check_Trapeze())
print(f"Длина сторон трапеции: \nAB = {trapeze2.AB}, \nBC = {trapeze2.BC}, \nCD = {trapeze2.CD}, \nDA = {trapeze2.DA}")
print(f"Периметр трапеции = {trapeze2.per_Trapeze()}")
print(f"Площадь трапеции = {trapeze2.area_Trapeze()}")
