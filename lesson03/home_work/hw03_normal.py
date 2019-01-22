# coding: utf-8

__author__ = 'Введенская Алла'

# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1

def fibonacci(n, m):

	fib_list = []
	a, b = 1, 1
	while a <= m:
		a, b = b, a + b
		if n <= a <= m:
			fib_list.append(a)
	return fib_list

n = int(input('Введите начальное число Фибоначчи: '))
m = int(input('Введите конечное значение: '))

print (f"Числа Фибоначчи в диапозоне от {n} до {m}: {fibonacci(n, m)}" )


# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()


def sort_to_max(origin_list):
	n = len(origin_list)
	
	for j in range(0,n-1):
		for i in range(0,n-j-1):
			if origin_list[i] < origin_list[i+1]:
				origin_list[i+1], origin_list[i] = origin_list[i], origin_list[i+1]
	return origin_list[::-1]
	
print(sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0]))

# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.

def filter_list(fucnt, param):
    new_list = list()
    for x in param:
        if fucnt(x) == True:
            new_list.append(x)
        else:
            continue
    return new_list
 
 
print((filter_list((lambda x: x > 10), param = [10, 57, 158, 259, 2, 98, 5, 46, 8, 9, 598])))

# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.

def is_parallelogram(A1, A2, A3, A4):
	
	if (A3[0] - A2[0]) == (A4[0] - A1[0]) and \
		(A2[1] - A1[1]) == (A3[1] - A4[1]):
		return "Это вершины параллелограмма"
	return "Это вершины не параллелограмма"
	
print (is_parallelogram((2, 2), (4, 5), (9, 5), (7, 2)))
print (is_parallelogram((2, 2), (4, 5), (10, 5), (7, 2)))
