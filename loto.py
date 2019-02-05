# coding: utf-8

__author__ = 'Введенская Алла'

"""
== Лото ==
Правила игры в лото.
Игра ведется с помощью специальных карточек, на которых отмечены числа,
и фишек (бочонков) с цифрами.
Количество бочонков — 90 штук (с цифрами от 1 до 90).
Каждая карточка содержит 3 строки по 9 клеток. В каждой строке по 5 случайных цифр,
расположенных по возрастанию. Все цифры в карточке уникальны. Пример карточки:
--------------------------
   9 43 62          74 90
2    27    75 78    82
  41 56 63     76      86
--------------------------
В игре 2 игрока: пользователь и компьютер. Каждому в начале выдается
случайная карточка.
Каждый ход выбирается один случайный бочонок и выводится на экран.
Также выводятся карточка игрока и карточка компьютера.
Пользователю предлагается зачеркнуть цифру на карточке или продолжить.
Если игрок выбрал "зачеркнуть":
    Если цифра есть на карточке - она зачеркивается и игра продолжается.
    Если цифры на карточке нет - игрок проигрывает и игра завершается.
Если игрок выбрал "продолжить":
    Если цифра есть на карточке - игрок проигрывает и игра завершается.
    Если цифры на карточке нет - игра продолжается.
 
Побеждает тот, кто первый закроет все числа на своей карточке.
Пример одного хода:
Новый бочонок: 70 (осталось 76)
------ Ваша карточка -----
6  7          49    57 58
  14 26     -    78    85
23 33    38    48    71
--------------------------
-- Карточка компьютера ---
7 87     - 14    11
     16 49    55 88    77
  15 20     -       76  -
--------------------------
Зачеркнуть цифру? (y/n)
Подсказка: каждый следующий случайный бочонок из мешка удобно получать
с помощью функции-генератора.
Подсказка: для работы с псевдослучайными числами удобно использовать
модуль random: http://docs.python.org/3/library/random.html
"""
import random
 
class Card:
	def __init__(self, row=3, column=9, nums_per_row=5, max_num=90):
		self._row = row
		self._column = column
		self._nums_per_row = nums_per_row
		self._max_num = max_num
 
class CommonCard(Card):
	counter = 0
	def __init__(self):
		Card.__init__(self, row=3, column=9, nums_per_row=5, max_num=90)
		self._title = ' '
		self._card = [['' for _ in range(self._column)] for _ in range(self._row)]
		self._nums = random.sample(range(1, self._max_num + 1), self._nums_per_row * self._row)
		self._pixels = self._column * 3 - 1
		self._nums_for_game = self._nums[:]
		 
	@property
	def nums(self):
		return len(self._nums_for_game)
 
	def _header(self):
		return '{:-^{}}'.format(self._title, self._pixels)
 
	def _mapping_card(self):
		for row in self._card:
			while row.count(True) != self._nums_per_row:
				i = random.randrange(self._column)
				if not row[i]:
					row[i] = True
 
	def _filling_card_with_numbers(self):
		for i, row in enumerate(self._card):
			tmp = sorted(self._nums[i * self._nums_per_row:(i + 1) * self._nums_per_row], reverse=True)
			for j, item in enumerate(row):
				if item:
					self._card[i][j] = tmp.pop()
 
	def __str__(self):
		res = list()
		res.append(self._header())
		for row in self._card:
			res.append(' '.join(['{:<2}'.format(x) for x in row]))
		res.append('-' * self._pixels)
		return '\n'.join(res)
 
 
	def modify_card(self, num):
		i = int(self._nums.index(num) / self._nums_per_row)
		self._card[i][self._card[i].index(num)] = '-'
		self._nums_for_game.remove(num)
 
	def check_num(self, num):
		return num in self._nums
 
	def create_card(self):
		self._mapping_card()
		self._filling_card_with_numbers()
 
class PlayerCard(CommonCard):
	def __init__(self, row=3, column=9, nums_per_row=5, max_num=90):
		CommonCard.__init__(self)
		self._title = ' Ваша карточка '

 
class ComputerCard(CommonCard):
	def __init__(self, row=3, column=9, nums_per_row=5, max_num=90):
		CommonCard.__init__(self)
		self._title = ' Карточка компьютера '

 
class Game(Card):
	def __init__(self):
		Card.__init__(self, row=3, column=9, nums_per_row=5, max_num=90)
		self._unit = None
		self._computer = None
 

	def _create_cards(self):
		self._unit.create_card()
		self._computer.create_card()
 
	def _init_game(self):
		self._unit = PlayerCard()
		self._computer = ComputerCard()
		self._create_cards()

 
	def _get_random_num(self):
		random_numbers = random.sample(range(1, self._max_num + 1), self._max_num)
		for i in random_numbers:
			yield i, self._max_num - random_numbers.index(i) - 1
 
	def _check_answer(self, unit, num, answer):
		if answer != 'y' and answer != 'n':
			self._check_answer(unit, num, input('Зачеркнуть цифру? (y/n) = '))
		elif answer == 'y' and unit.check_num(num):
			unit.modify_card(num)
			return 0
		elif answer == 'n' and not unit.check_num(num):
			return 0
		elif answer == 'y' and not unit.check_num(num):
			print(f'Боченка {num} нет на вашей карточке.')
			return 1
		elif answer == 'n' and unit.check_num(num):
			print(f'Боченок {num} на есть вашей карточке.')
			return 1
		else:
			print('Что-то пошло не так', answer)
			return 1
 
	def _clean(self):
		del self._unit
		del self._computer
 
	def _lets_play(self):
		num_generator = self._get_random_num()
		gen_res = next(num_generator)
		num = gen_res[0]
		left = gen_res[1]
		
		try:
			while self._unit.nums and self._computer.nums:
				print(f'Новый бочонок: {num} (осталось {left})')
				print(self._unit)
				print(self._computer)
			
				if self._check_answer(self._unit, num, input('Зачеркнуть цифру? (y/n) = ')):
					return 'К сожалению, вы проиграли.'
				else:
					if self._computer.check_num(num):
						self._computer.modify_card(num)
			
				gen_res = next(num_generator)
				num = gen_res[0]
				left = gen_res[1]
			
			if not self._unit.nums and not self._computer.nums:
				return 'Ничья!'
			elif self._computer.nums:
				return 'Поздравляем, Вы победили!'
			else:
				return 'Компьютер успел первым. Попробуйте еще раз.'

		except StopIteration:
			return 'У нас закончились бочонки, все проиграли!'

	def main(self):
		while True:
			answer = input('Сыграем в лото? (y/n) = ')
			if answer == 'y':
				self._init_game()
				print(self._lets_play())
				self._clean()
			elif answer == 'n':
				print('До свидания!')
				return
 
if __name__ == '__main__':
	game = Game()
	game.main()
