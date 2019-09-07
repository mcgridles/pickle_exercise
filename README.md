# Pickle Robot Co. Exercises

## Dependencies
- Python3
- [PyEnchant](https://pypi.org/project/pyenchant/)

## Exercises
1. Write function `number_to_words()`, which takes as an argument a string representing a US phone number and which outputs a string which has transformed part or all of the phone number into a single "wordified" phone number that can be typed on a US telephone.
2. Write function `words_to_number()`, which does the reverse of `number_to_words()`
3. Write function `all_wordifications()`, which outputs all possible combinations of numbers and English words in a phone number.

## Approach
- Starting with `words_to_number()` because it's essentially just a look-up table and thus the most straightforward. 
- Next doing `all_wordifications()` because `number_to_words()` is a subset of that problem.
  - Starting with brute force method and refining later. 
  - Convert all numbers to letters, use `itertools.product()` to create all possible permutations; search through them for English words.
  - For now, I will constrain the problem such that the words must be at the end of the number i.e. **1-800-PAINTER** is acceptable but **1-800-PAINT37** is not. This makes the problem less complex and because the concept of a "wordified" phone number typically has the word at the end. This further simplifies the problem because there are no letters associated with "0" or "1" (based on standard cellphone keypad) so all words must occur after the right-most "0" and "1".
- `number_to_words()` just requires selecting one of the possible phone numbers from `all_wordifications()`.

- Possible extensions/improvements that I may or may not make:
  - The search space for `all_wordifications()` could be improved by looking up possible words as you go and ignoring letters that are not possible. For example, start with the first number **7** (as in **PAINTER**) for wich the first option is **P**. For the next number **2**, you can eliminate **B** and **C** as possible choices because there aren't any English words that start with **PB** or **PC**. From there, you are only looking for words that start with **PA** and so on. Depending on how long it takes to look up if there are any words that start with a certain set of letters this may not actually improve the efficiency time-wise.
  - `number_to_words()` could be sped up by returning the first wordified phone number found, though this would not be able to take advantage of the implementation of `all_wordifications()` and would thus involve duplicating a lot of the code.
  - Extend the current definition of a wordified phone number to include words not just at the end of the phone number. This is a "all substrings in a string" type of problem so there may be a pretty efficient way to do it.

## Notes/Thoughts
- If you are looking for a much better implimentation of these functions, check out [callword](https://pypi.org/project/callword/), which is coincidentally written by a Pickle employee!
  - Full disclosure for all the Pickle employees, I didn't look at or use any `callword` source code, I just stumbled upon it while trying to figure out what constitutes a "wordified" phone number.
- After playing around with the `callword` library for a bit, it appears that it maps of all numbers with 2+ digits to their word equivalent using an English dictionary to check if the words are valid or not. Then, all three functions are most likely just lookup tables in one way or another. This makes things quick and easy once the `word_dict` hash map has been created but having to look up all those words that aren't relevant to the input phone number takes time so the benefits will really only be seen if you are interested in wordifying many phone numbers. May be worth looking into.