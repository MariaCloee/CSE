import random
# Maria Garcia

num = random.randint(1, 50)  # 50

turns_left = 5
right_guess = False

while turns_left > 0 and right_guess is False:
    num1 = int(input("Guess what number I am thinking of from 1-50? "))
    if num1 == num:
        print("YOU DID IT!")
        right_guess = True
    elif num1 < num:
        print("higher")
        turns_left -= 1
    elif num1 > num:
        print("lower")
        turns_left -= 1

if turns_left is 0:
    print("GOOD JOB!!! You tried your best, but here was the answer %s." % num)

# In order:
# Generate a number
# Get a number (input) from the user
# compare number to input
# Add a "higher" or "lower"
# add 5 guesses
