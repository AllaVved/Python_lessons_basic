# coding: utf-8

__author__ = 'Введенская Алла'

# Задача-1: Дано произвольное целое число, вывести самую большую цифру этого числа.
# Например, дается x = 58375.
# Нужно вывести максимальную цифру в данном числе, т.е. 8.
# Подразумевается, что мы не знаем это число заранее.
# Число приходит в виде целого беззнакового.
# Подсказки:
# * постарайтесь решить задачу с применением арифметики и цикла while;
# * при желании и понимании решите задачу с применением цикла for.

# Пример 1
x = 58375
max_digit = 0
while x%10 > 1:
    digit = x%10
    x //= 10
    if digit > max_digit:
        max_digit = digit
print("Максимальное число - ", max_digit)

# Пример 2
x = 58375
g = max(str(x))
print("Максимальное число - ", g)



# Задача-2: Исходные значения двух переменных запросить у пользователя.
# Поменять значения переменных местами. Вывести новые значения на экран.
# Решите задачу, используя только две переменные.
# Подсказки:
# * постарайтесь сделать решение через действия над числами;
# * при желании и понимании воспользуйтесь синтаксисом кортежей Python.

A = input("Введите число A - ")
B = input("Введите число B - ")
A, B = B, A
print("A = ", A)
print("B = ", B)



# Задача-3: Напишите программу, вычисляющую корни квадратного уравнения вида
# ax² + bx + c = 0.
# Коэффициенты уравнения вводятся пользователем.
# Для вычисления квадратного корня воспользуйтесь функцией sqrt() модуля math:
# import math
# math.sqrt(4) - вычисляет корень числа 4

import math
	
print("Введите коэффициенты для квадратного уравнения (ax^2 + bx + c = 0):")
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))
 
discr = b**2 - 4 * a * c

if discr > 0:
	x1 = (-b + math.sqrt(discr)) / (2 * a)
	x2 = (-b - math.sqrt(discr)) / (2 * a)
	print("Первый корень = ", x1)
	print("Второй корень = ", x2)
	
elif discr == 0:
	x = -b / (2 * a)
	print("Корень = ", x)
	
else:
	print("Корней нет")
