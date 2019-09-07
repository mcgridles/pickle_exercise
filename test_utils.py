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


if __name__ == '__main__':
	unittest.main()
