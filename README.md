# Pickle Robot Co. Exercises

## Dependencies
- Python3
- [PyEnchant](https://pypi.org/project/pyenchant/)

## Exercises
1. Write function `number_to_words()`, which takes as an argument a string representing a US phone number and which outputs a string which has transformed part or all of the phone number into a single "wordified" phone number that can be typed on a US telephone.
2. Write function `words_to_number()`, which does the reverse of `number_to_words()`
3. Write function `all_wordifications()`, which outputs all possible combinations of numbers and English words in a phone number.

## Approach
Initially, I define a "wordified" number to be a US phone number where some or all of the numbers have been used to make a word. Since the prompt is open ended I will constrain it slightly by saying the word must be at the end of the number i.e. **1-800-PAINTER** is acceptable but **1-800-PAINT-37** is not. This makes the problem less complex and because the concept of a "wordified" phone number typically has the word at the end (such as on advertisements). This further simplifies the problem because there are no letters associated with "0" or "1" (based on standard cellphone keypad) so all words must occur after the right-most "0" and "1".

After finishing all exercises, I went back and modified `all_wordifications()` to find words that don't always occur at the end of a phone number i.e. **1-800-PAINT-37** is now valid. This means *v1.2* is slower than *v1.1* because it searches through all possible subets of each number. While this does add overhead, because US phone numbers are always 10 digits (excluding country code), the overhead is constant for every phone number.

For the coding, I started with `words_to_number()` because it's essentially just a look-up table and thus the most straightforward. Then, I moved on to `all_wordifications()` because `number_to_words()` is a subset of that problem. Finally, `number_to_words()` just requires selecting one of the possible phone numbers from `all_wordifications()`.

### Possible Extensions

- The search space for `all_wordifications()` could be improved by looking up possible words as you go and ignoring letters that are not possible. For example, start with the first number **7** (as in **PAINTER**) for wich the first option is **P**. For the next number **2**, you can eliminate **B** and **C** as possible choices because there aren't any English words that start with **PB** or **PC**. From there, you are only looking for words that start with **PA** and so on. Depending on how long it takes to look up if there are any words that start with a certain set of letters this may not actually improve the efficiency time-wise.
- `number_to_words()` could be sped up by returning the first wordified phone number found, though this would not be able to take advantage of the implementation of `all_wordifications()` and would thus involve duplicating a lot of the code.

## Notes
- If you are looking for a library implimentation of these functions, check out [callword](https://pypi.org/project/callword/), which is coincidentally written by a Pickle employee!
  - Full disclosure for all the Pickle employees, I didn't look at or use any `callword` source code, I just stumbled upon it while trying to define what constitutes a "wordified" phone number.
- After playing around with the `callword` library for a bit, it appears that it maps of all numbers with 2+ digits to their word equivalent using an English dictionary to check if the words are valid or not. Then, all three functions are most likely just lookup tables in one way or another. This makes things quick and easy once the `word_dict` hash map has been created but having to look up all those words that aren't relevant to the input phone number takes time so the benefits will really only be seen if you are interested in wordifying many phone numbers. May be worth looking into.
- For all three exercises, a US phone number is considered to be the last 10 digits of the input, meaning the country code is the digits preceding the phone number if applicable. For `number_to_words()` and `all_wordifications()` the country code is not considered when wordifying.
- Some of the words found in the phone number don't seem like words to me but that is due to `PyEnchant` and the `Enchant` dictionary. This could be fixed by using a different dictionary library, though all dictionaries will most likely have their own quirks, or having a blacklist of "non-words". However, neither is all that necessary.