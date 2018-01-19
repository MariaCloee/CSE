"""
Outline of Hangman
1. Make a word bank - 10 items
2. select random item from the list
3. Hide the word (use *)
4. Reveal letters if they have been guessed.
5. Create the win condition

"""
import random

turns_left = 10
word_bank = ["seal", "puppy", "hamster", "horse", "monkey", "dog", "unicorn", "red wolf", "duck", "whales", "cat"]
a_word = random.randint(0, 10)
print(word_bank[a_word])

str1 = (word_bank[a_word])
listOne = list(str1)
print(listOne)
listOne = "*"

