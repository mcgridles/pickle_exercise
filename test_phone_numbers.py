import unittest

from phone_numbers import *


class TestPhoneNumbers(unittest.TestCase):
	def setUp(self):
		self.test_num1 = '1-800-724-6837'
		self.test_word1 = '1-800-PAINTER'

	def test_number_to_words_valid_number(self):
		word_output = number_to_words(self.test_num1)

		self.assertTrue(type(word_output) is str)
		self.assertEqual(word_output, self.test_word1)

	def test_words_to_number_valid_number(self):
		number_output = words_to_number(self.test_word1)

		self.assertTrue(type(number_output) is str)
		self.assertEqual(number_output, self.test_num1)

	def test_all_wordification_valid_number(self):
		word_output = all_wordifications(self.test_num1)

		self.assertTrue(type(word_output) is list)
		self.assertTrue(len(word_output) > 0)
		self.assertTrue(type(word_output[0]) is str)
		self.assertTrue('1-800-PAINTER' in word_output)
		self.assertTrue('1-800-PAINT-37' in word_output)
		self.assertTrue('1-800-PAIN-837' in word_output)
		self.assertTrue('1-800-SAINT-37' in word_output)
		self.assertTrue('1-800-72-HOVER' in word_output)


if __name__ == '__main__':
	unittest.main()
