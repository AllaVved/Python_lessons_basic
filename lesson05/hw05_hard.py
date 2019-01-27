# coding: utf-8

__author__ = 'Введенская Алла'

# Задание-1:
# Доработайте реализацию программы из примера examples/5_with_args.py,
# добавив реализацию следующих команд (переданных в качестве аргументов):
#   cp <file_name> - создает копию указанного файла
#   rm <file_name> - удаляет указанный файл (запросить подтверждение операции)
#   cd <full_path or relative_path> - меняет текущую директорию на указанную
#   ls - отображение полного пути текущей директории
# путь считать абсолютным (full_path) -
# в Linux начинается с /, в Windows с имени диска,
# все остальные пути считать относительными.

# Важно! Все операции должны выполняться в той директории, в который вы находитесь.
# Исходной директорией считать ту, в которой был запущен скрипт.

# P.S. По возможности, сделайте кросс-платформенную реализацию.

import os
import sys
import shutil
print('sys.argv = ', sys.argv)

# Получение справки
def print_help():
	print("help - получение справки")
	print("mkdir <dir_name> - создание директории")
	print("ping - тестовый ключ")
	print("cp <file_name> - создает копию указанного файла")
	print("rm <file_name> - удаляет указанный файл")
	print("cd <full_path or relative_path> - меняет текущую директорию на указанную")
	print("ls - отображение полного пути текущей директории")

# Создаем папку
def make_dir():
	if not dir_name:
		print("Необходимо указать имя директории вторым параметром")
		return
	dir_path = os.path.join(os.getcwd(), dir_name)
	try:
		os.mkdir(dir_path)
		print('директория {} создана'.format(dir_name))
	except FileExistsError:
		print('директория {} уже существует'.format(dir_name))

# Выводим ping
def ping():
	print("ping")


# Копируем файл
def copy_file():
	if not file_name:
		print("Необходимо указать имя файла вторым параметром")
		return
	try:
		file_copy = file_name + ".copy" 
		shutil.copy(file_name, file_copy)
		print(f"Файл {file_name} скопирован в {file_copy}")
	except:
		print("Невозможно скопировать файл")

		
# Удоляем файл
def remove_file():
	if not file_name:
		print("Необходимо указать имя файла вторым параметром")
		return
	try:
		print(f"Вы точно желаете удалить файл {file_name}?")
		go = input("Yas/No: ")
		if go == 'Yas':
			os.remove(file_name)
			print(f"Файл {file_name} удален")
		elif go == 'No':
			print(f"Удаление файла {file_name} отменено")
		else:
			print("Подтверждение введено не корректно")
	except:
		print(f"Невозможно удалить файл {file_name}")
		
# Переходим в папку	
def come_dir():
	if not dir_name:
		print("Необходимо указать имя директории вторым параметром")
		return
	try:
		path = os.path.join(dir_name)
		os.chdir(path)
		print(f"Успешно перешли в директорию {os.getcwd()}")
	except:
		print("Невозможно перейти")

# Абсолютный путь
def full_path_dir():
	print(os.path.abspath(os.getcwd()))

do = {
    "help": print_help,
    "mkdir": make_dir,
    "ping": ping,
    "cp": copy_file,
    "rm": remove_file,
    "cd": come_dir,
    "ls": full_path_dir,
}

try:
    dir_name = sys.argv[2]
    file_name = sys.argv[2]
except IndexError:
    dir_name = None
    file_name = None

try:
    key = sys.argv[1]
except IndexError:
    key = None


if key:
    if do.get(key):
        do[key]()
    else:
        print("Задан неверный ключ")
print("Укажите ключ help для получения справки")

