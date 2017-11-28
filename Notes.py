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
# print(100%3)
#
# # Variable
# car_name =  "Wiebe Mobile"
# car_type= "Lamborghini Sesto Elemento"
# car_cylinders = 8
# car_mpg = 9000.1
#
# # Inline Printing
# print("My car is the %s" % car_name)  # %s = insert and  %d = number
# print("My car is the %s. It is a %s." % (car_name,car_type))
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


def print_hw():
    print("Hello World")
    # 4 spaces = 1 indent (very important)


print_hw()


def say_hi(name):  # name is a "parameter"
    print("Hello %s." % name)
    print("I hope you have a fantastic day!")


say_hi("John")


def birthday(age):
    age += 1   # age = age + 1
    print(age)


say_hi("John")
print("John is 15. Next year:")
birthday(15)
