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
word_bank = ["Seal", "Puppy", "Hamster", "Horse", "Monkey", "Dog", "Unicorn", "Red wolf", "Duck", "Whales", "Cat"]
a_word = random.randint(0, 10)
chosen = word_bank[a_word]
points = 0

correct_letters = list(chosen)
letters = string.ascii_letters

# each turn
print("You have 10 tries to guess this word(might includes spaces and uppercase letter(s)) Good Luck. ")
print("If you can't do it, type 'quit' to stop.")

while turns_left > 0:
    list_form = []

    for letter in chosen:
        if letter.lower() in letters_guessed:
            # Show the letter
            list_form.append(letter)
        else:
            # Hide the letter
            list_form.append("*")

    new_str = ''.join(list_form)
    print(new_str)

    if list_form == correct_letters:
        print("Good Job! You guessed it!")
        exit(0)
    print("You have %d points." % points)
    guess = input("Guess a letter ").lower()
    if guess == 'quit':
        exit(0)
    letters_guessed.append(guess)
    if guess in chosen:
        points += 1
        print("YAY! You got it right!")
    else:
        turns_left -= 1
        print("Sorry, but that was wrong!")

if turns_left == 0:
    print("Good job, but the word was %s." % chosen)
    print("You ended with %d points." % points)
