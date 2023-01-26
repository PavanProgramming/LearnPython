#
# def hello_func(greeting, name='You'):
#     return '{}, {}'.format(greeting, name)
#
# print(hello_func('Hi'))
# print(hello_func('Hi', name= 'pavan'))
#
#
# # def function_name(*args, **kwargs):
# # *args (Non-Keyword Arguments)
# # **kwargs (Keyword Arguments)
#
# # *args:
# # We use the “wildcard” or “*” notation like
# # this – *args OR **kwargs – as our function’s argument
# # when we have doubts about the number of  arguments we should pass in a function.
# #
# # *args allows you to do is take in more arguments than the number of formal arguments
# # that you previously defined. With *args, any number of extra arguments can be tacked
# # on to your current formal parameters (including zero extra arguments)
# def myfun1(arg1, *argv):
#     print("First argument :", arg1)
#     for arg in argv:
#         print("Next argument through *argv :", arg)
#
#
# myfun1('Hello', 'Welcome', 'to', 'India')
#
#
# # **kwargs: keyword arguments
# # **kwargs in function definitions in python is used to pass a keyworded, variable-length argument list.
# # A keyword argument is where you provide a name to the variable as you pass it into the function.
# # One can think of the kwargs as being a dictionary that maps each keyword to the value that we pass alongside it.
# # That is why when we iterate over the kwargs there doesn’t seem to be any order in which they were printed out.
# def myfun2(arg1, **kwargs):
#     for key, value in kwargs.items():
#         print("%s == %s" % (key, value))
#
#
# myfun2('Hi', first='Hello', mid='welcome', last='Good')
#
#
# def myfun3(arg1, arg2, arg3):
#     print("arg1:", arg1)
#     print("arg2:", arg2)
#     print("arg3:", arg3)
#
#
# # Now we can use *args or **kwargs to
# # pass arguments to this function :
# arg = ("Hello", "welcome to", "India")
# myfun3(*arg)
#
# kwarg = {"arg1": "Hello", "arg2": "welcome to", "arg3": 10}
# myfun3(**kwarg)
#
#
# def student_info(*args, **kwargs):
#     print(args)
#     print(kwargs)
#
#
# # student_info("hello", "pavan", subjects = ['math', 'science'], age = 30)
# details = ["hello", "pavan"]
# info = {'subjects': ['math', 'science'], 'age': 30}
# student_info(details, info)
# student_info(*details, **info)  # unpacking details and info


# functions advanced: In Python, functions are first class objects which means that
# functions in Python can be used or passed as arguments.
#
# Properties of first class functions:
# A function is an instance of the Object type.
# You can store the function in a variable.
# You can pass the function as a parameter to another function.
# You can return the function from a function.
# You can store them in data structures such as hash tables, lists, …

#  we have assigned the function shout to a variable. This will not call the function
#  instead it takes the function object referenced by a shout and creates a second name pointing to it, yell.
def shout(text):
    return text.upper()


print(shout('Hello'))
yell = shout
print(yell('Hello'))
print(id(yell))
print(id(shout))
print(dir(yell))
print(yell.__name__)
print(shout.__name__)


# the greet function takes another function as a parameter (shout and whisper in this case).
# The function passed as an argument is then called inside the function greet.

# Python program to illustrate functions
# can be passed as arguments to other functions


def ch_upper(text):
    return text.upper()


def ch_lower(text):
    return text.lower()


def greet(func):
    # storing the function in a variable
    greeting = func("""Hi, I am created by a function passed as an argument.""")
    print (greeting)

greet(ch_upper)
greet(ch_lower)


#   we have created a function inside of another function and then have returned the function created inside.

# Python program to illustrate functions
# Functions can return another function

def create_adder(x):
    def adder(y):
        return x+y

    return adder

add_15 = create_adder(15)

print(add_15(10))


