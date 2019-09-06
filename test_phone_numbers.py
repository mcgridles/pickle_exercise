import unittest

from phone_numbers import number_to_words, words_to_number, all_wordification


class TestPhoneNumberManipulations(unittest.TestCase):

	def setUp(self):
		self.test_num1 = "1-800-724-6837"
		self.test_word1 = "1-800-PAINTER"

		self.invalid_num = "1-800-7245-6837"
		self.invalid_word = "1-800-PAINTERS"
		self.invalid_type = 18007246837

	def test_number_to_words_valid_number(self):
		word_output = number_to_words(self.test_num1)

		self.assertTrue(type(word_output) is str)
		self.assertEqual(word_output, self.test_word1)

	def test_number_to_words_invalid_number(self):
		with self.assertRaises(ValueError):
			number_to_words(self.invalid_num)

	def test_number_to_words_invalid_input_type(self):
		with self.assertRaises(TypeError):
			number_to_words(self.invalid_type)

		with self.assertRaises(TypeError):
			number_to_words(None)

	def test_words_to_number_valid_number(self):
		number_output = words_to_number(self.test_word1)

		self.assertTrue(type(number_output) is str)
		self.assertEqual(number_output, self.test_num1)

	def test_words_to_number_invalid_number(self):
		with self.assertRaises(ValueError):
			words_to_number(self.invalid_word)

	def test_number_to_words_invalid_input_type(self):
		with self.assertRaises(TypeError):
			words_to_number(self.invalid_type)

		with self.assertRaises(TypeError):
			words_to_number(None)

	def test_all_wordification_valid_number(self):
		word_output = all_wordification(self.test_num1)

		self.assertTrue(type(word_output) is list)
		self.assertTrue(len(word_output) > 0)
		self.assertTrue(type(word_output[0]) is str)
		# TODO: add assertEqual

	def test_all_wordification_invalid_number(self):
		with self.assertRaises(ValueError):
			all_wordification(self.invalid_num)

	def test_all_wordification_invalid_input_type(self):
		with self.assertRaises(TypeError):
			all_wordification(self.invalid_type)

		with self.assertRaises(TypeError):
			all_wordification(None)
