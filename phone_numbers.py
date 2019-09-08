import itertools
import enchant

from utils import check_input, switch


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
		# Find the phone number with the longest word
		words = [w.split('-')[-1] for w in wordified]
		lengths = list(map(len, words))
		longest = max(lengths)

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


def all_wordifications(num, lang='en_US'):
	"""
	Outputs all combinations of English words and numbers in a phone number

	:param num: (str) -> Valid US phone number
	:param lang: (str) -> Enchant language code for dictionary
	:return: (list(str)) -> All possible combinations of English words and numbers in the phone number
	"""

	country_code, number = check_input(num)

	letter_candidates = []
	for n in number:
		if n == '0' or n == '1':
			# Words must be to the right of the right-most "0" and "1"
			# If "0" or "1" is encountered, reset list and continue
			letter_candidates = []
		else:
			# Keep list of possible letters for each position in the phone number
			letter_candidates.append(switch(n))

	dictionary = enchant.Dict(lang)  # Using PyEnchant for dictionary
	wordifications = []
	for permutation in itertools.product(*letter_candidates):
		for i in range(2, len(permutation)):  # Constrain to words >2 letters to avoid abbreviations (optional)
			word = ''.join(permutation[-i-1:])  # Work from back to front so words are only at the end of the number

			# PyEnchant seems to have some acronyms in its dictionary 
			# so only lowercase words are considered to avoid them
			if dictionary.check(word.lower()):
				wordified = number[:-i-1] + word

				# Add hyphens back into phone number
				hyphenated = country_code + '-' if country_code else ''
				for i in range(len(wordified)):
					if wordified[i+1].isalpha():
						hyphenated += wordified[i] + '-' + wordified[i+1:]
						break
					elif i in [3, 6]:
						hyphenated += '-'
					hyphenated += wordified[i]

				wordifications.append(hyphenated)

	return list(set(wordifications))
