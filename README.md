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
  - For now, I have decided to constrain the problem such that the words must be at the end of the number i.e. **1-800-PAINTER** is acceptable but **1-800-PAINT37** is not. This makes the problem less complex and because the concept of a "wordified" phone number typically has the word at the end. This further simplifies the problem because there are no letters associated with "0" or "1" (based on standard cellphone keypad) so all words must occur after the right-most "0" and "1".