import random
# Maria Garcia

num = random.randint(1, 50)  # 50
print(num)


response = ""
while response != num:
    response = int(input("Guess what number I am thinking of from 1-50? "))


num1 = int(input("Guess what number I am thinking of from 1-50? "))  #
if num1 == num:
    print("YOU DID IT!")
elif num1 < num:
    print("higher")
elif num1 > num:
    print("lower")


# In order:
# Generate a number
# Get a number (input) from the user
# compare number to input
# Add a "higher" or "lower"
# add 5 guesses
