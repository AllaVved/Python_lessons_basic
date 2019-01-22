# coding: utf-8

__author__ = 'Введенская Алла'

# Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.

def my_round(number, ndigits):
	
# Пример 1

    	number = number * (10 ** ndigits)
	if float(number) - int(number) > 0.5:
		number = number // 1 + 1
	else:
		number = number // 1
	return number / (10 ** ndigits)
	
# Пример 2

	number = number*(10**ndigits)+0.4
	number = number//1
	return number/(10**ndigits) 


print(my_round(2.1234567, 5))
print(my_round(2.1999967, 5))
print(my_round(2.9999967, 5))


# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить

def lucky_ticket(ticket_number):
	
	if (len(str(ticket_number))!= 6) or (type(ticket_number) is not int):
		return f'Билет {ticket_number} номер некорректный '
	number = str(ticket_number)
	sumA = int(number[0]) + int(number[1]) + int(number[2])
	sumB = int(number[3]) + int(number[4]) + int(number[5])
	if sumA == sumB:
		return f'Билет {ticket_number} счастливый' 
	else:
		return f'Билет {ticket_number} несчастливый'
		

print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))
