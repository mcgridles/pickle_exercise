import itertools
import enchant


def check_input(num):
	"""
	Checks for valid input and raises exceptions if invalid.

	:param num: (str) -> US or wordified phone number
	:return: (str) -> Phone country code
			 (str) -> US or wordified phone number with hyphens removed
	"""

	# Check type
	try:
		assert(type(num) is str)
	except AssertionError:
		raise TypeError('Phone number is not a string.')

	num = ''.join([n.upper() for n in num.split('-')])  # Remove hyphens

	# Check length is correct
	try:
		assert(len(num) >= 10)
	except AssertionError:
		raise ValueError('Invalid number containing {} digits.'.format(len(num)))

	# Check for invalid characters
	for n in num:
		if not (n.isnumeric() or n.isalpha()):
			raise ValueError('Invalid characters in phone number.')

	number = num[-10:]   # Last 10 digits are US phone number
	country = num[:-10]  # Remaning digits are considered country code

	return country, number


def switch(n):
	"""
	Switch between letters and numbers using traditional keypad associations.

	:param n: (str) -> Letter or number
	:return: (Union{str, list(str)}) -> Single number or list of possible letters
	"""

	keypad = {
		'1': [],
		'2': ['A', 'B', 'C'],
		'3': ['D', 'E', 'F'],
		'4': ['G', 'H', 'I'],
		'5': ['J', 'K', 'L'],
		'6': ['M', 'N', 'O'],
		'7': ['P', 'Q', 'R', 'S'],
		'8': ['T', 'U', 'V'],
		'9': ['W', 'X', 'Y', 'Z'],
		'0': []
	}

	if n.isalpha():
		# Look for letter in lists
		for k, v in keypad.items():
				if n.upper() in v:
					return k
	else:
		# Return list with possible letters
		return keypad[n]


def get_letters(number):
	"""
	Get all possible letters for each number in the substring.

	:param number: (str) -> Digits forming a subset of a US phone number
	:return: (list(list(str))) ->  Lists of possible letters for each number
	"""

	return list(map(switch, number))


def get_words(letters, lang='en_US'):
	"""
	Find all valid words that can be made from the given letters.

	:param letters: (list(list(str))) -> Lists of possible letters for each number
	:param lang: (str) -> Enchant language code for dictionary
	:return: (list(str)) -> All valid words formed from subset
	"""

	all_words = []
	dictionary = enchant.Dict(lang)  # Using PyEnchant for dictionary

	# Iterate through all permutations of letters using itertools.product()
	for permutation in itertools.product(*letters):
		word = ''.join(permutation)  # Join letters to create word

		# Check word against dictionary and add to list if valid.
		# Words are checked in lowercase to avoid abbreviations and acronyms that are valid in uppercase
		if dictionary.check(word.lower()):
			all_words.append(word)

	return all_words


def insert_words(words, number, start, end):
	"""
	"Wordify" subset of US phone number by replacing numbers with letters.

	:param words: (list(str)) -> All valid words formed from subset
	:param number: (str) -> Valid US phone number
	:param start: (int) -> Starting index of subset
	:param end: (int) -> Ending index of subset
	:return: (list(str)) -> All wordified numbers for subset
	"""

	wordifications = []
	for w in words:
		# Concatenate number and wordified subset
		wordify = number[:start] + w + number[end:]
		wordifications.append(wordify)

	return wordifications


def format_numbers(country_code, numbers):
	"""
	Correctly format US phone numbers with hyphens.

	:param country_code: (str) -> Phone country code
	:param numbers: (list(str)) -> All wordified numbers
	:return: (list(str)) -> Wordified and formatted phone numbers
	"""

	for i in range(len(numbers)):
		formatted = ''
		in_word = False

		for j in range(len(numbers[i])):
			if numbers[i][j].isalpha() and j == 0:
				# A hyphen will have already been added after the country code
				# so skip hyphens at index 0
				in_word = True
			elif numbers[i][j].isalpha() and not in_word:
				# Place hyphens before "wordified" sections
				in_word = True
				formatted += '-'
			elif numbers[i][j].isnumeric() and in_word:
				# Place hyphen after "wordified" sections
				in_word = False
				formatted += '-'
			elif j in [3, 6] and not in_word:
				# Place hyphens at correct place for standard US phone number
				formatted += '-'

			formatted += numbers[i][j]  # Add current digit/letter to number

		numbers[i] = country_code + '-' + formatted  # Concetenate country code on the front

	return numbers
