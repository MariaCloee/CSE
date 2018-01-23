"""
Outline of Hangman
1. Make a word bank - 10 items
2. select random item from the list
3. Add user input to a list of letters_guessed
4. Build a list of letters to show, and display the string form
5. Create the win condition

"""
import random
import string


letters_guessed = []
turns_left = 10
word_bank = ["seal", "puppy", "hamster", "horse", "monkey", "dog", "unicorn", "red wolf", "duck", "whales", "cat"]
a_word = random.randint(0, 10)
chosen = word_bank[a_word]
the_right_guess = (random.choices(word_bank))

list_one = list(chosen)
print(list_one)
letters = string.ascii_letters

# each turn

# print(''.join(list_one))  # prints out the list for the user
# output =
while turns_left > 0:
    list_form = []

    # print(letters_guessed)
    for letter in chosen:
        if letter in letters_guessed:
            # Show the letter
            list_form.append(letter)
        else:
            # Hide the letter
            list_form.append("*")
    print(list_form)
    guess = input("Guess a letter")
    if guess == 'quit':
        exit(0)
    letters_guessed.append(guess)