# coding: utf-8

__author__ = 'Введенская Алла'

# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

import os

# Создаем директории 

def make_dir(dir_name = "dir_", x = 9):
	number_dir = 1
	while number_dir <= x:
		path_dir = os.path.join(os.getcwd(), f"{dir_name}{number_dir}")
		try:
			os.mkdir(path_dir) 
			print(f"Деректория {path_dir} создана")
		except FileExistsError:
			print(f"Деректория {path_dir} уже существует")
		number_dir += 1


# Удаляем директории 

def remove_dir(dir_name = "dir_", x = 9):
    number_dir = 1
    while number_dir <= x:
        path_dir = os.path.join(os.getcwd(), f"{dir_name}{number_dir}") 
        try:
            os.rmdir(path_dir) 
            print(f"Директория {path_dir} удалена")
        except FileNotFoundError:
            print(f"Директории {path_dir} несуществует")
        number_dir += 1


# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.


def list_dir():
    path_dir = os.path.join(os.getcwd()) 
    list_dir = os.listdir(path_dir) 
    print(f"Список всех файлов текущий директории: \n{list_dir}")

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.

import shutil

def copy_file():
    path_dir = os.path.realpath(__file__) 
    dir_copy = path_dir + ".copy" 
    shutil.copy(path_dir, dir_copy)
    print(f"Файл {path_dir} скопирован в {dir_copy}")
