def check_input(num):
	"""
	Checks for valid input and raises exceptions if invalid.

	:param num: (str) -> US or wordified phone number
	:return: (str) -> US or wordified phone number with hyphens removed
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
