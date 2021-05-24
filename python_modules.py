# # What are python Modules
# # We have  built in Modules that we can find on Python's Library
# # if the value is 1.49 floor() 1 ,  ceil()1.51 2
# # we have a keyword called import that we can use to call a module
#
# from random import random
# import math
#
# print(random())
# num1 = 23.66
# print(num1)
#
# # if the user input is >= .50 apply ceil() - use random() to generate a number
# # if the user input is <= .49 apply floor()
#
# print(math.ceil(num1))
# print(math.floor(num1))
# # what is the use case
# os , sys are used to get information about your localhost/your machine such as name, path etc
#
# import os, sys, datetime, math
#
# print(os.cpu_count())
# print(datetime.datetime.today())
#
# # % ? provides remainder value
# print(math.remainder(1, 5))








# working_dir = os.getcwd()
# print("This is your current working Dir " + working_dir)
# #
# system_path = sys.path
# print("This is the path " + str(system_path))
#
#
# def current_system_path():
#     print("This is your current path ")
#     return sys.path
# print(current_system_path())

















# from random import random
# import math
#
# num1 = random()
# print(num1)
# if num1 >= 0.5:
#     print(math.ceil(num1))
# else:
#     print(math.floor(num1))

# import os, sys
# def current_system_path():
#     print(" this is your current directory ")
#     return sys.path
#
# print(current_system_path())


# Lambda's work on the bases of lambda arguments : expression and in this case we're doing nothing more than name a variable to include a Lambda and although this works,
# Looks kinda pretty in one line, it's not a clean nor understandable way of writing code

def _add(num1, num2):
    return num1 + num2

# arguments:expression
addition = lambda num1, num2: num1 + num2 # calculating the expresstion

print("value returned by add() function")
print(add(2, 2))
print(" value returned using Lambda function ")
print(addition(7, 2))