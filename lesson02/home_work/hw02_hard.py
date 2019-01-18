#!/usr/bin/env python3
# coding: utf-8


# Задание-1: уравнение прямой вида y = kx + b задано в виде строки.
# Определить координату y точки с заданной координатой x.

equation = 'y = -12x + 11111140.2121'
x = 2.5
# вычислите и выведите y

a = equation.split(' ')
a1 = str(a[2])
a[2] = a1[:-1]
y = float(a[2]) * x + float(a[4])
print(y)





# Задание-2: Дата задана в виде строки формата 'dd.mm.yyyy'.
# Проверить, корректно ли введена дата.
# Условия корректности:
# 1. День должен приводиться к целому числу в диапазоне от 1 до 30(31)
#  (в зависимости от месяца, февраль не учитываем)
# 2. Месяц должен приводиться к целому числу в диапазоне от 1 до 12
# 3. Год должен приводиться к целому положительному числу в диапазоне от 1 до 9999
# 4. Длина исходной строки для частей должна быть в соответствии с форматом 
#  (т.е. 2 символа для дня, 2 - для месяца, 4 - для года)

# Пример корректной даты
date = '01.11.1985'

# Примеры некорректных дат
date = '01.22.1001'
date = '1.12.1001'
date = '-2.10.3001'


# Пример 1

import time


date = str(input('Введите дату: '))
day, month, year = date.split('.')
days_count_by_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
 
if len(day) == 2 and len(month) == 2 and len(year) == 4:
	if 0 < int(month) <= 12  \
	and 0 < int(year) <= 9999 \
	and 0 < int(day) <= days_count_by_month[int(month)]:
		print("Дата введена корректна")
	else:
		print("Дата введена не корректна")
else:
	print("Дата введена не корректна")

# Пример 2

import time

date = str(input('Введите дату: '))

try:
	struct_time = time.strptime(date, "%d%m%Y")
	print ("Дата введена корректна")
except ValueError:
	print("Дата введена не корректна")
 


# Задание-3: "Перевёрнутая башня" (Задача олимпиадного уровня)
#
# Вавилонцы решили построить удивительную башню —
# расширяющуюся к верху и содержащую бесконечное число этажей и комнат.
# Она устроена следующим образом — на первом этаже одна комната,
# затем идет два этажа, на каждом из которых по две комнаты, 
# затем идёт три этажа, на каждом из которых по три комнаты и так далее:
#         ...
#     12  13  14
#     9   10  11
#     6   7   8
#       4   5
#       2   3
#         1
#
# Эту башню решили оборудовать лифтом --- и вот задача:
# нужно научиться по номеру комнаты определять,
# на каком этаже она находится и какая она по счету слева на этом этаже.
#
# Входные данные: В первой строчке задан номер комнаты N, 1 ≤ N ≤ 2 000 000 000.
#
# Выходные данные:  Два целых числа — номер этажа и порядковый номер слева на этаже.
#
# Пример:
# Вход: 13
# Выход: 6 2
#
# Вход: 11
# Выход: 5 3

room = int(input('Введите номер комнаты: '))
block = 1
stage = 1
last_room_on_stage = 1
 
while room > last_room_on_stage:
	stage = stage + block
	block += 1
	last_room_on_stage = block ** 2 + last_room_on_stage
 
rooms_in_block = []

for i in range(block**2):
	rooms_in_block.append(last_room_on_stage - i)
 
rooms_in_block.reverse()
part_of_block_index = 0
part_of_block = []
 
offset = 0

for i in range(block,block**2+block,block):
	if room in rooms_in_block[offset:i]:
		part_of_block_index = int(i/block)
		part_of_block = rooms_in_block[offset:i]
		break
	offset += block
 
stage = part_of_block_index + stage -1
position = part_of_block.index(room) + 1

print(stage, position)
