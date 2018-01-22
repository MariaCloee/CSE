"""
Outline of Hangman
1. Make a word bank - 10 items
2. select random item from the list
3. Hide the word (use *)
4. Reveal letters if they have been guessed.
5. Create the win condition

"""
import random

letters_guessed = []
turns_left = 10
word_bank = ["seal", "puppy", "hamster", "horse", "monkey", "dog", "unicorn", "red wolf", "duck", "whales", "cat"]
a_word = random.randint(0, 10)
chosen = word_bank[a_word]

list_one = list(chosen)
print(list_one)
letters = word_bank[a_word]
# each turn
hashed_word = []
if letters != letters_guessed:


print(''.join(list_one))  # prints out the list for the user



