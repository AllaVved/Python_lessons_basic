# coding: utf-8

__author__ = 'Введенская Алла'

# Задача-1:
# Напишите небольшую консольную утилиту,
# позволяющую работать с папками текущей директории.
# Утилита должна иметь меню выбора действия, в котором будут пункты:
# 1. Перейти в папку
# 2. Просмотреть содержимое текущей папки
# 3. Удалить папку
# 4. Создать папку
# При выборе пунктов 1, 3, 4 программа запрашивает название папки
# и выводит результат действия: "Успешно создано/удалено/перешел",
# "Невозможно создать/удалить/перейти"

# Для решения данной задачи используйте алгоритмы из задания easy,
# оформленные в виде соответствующих функций,
# и импортированные в данный файл из easy.py


import os
import sys
import hw05_easy

answer = input('Поработаем? (y/n) = ')

while answer:
	if answer == 'y':
		print("1. Перейти в директорию")
		print("2. Просмотреть содержимое текущей директории")
		print("3. Удалить директорию")
		print("4. Создать директорию")
		print("5. Выход")
		do = int(input("Укажите номер действия: "))

		if do == 1:
			try:
				dir_name = str(input ("Укажите полный путь в дерикторию: "))
				dir_name = os.path.join(dir_name)
				os.chdir(dir_name)
				print(f"Успешно перешли в директорию {dir_name}")
			except:
				print("Невозможно перейти")
		elif do == 2:
			hw05_easy.list_dir()

		elif do == 3:
			try:
				dir_name = (input("Укажите имя директории: "))
				x = int(input("Укажите количество директорий: "))
				hw05_easy.remove_dir(dir_name, x)
			except:
				print("Невозможно удалить")
		elif do == 4:
			try:
				dir_name = (input("Укажите имя директории: "))
				x = int(input("Укажите количество директорий: "))
				hw05_easy.make_dir(dir_name, x)
			except:
				print("Невозможно создать")
		elif do == 5:
			print('До свидания!')
			exit()
		else:
			print("Неверно указан номер действия")

	elif answer == 'n':
		print('До свидания!')
		exit()
	elif answer != 'n' and answer != 'y':
		print('Ответ не корректен! Попробуйте ещё раз!')
		answer = input('Поработаем? (y/n) = ')
		continue
