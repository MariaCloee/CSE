# import random   # imports should be at the top
#
# print("Hello World")
#
# # Maria Garcia
#
# print(3+5)
# print(5-3)
# print(5*3)
# print(6/2)
# print(3**2)   # 2 ** means to the power of and 1 * means multiply
#
# print()   # Creates a blank line
# print("See if you can figure this out")
# print(100 % 3)
#
# # Variable
# car_name = "Wiebe Mobile"
# car_type = "Lamborghini Sesto Elemento"
# car_cylinders = 8
# car_mpg = 9000.1
#
# # Inline Printing
# print("My car is the %s" % car_name)  # %s = insert and  %d = number
# print("My car is the %s. It is a %s." % (car_name, car_type))
#
# # Taking input
# name = input("What is your name?")
# print("Hello %s." % name)
# # print(name)
#
# age = input("What is your age?")
# print("You are %s years old." % age)
#
# # Change the file
#
#
# def print_hw():
#     print("Hello World")
#     # 4 spaces = 1 indent (very important)
#
#
# print_hw()
#
#
# def say_hi(name1):  # name is a "parameter"
#     print("Hello %s." % name1)
#     print("I hope you have a fantastic day!")
#
#
# say_hi("John")
#
#
# def birthday(age1):
#     age1 += 1   # age = age + 1
#     print(age1)
#
#
# say_hi("John")
# print("John is 15. Next year:")
# birthday(15)
#
# # Press Ctrl-A = Select all and Ctrl-/ = to comment old code
# # Press Ctrl-A and Ctrl-/ to select everything and comment everything
#
#
# def f(x):
#     return x**5 + 4 * x**4 - 17*x**2 + 4
#
#
# print(f(3))
# print(f(3) + f(5))
#
# # If statements
#
#
# def grade_calc(percentage):
#     if percentage >= 90:
#         return "A"
#     elif percentage >= 80:  # Else if = elif
#         return "B"
#     elif percentage >= 70:
#         return "C"
#     elif percentage >= 60:
#         return "D"
#     else:
#         return "F"
#
# # Loops
#
#
# for num in range(5):
#     print(num + 1)
#
# for mystery in "Hello World":    # Don't use a blue word as the 'name'
#     print(mystery)
#
# a = 1
# while a < 10:
#     print(a)
#     a += 1
#
# response = ""
# while response != "Hello":  # ! = not
#     response = input("Say \"Hello\"")   # \\ 2 of these = print the actual \ on the program
#
# print("Hello \nWorld")   # \n means newline
#
#
# print(random.randint(0, 6))
#
#
# # Comparisons
# print(1 == 1)   # Two equal signs to compare
# print(1 != 2)    # One is not euqal to 2
# print(not False)    # This prints True
# print(1 == 1 and 4 <= 5)
# print(1 < 0 or 5 > 1)
#
#
# # Recasting
# c = '1'
# print(c == 1)   # False - C is a String, 1 is an int
# print(int(c) == 1)    # True - Compares two ints
# print(c == str(1))    # True - Compares two strings
#
#
# num = input("Give me a number")
# # Inputs are ALWAYS (!!!!!!!!!) of type string
#

# Lists
#
# the_count = [1, 2, 3, 4, 5]
# characters = ["graves", "Dory", "Boots", "Dora", "Shrek", "Obi-wan", "Carl"]
# print(characters[0])
# print(characters[4])
#
# print(len(characters))   # Gives you the length of the list
#
# #  Going through Lists
# for char in characters:
#     print(char)
# for cou in the_count:
#     print(cou**2)
#
# len(characters)
# range(3)     # Make a list of the numbers from 0 to 2
# range(len(characters))  # Makes a list of ALL INDICES
#
# for num in range(len(characters)):
#     char = characters[num]
#     print("The character at index %d is %s." % (num, char))
#
# str1 = "Hello World!"
# listOne = list(str1)
# print(listOne)
# listOne[11] = '.'
# print(listOne)
# newStr = "".join(listOne)
# print(newStr)
# print(listOne[-5])
#
# # adding stuff to a list
# characters.append("Iron man/Batman/whomever you want")
# print(characters)
#
# characters.append("Nemo")
# print(characters)
#
# # removing things from a list
# characters.remove("Carl")
# print(characters)
#
# characters.pop(6)
# print(characters)

# the string class
# import string
# print(string.ascii_letters)
# print(string.ascii_letters)
# print(string.digits)
# print(string.punctuation)
#
# strTwo = 'ThIs sEntENcE iS uNuSuAL'
# lowercase = strTwo.lower()
# print(lowercase)
#

# Dictionaries - Make upi a key: value pair
dictionary = {'name': 'Lance', 'age': 18, 'height': 6 * 12 + 2}

# Accessing from a dictionary
print(dictionary['name'])
print(dictionary['age'])
print(dictionary['height'])


# Adding to a dictionary
dictionary["eye colour"] = "blue"
dictionary["toilet paper"] = True
print(dictionary)


large_dictionary = {
    "California": "CA",
    "Michigan": "MI",
    "Florida": "FL"
}
print(large_dictionary["Florida"])

larger_dictionary = {
    "California": [
        "Fresno",
        "Sacramento",
        "Los Angles"
    ],
    "Washington": [
        "Seattle",
        "Tacoma",
        "Olympia",
        "Spokane"
    ],
    "Illinois": [
        "Chicago",
        "Naperville",
        "Peoria"
    ]
}

print(larger_dictionary["Illinois"])
print(larger_dictionary["Illinois"][0])
print(larger_dictionary["Washington"][3])

largest_dictionary = {
    "CA": {
        'NAME': 'California',
        'POPULATION': 39250000,
        'BORDER ST': [
            'Oregon',
            "Nevada",
            "Arizona"
        ]
    },
    "MI": {
        "NAME": "Michigan",
        "POPULATION": 9928000,
        "BORDER ST": [
            'Wisconsin',
            'Ohio',
            "Indiana"
        ]
    },
    "FL": {
        "NAME": "Florida",
        "POPULATION": 20610000,
        "BORDER ST": [
            'Georgia',
            'Alabama'
        ]
    }
}
print(largest_dictionary["MI"]["BORDER ST"][1])
print(largest_dictionary["FL"]["NAME"])
print(largest_dictionary["MI"]["NAME"])
