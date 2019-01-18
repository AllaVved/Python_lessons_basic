# coding: utf-8

# Задача-1:
# Дан список фруктов.
# Напишите программу, выводящую фрукты в виде нумерованного списка,
# выровненного по правой стороне.

# Пример:
# Дано: ["яблоко", "банан", "киви", "арбуз"]
# Вывод:
# 1. яблоко
# 2.  банан
# 3.   киви
# 4.  арбуз

# Подсказка: воспользоваться методом .format()


Fruits = ['Яблоко', 'Банан', 'Киви', 'Арбуз', 'Манго', 'Груша', 'Дыня']
last_name = len(Fruits)
for i in range(last_name):
	print(f"{str(i + 1)}{Fruits[i]:>10}")



# Задача-2:
# Даны два произвольные списка.
# Удалите из первого списка элементы, присутствующие во втором списке.



One_list = [1, 2, 3, 4, 5]
Two_list = [2, 3, 6, 7, 8]
for item in Two_list:
	if item in One_list:
		One_list.remove(item)
print(One_list)


# Задача-3:
# Дан произвольный список из целых чисел.
# Получите НОВЫЙ список из элементов исходного, выполнив следующие условия:
# если элемент кратен двум, то разделить его на 4, если не кратен, то умножить на два.


List = [2, 7, 5, 6, 9, 15]
New_list = []
last_name = len(List)
for i in range(last_name):
	if List[i] % 2 == 0:
		New_list.append(List[i] / 4)
	else:
		New_list.append(List[i] * 2)
print(New_list)
