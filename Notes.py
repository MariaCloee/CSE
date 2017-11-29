# # # print("Hello World")
# # #
# # # # Maria Garcia
# # #
# # # print(3+5)
# # # print(5-3)
# # # print(5*3)
# # # print(6/2)
# # # print(3**2)   # 2 ** means to the power of and 1 * means multiply
# # #
# # # print()   # Creates a blank line
# # # print("See if you can figure this out")
# # # print(100%3)
# # #
# # # # Variable
# # # car_name =  "Wiebe Mobile"
# # # car_type= "Lamborghini Sesto Elemento"
# # # car_cylinders = 8
# # # car_mpg = 9000.1
# # #
# # # # Inline Printing
# # # print("My car is the %s" % car_name)  # %s = insert and  %d = number
# # # print("My car is the %s. It is a %s." % (car_name,car_type))
# # #
# # # # Taking input
# # # name = input("What is your name?")
# # # print("Hello %s." % name)
# # # # print(name)
# # #
# # # age = input("What is your age?")
# # # print("You are %s years old." % age)
# # #
# # # # Change the file
# #
# #
# # def print_hw():
# #     print("Hello World")
# #     # 4 spaces = 1 indent (very important)
# #
# #
# # print_hw()
# #
# #
# # def say_hi(name):  # name is a "parameter"
# #     print("Hello %s." % name)
# #     print("I hope you have a fantastic day!")
# #
# #
# # say_hi("John")
# #
# #
# # def birthday(age):
# #     age += 1   # age = age + 1
# #     print(age)
# #
# #
# # say_hi("John")
# # print("John is 15. Next year:")
# # birthday(15)
# #
# # # Press Ctrl-A = Select all and Ctrl-/ = to comment old code
# # # Press Ctrl-A and Ctrl-/ to select everything and comment everything
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
# Loops


# for num in range(5):
#     print(num + 1)

# for mystery in "Hello World":    # Don't use a blue word as the 'name'
#     print(mystery)

# a = 1
# while a < 10:
#     print(a)
#     a += 1

# response = ""
# while response != "Hello":  # ! = not
#     response = input("Say \\ \"Hello\"")   # \\ 2 of these = print the actual \ on the program

print("Hello \nWorld")   # \n means newline

import random   # imports should be at the top
print(random.randint(0, 6))
