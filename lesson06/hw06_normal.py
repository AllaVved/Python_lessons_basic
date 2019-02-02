# coding: utf-8

__author__ = 'Введенская Алла'

# Задание-1:
# Реализуйте описаную ниже задачу, используя парадигмы ООП:
# В школе есть Классы(5А, 7Б и т.д.), в которых учатся Ученики.
# У каждого ученика есть два Родителя(мама и папа).
# Также в школе преподают Учителя. Один учитель может преподавать 
# в неограниченном кол-ве классов свой определенный предмет. 
# Т.е. Учитель Иванов может преподавать математику у 5А и 6Б,
# но больше математику не может преподавать никто другой.

# Выбранная и заполненная данными структура должна решать следующие задачи:
# 1. Получить полный список всех классов школы
# 2. Получить список всех учеников в указанном классе
#  (каждый ученик отображается в формате "Фамилия И.О.")
# 3. Получить список всех предметов указанного ученика 
#  (Ученик --> Класс --> Учителя --> Предметы)
# 4. Узнать ФИО родителей указанного ученика
# 5. Получить список всех Учителей, преподающих в указанном классе

class Person:
	def __init__(self, surname, name, patronymic, birth_date):
		self.surname = surname
		self.name = name
		self.patronymic = patronymic
		self.birth_date = birth_date
	def get_full_name(self):
		return self.surname + ' ' + self.name + ' ' + self.patronymic
	def get_surname_initials(self):
		return self.surname + ' ' + self.name[0] + '.' + self.patronymic[0] + '.'
	def set_name(self, new_name):
		self.surname = new_name

class Teacher(Person):
	def __init__(self, surname, name, patronymic, birth_date, subject):
		Person.__init__(self, surname, name, patronymic, birth_date)
		self.subject = subject
# 5. Получить список всех Учителей, преподающих в указанном классе	
	def teacher_in_class_rooms(class_rooms):
		for teacher in class_rooms.teachers:
			print(teacher.get_full_name())
			
	def sub(students):  # Для 3 пункта
		for teacher in students.class_rooms.teachers:
			print(teacher.subject)

class Class_room:
	def __init__(self, class_room, teachers):
		self.class_room = class_room
		self.teachers = teachers
# 1. Получить полный список всех классов школы
	def class_room(self):
		for cl in class_rooms:
			print(cl.class_room)
# 2. Получить список всех учеников в указанном классе
	def get_list_students(class_rooms):
		for st in students:
			if st.class_rooms == class_rooms:
				print(st.get_surname_initials()) 

	
class Student(Person):
	def __init__(self, surname, name, patronymic, birth_date, class_rooms, parents):
		Person.__init__(self, surname, name, patronymic, birth_date)
		self.class_rooms = class_rooms
		self.parents = parents

# 4. Узнать ФИО родителей указанного ученика
	def parent(students):
		for parent in students.parents:
			print(parent.get_full_name())				

teachers = [Teacher('Петрова', 'Нина', 'Геннадьвна', '11.11.1980', 'математика'),
			Teacher('Васильева', 'Любовь', 'Анатольевна', '10.12.1981', 'русский язык'),
			Teacher('Федорова', 'Екатерина', 'Ивановна', '01.10.1979', 'литература'),
			Teacher('Иванова', 'Любовь', 'Викторовна', '14.02.1981', 'геометрия'),
			Teacher('Львова', 'Надежда', 'Васильевна', '10.05.1977', 'иносртанный язык'),
			Teacher('Николаев', 'Петр', 'Анатльевич', '18.02.1971', 'физкультура'),
			Teacher('Егоров', 'Сергей', 'Петрович', '19.09.1970', 'ОБЖ'),
			Teacher('Сергеева', 'Анна', 'Андреева', '11.10.1982', 'биология')]

class_rooms = [Class_room('5 А', [teachers[0], teachers[1], teachers[2]]),
				Class_room('5 Б', [teachers[3], teachers[1], teachers[2]]),
				Class_room('7 А', [teachers[5], teachers[4], teachers[2]]),
				Class_room('7 В', [teachers[5], teachers[6], teachers[7]])]

parents = [Person("Иванов", "Андрей", "Сергеевич", '15.11.1970'),
			Person("Сидоров", "Александр", "Олегович", '27.01.1980'),
			Person("Андреев", "Петр", "Степанович", '30.05.1979'),
			Person("Петров", "Александр", "Львович", '02.09.1978'),
			Person("Сергеев", "Иван", "Максимович", '01.12.1970'),
			Person("Алевсеев", "Сергей", "Борисович", '25.11.1977'),
			Person("Александров", "Павел", "Михайлович", '03.02.1969'),
			Person("Яковлев", "Алексей", "Анатольевич", '14.03.1981'),
			Person("Иванова", "Анна", "Андреевна", '18.11.1979'),
			Person("Сидорова", "Мария", "Давыдовна", '26.01.1984'),
			Person("Андреева", "Людмила", "Петровна", '17.08.1975'),
			Person("Петрова", "Ирина", "Александровна", '19.07.1984'),
			Person("Сергеева", "Раиса", "Ивановна", '23.04.1968'),
			Person("Алевсеев", "Ольга", "Сергеевна", '05.02.1978'),
			Person("Александрова", "Мария", "Алексеевна", '11.09.1979'),
			Person("Яковлева", "Инна", "Павловна", '27.10.1979')]

students = [Student("Иванов", "Александр", "Андреевич", '10.11.1998', class_rooms[0], [parents[0], parents[8]]),
			Student("Сидоров", "Петр", "Александрович", '10.01.2004', class_rooms[0], [parents[1], parents[9]]),
			Student("Андреева", "Анна", "Петровна", '12.11.1999', class_rooms[1], [parents[2], parents[10]]),
			Student("Петров", "Иван", "Александрович", '10.11.1999', class_rooms[1], [parents[3], parents[11]]),
			Student("Сергеев", "Сергей", "Иванович", '11.11.1999', class_rooms[2], [parents[4], parents[12]]),
			Student("Алевсеев", "Павел", "Сергеевич", '04.11.2003',  class_rooms[2], [parents[5], parents[13]]),
			Student("Александрова", "Инна", "Павловна", '03.11.1999', class_rooms[3], [parents[6], parents[14]]),
			Student("Яковлева", "Мария", "Алексеевна", '11.11.1999',  class_rooms[3], [parents[7], parents[15]])]

# 1. Получить полный список всех классов школы

print("Список всех классов школы:")
Class_room.class_room(class_rooms)

print()

# 2. Получить список всех учеников в указанном классе
#  (каждый ученик отображается в формате "Фамилия И.О.")

print("Список всех учеников класса")
Class_room.get_list_students(class_rooms[3])

print()

# 3. Получить список всех предметов указанного ученика
#  (Ученик --> Класс --> Учителя --> Предметы)


print('Cписок всех предметов ученика')
Teacher.sub(students[0])

print()

# 4. Узнать ФИО родителей указанного ученика

print('ФИО родителей ученика')
Student.parent(students[0])

print()

# 5. Получить список всех Учителей, преподающих в указанном классе

print('Список учителей в классе')
Teacher.teacher_in_class_rooms(class_rooms[3])

