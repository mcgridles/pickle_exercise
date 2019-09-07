# Pickle Robotics Exercise

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
- After completing `all_wordifications()`, `number_to_words()` just requires selecting one of the possible phone numbers output.

## Notes
- If you are looking for a much better implimentation of these functions, check out [callword](https://pypi.org/project/callword/), which is coincidentally written by a Pickle employee!
  - Full disclosure for all the Pickle employees, I didn't look at or use any `callword` source code, I just stumbled upon it while trying to figure out what constitutes a "wordified" phone number.
- After playing around with the `callword` library for a bit, it appears that it maps of all numbers with 2+ digits to their word equivalent using an English dictionary to check if the words are valid or not. Then, all three functions are most likely just lookup tables in one way or another. This makes things quick and easy once the `word_dict` hash map has been created but having to look up all those words that aren't relevant to the input phone number takes time so the benefits will really only be seen if you are interested in wordifying many phone numbers.