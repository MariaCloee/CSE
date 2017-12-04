import random
# Maria Garcia

print(random.randint(1, 50))

num = random.randint

num1 = input("Guess what number I am thinking of from 1-50? ")


response = ""
while response != num:
    response = input("Guess what number I am thinking of from 1-50?)

# In order:
# Generate a number
# Get a number (input) from the user
# compare number to input
# Add a "higher" or "lower"
# add 5 guesses
