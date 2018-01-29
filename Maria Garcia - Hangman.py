import random
import string
import time

level = input("Do you want easy or hard level? ")
if level == "easy":
    letters_guessed = []
    turns_left = 10
    word_bank = ["Seal", "Puppy", "Hamster", "Horse", "Monkey", "Dog", "Unicorn", "Red wolf", "Duck", "Whales", "Cat"]
    a_word = random.randint(0, 10)
    chosen = word_bank[a_word]
    points = 0

    correct_letters = list(chosen)
    letter = string.ascii_letters

    # each turn
    print("You have 10 tries to guess this word(might includes spaces and uppercase letter(s)) Good Luck. ")
    print("Hint: It is all animals!")
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
            print("You got %d points." % points)
            exit(0)
        print("You have %d points." % points)
        guess = input("Guess a letter ").lower()
        if guess == 'quit':
            print("The word was: %s." % chosen)
            print("You still had %d turns left!" % turns_left)
            exit(0)
        if guess == "":
            turns_left -= 1
            print("You have to guess something!")
            print("You have %d turns left." % turns_left)
        elif guess in letters_guessed:
            print("You already guessed that letter. No point.")
        elif guess in chosen.lower():
            points += 1
            print("YAY! You got it right!")
            print("You have %d turns left." % turns_left)
        else:
            turns_left -= 1
            print("Sorry, but that was wrong!")
            print("You have %d turns left." % turns_left)
        letters_guessed.append(guess)

    if turns_left == 0:
        print("Good job, but the word was %s." % chosen)
        print("You ended with %d points." % points)


if level == "hard":
    letters_guessed = []
    turns_left = 5
    word_bank = ["moral", "peace", "grand", "will", "meal", "cart", "lamb", "free", "loose", "interrupt", "colleague",
                 "unanimous", "dynamic", "crack", "stress", "wording", "feather", "teach", "band"]
    a_word = random.randint(0, 10)
    chosen = word_bank[a_word]
    points = 0

    correct_letters = list(chosen)
    letter = string.ascii_letters

    # each turn
    print("You have 5 tries to guess this word(might includes spaces) Good Luck. ")
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
            print("You got %d points." % points)
            exit(0)
        print("You have %d points." % points)
        guess = input("Guess a letter ").lower()
        if guess == 'quit':
            print("The word was: %s." % chosen)
            print("You still had %d turns left!" % turns_left)
            exit(0)
        if guess == "":
            turns_left -= 1
            print("You have to guess something!")
            print("You have %d turns left." % turns_left)
        elif guess in letters_guessed:
            print("You already guessed that letter. No point.")
        elif guess in chosen.lower():
            points += 1
            print("YAY! You got it right!")
            print("You have %d turns left." % turns_left)
        else:
            turns_left -= 1
            print("Sorry, but that was wrong!")
            print("You have %d turns left." % turns_left)
        letters_guessed.append(guess)

    if turns_left == 0:
        print("Good job, but the word was %s." % chosen)
        print("You ended with %d points." % points)