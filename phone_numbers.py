import itertools

from utils import *


def number_to_words(num):
	"""
	Transforms all or part of a US phone number into a "wordified" phone number.

	Ex.
		"1-800-724-6837" -> "1-800-PAINTER"

	:param num: (str) -> Valid US phone number
	:return: (str) -> US phone number containing a combination of numbers and a word
	"""

	# Generate all possible wordifications
	wordified = all_wordifications(num)

	if not wordified:
		# If no possible wordified numbers, return original number
		return num
	else:
		# Split numbers into sections by hyphens
		split_numbers = [w.split('-') for w in wordified]

		# Filter out all but the wordified part of each phone number
		words = list(map(lambda x: list(filter(lambda y: not y.isdigit(), x))[0], split_numbers))

		# Find the length of the longest wordified section
		lengths = list(map(len, words))  
		longest = max(lengths)

		# Return wordified number with longest wordified section
		return wordified[lengths.index(longest)]


def words_to_number(wordified):
	"""
	Transforms a "wordified" phone number into a valid US phone number.

	Ex. 
		"1-800-PAINTER" -> "1-800-724-6837"

	:param wordified: (str) -> US phone number containing a combination of numbers and a word
	:return: (str) -> Valid US phone number
	"""

	country_code, wordified = check_input(wordified)

	num = country_code + '-' if country_code else ''
	for i, w in enumerate(wordified):
		# Add hyphens in correct place
		if i in [3, 6]:
			num += '-'

		if w.isalpha():
			num += switch(w)
		else:
			num += w

	return num


def all_wordifications(num, lang='en_US', abbr=False):
	"""
	Outputs all combinations of English words and numbers in a phone number

	:param num: (str) -> Valid US phone number
	:param lang: (str) -> Enchant language code for dictionary
	:return: (list(str)) -> All possible combinations of English words and numbers in the phone number
	"""

	country_code, number = check_input(num)
	wordifications = []

	# Use itertools.combinations() and a range to return all possible subsets of the phone number
	for start, end in itertools.combinations(range(len(number) + 1), 2):
		# Skip strings of length 1 or length 2 (if abbreviations are not wanted)
		if not abbr and end - start < 3:
			continue
		elif end - start < 2:
			continue

		subset = number[start:end]

		# Substrings with "0" or "1" contain spaces or invalid characters so they should be skipped
		if '0' in subset or '1' in subset:
			continue

		letters = get_letters(subset)  # Look-up all possible letters for the string of numbers
		words = get_words(letters, lang)  # Find all valid English words from possible letters
		wordify = insert_words(words, number, start, end)  # Insert words into phone numbers

		wordifications.extend(wordify)

	# Remove duplicates and format phone numbers
	wordifications = list(set(wordifications))
	wordifications = format_numbers(country_code, wordifications)

	return wordifications
