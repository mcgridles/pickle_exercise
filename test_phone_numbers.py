import unittest

from phone_numbers import *


class TestPhoneNumbers(unittest.TestCase):
	def setUp(self):
		self.test_num1 = '1-800-724-6837'
		self.test_word1 = '1-800-PAINTER'

	def test_number_to_words_valid_number(self):
		word_output = number_to_words(self.test_num1)
		possible_ouput = [
			'1-800-72-INTER',
			'1-800-72-HOVER',
			'1-800-PAINTER',
			'1-800-724-OVER',
			'1-800-724-MUDS',
		]

		self.assertTrue(type(word_output) is str)
		self.assertTrue(word_output in possible_ouput)

	def test_words_to_number_valid_number(self):
		number_output = words_to_number(self.test_word1)

		self.assertTrue(type(number_output) is str)
		self.assertEqual(number_output, self.test_num1)

	def test_all_wordification_valid_number(self):
		word_output = all_wordifications(self.test_num1)

		self.assertTrue(type(word_output) is list)
		self.assertTrue(len(word_output) > 0)
		self.assertTrue(type(word_output[0]) is str)
		self.assertCountEqual(word_output, [
			'1-800-72-INTER',
			'1-800-72-HOVER',
			'1-800-PAINTER',
			'1-800-724-OVER',
			'1-800-724-MUDS',
		])


class TestUtils(unittest.TestCase):
	def setUp(self):
		self.valid_num = '1-800-724-6837'
		self.valid_word = '1-800-PAINTER'
		self.invalid_num = '1-800-7245-6837'
		self.invalid_word = '1-800-PAINTERS'
		self.invalid_character = '1-800-P@INTER'
		self.invalid_type = 18007246837

	def test_check_input_valid_input(self):
		num = check_input(self.valid_num)
		word = check_input(self.valid_word)

		self.assertEqual(num, '18007246837')
		self.assertEqual(word, '1800PAINTER')

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


if __name__ == '__main__':
	unittest.main()
