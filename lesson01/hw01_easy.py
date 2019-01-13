# coding: utf-8


__author__ = 'Введенская Алла'

# Задача-1: Дано произвольное целое число (число заранее неизвестно).
# Вывести поочередно цифры исходного числа (порядок вывода цифр неважен).
# Подсказки:
# * постарайтесь решить задачу с применением арифметики и цикла while;
# * при желании решите задачу с применением цикла for.

# Пример 1

Number = str(input("Введите число - "))
i, count = 0, len(Number)
while i < count:
	print(Number[i])
	i += 1


# Пример 2

Number = input("Введите число - ")
while Number >= 1:
	digit = Number%10
	Number //= 10
	print(digit)

# Задача-2: Исходные значения двух переменных запросить у пользователя.
# Поменять значения переменных местами. Вывести новые значения на экран.
# Подсказка:
# * постарайтесь сделать решение через дополнительную переменную 
#   или через арифметические действия
# Не нужно решать задачу так:
# print("a = ", b, "b = ", a) - это неправильное решение!

A = input("Введите число A - ")
B = input("Введите число B - ")
C = A
A = B
B = C
print("A = ", A)
print("B = ", B)


# Задача-3: Запросите у пользователя его возраст.
# Если ему есть 18 лет, выведите: "Доступ разрешен",
# иначе "Извините, пользование данным ресурсом только с 18 лет"

Age = int(input("Введите ваш возраст - "))
if Age >= 18:
	print("Доступ разрешен")
else :
	print("Извините, пользование данным ресурсом только с 18 лет")



