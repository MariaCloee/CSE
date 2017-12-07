# New python File: Warmups.py

# 12.4.17
#
# firstname = input("What is your first name? ")
# lastname = input("What is your last name? ")
# print("Hello %s %s." % (firstname, lastname))
# print("Hello %s %s." % (lastname, firstname))
#
#
# def reverse_order(first_name, last_name):
#     # print("%s %s" % (last_name, first_name))
#     print(last_name + " " + first_name)       # Concatenation
#
#
# reverse_order("Maria", "Garcia")
#
#
# def reverse_order():
#     first_name = input("What is your first name? ")
#     last_name = input("What is your last name? ")
#     print("%s %s" % (last_name, first_name))

#
# def happy_bday(name1):
#     print("Happy Birthday to You!. Happy Birthday to You! Happy Birthday Dear %s! Happy Birthday to You!" % name1)
#
#
# happy_bday("JOHN")

#
# def happy_bday(name):
#     print("Happy Birthday to You!. Happy Birthday to You!")
#     print("Happy Birthday Dear" + name)
#     print("Happy Birthday to You!")

#
# def add_py(name):
#     print("Hello %s.py" % name)
#
# add_py(name= )

#
# # this is 2 (num1, num2) and this is one (num1) and this is 0 ()
# def add(num1, num2, num3):  # these are 3 parameters (num1, num2, num3)
#     print(num1 + num2 + num3)
#
#
# add(90, 900, 9000)


# 12/7/17

def repeat(string):
    print(string)
    print(string)
    print(string)

    for x in range(3):
        print(string)


repeat("Hello")
