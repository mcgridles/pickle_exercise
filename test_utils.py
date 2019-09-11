import unittest

from utils import *


class TestUtils(unittest.TestCase):
	def setUp(self):
		self.valid_num = '1-800-724-6837'
		self.valid_word = '1-800-PAINTER'
		self.invalid_num = '800-724-683'
		self.invalid_word = '1-800-PAINT'
		self.invalid_character = '1-800-P@INTER'
		self.invalid_type = 18007246837

	def test_check_input_valid_input(self):
		output1 = check_input(self.valid_num)
		output2 = check_input(self.valid_word)

		self.assertEqual(output1, ('1', '8007246837'))
		self.assertEqual(output2, ('1', '800PAINTER'))

	def test_check_input_invalid_input(self):
		with self.assertRaises(TypeError):
			check_input(self.invalid_type)

		with self.assertRaises(ValueError):
			check_input(self.invalid_num)

		with self.assertRaises(ValueError):
			check_input(self.invalid_word)

		with self.assertRaises(ValueError):
			check_input(self.invalid_character)

	def test_switch(self):
		num1 = switch('a')
		num2 = switch('Z')
		letter = switch('3')

		self.assertEqual(num1, '2')
		self.assertEqual(num2, '9')
		self.assertEqual(letter, ['D', 'E', 'F'])

	def test_get_letters(self):
		number = '123470'

		letters = get_letters(number)

		self.assertCountEqual(letters, [
			[],
			['A', 'B', 'C'],
			['D', 'E', 'F'],
			['G', 'H', 'I'],
			['P', 'Q', 'R', 'S'],
			[]
		])

	def test_get_words(self):
		number = '228'
		letters = get_letters(number)

		words = get_words(letters)

		self.assertCountEqual(words, ['CAT', 'BAT', 'ACT'])

	def test_insert_words(self):
		words = ['CAT', 'BAT', 'ACT']
		number = '8002281234'
		start = 3
		end = 6

		wordified = insert_words(words, number ,start, end)

		self.assertCountEqual(wordified, [
			'800CAT1234',
			'800BAT1234',
			'800ACT1234'
		])

	def test_format_numbers(self):
		country_code = '1'
		wordified = ['800CAT1234', '800PAINTER', '800PAINT37', '8007246837', '8001A31234', 'CAT1231234']

		formatted = format_numbers(country_code, wordified)

		self.assertCountEqual(formatted, [
			'1-800-CAT-1234',
			'1-800-PAINTER',
			'1-800-PAINT-37',
			'1-800-724-6837',
			'1-800-1-A-3-1234',
			'1-CAT-123-1234'
		])


if __name__ == '__main__':
	unittest.main()
