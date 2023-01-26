#  decorators: function decorators and class decorators


# function decorators : is a function that takes another function as argument and extends
# the behavior of this function without explicitly modifying it so in other
# words it allows you to add new functionality to an existing function

# @mydeco
# def dosomething():
#     pass

# in the above case the functionality of dosomething function is extended using mydeco decorator

# to understand this concept we have to know that functions in Python are first-class objects
# this means that like any other object they can be defined inside another function passed as an argument
# to another function and even returned from other function
#
# def temp_decorator(func):
#     def wrapper():  # should have same no. of arguments as func so we can use args, kwargs
#         print('starting decorator')
#         func()
#         print('Ending decorator')
#     return wrapper
#
#
# @temp_decorator    # equivalent to print_name = temp_decorator(print_name)
# def print_name():
#     print('Hai')
#
#
# # # Model-1
# # print_name = temp_decorator(print_name)  # if we are not mentioning @temp_decorator above print_name function
# # print_name()  # it will call the temp_decorator function
#
# # Model-2 # we have to add @temp_decorator
# print_name()

# # step numbers for processing
# # defining a decorator
# def hello_decorator(func):   # step-2
#     # inner1 is a Wrapper function in which the argument is called
#     # inner function can access the outer local functions like in this case "func"
#     def inner1():   # step-3   # step-6
#         print("Hello, this is before function execution")  # step-7
#         # calling the actual function now inside the wrapper function.
#         func()  # step-8
#         print("This is after function execution")  # step-11
#     return inner1   # step-4
#
#
# # defining a function, to be called inside wrapper
# def function_to_be_used():  # step-9
#     print("This is inside the function !!")  # step-10
#
#
# # passing 'function_to_be_used' inside the decorator to control its behaviour
# function_to_be_used = hello_decorator(function_to_be_used)   # step-1
#
# # calling the function
# function_to_be_used()  # step-5  # step-12


#
# def temp_decorator(func):
#     def wrapper(*args, **kwargs):  # should have same no. of arguments as func so we can use args, kwargs
#         print('starting decorator')
#         func(*args, **kwargs)  # the function arguments should match so we can use args, kwargs
#         print('Ending decorator')
#     return wrapper
#
#
# @temp_decorator    # equivalent to print_name = temp_decorator(print_name)
# def add10(x):
#     print(x+10)
#     return x+10
#
#
# # Model-2 # we have to add @temp_decorator
# add10(15)
#
# print(help(add10))
# print(add10.__name__)  # identity of add10 will change as wrapper


# # for not changing the identity use functools
# import functools
# def temp_decorator(func):
#     @functools.wraps(func)   # preserve the actual function information
#     def wrapper(*args, **kwargs):  # should have same no. of arguments as func so we can use args, kwargs
#         print('starting decorator')
#         temp = func(*args, **kwargs)  # the function arguments should match so we can use args, kwargs
#         print('Ending decorator')
#         return temp
#     return wrapper
#
#
# @temp_decorator    # equivalent to print_name = temp_decorator(print_name)
# def add10(x):
#     print(x+10)
#     return x+10
#
#
# # Model-2 # we have to add @temp_decorator
# add10(15)
#
# print(help(add10))
# print(add10.__name__)  # identity of add10 will change as wrapper
#
#
# # new_example
#
# def repeat(num_times):
#     def temp_decorator(func):
#         @functools.wraps(func)
#         def inner_wrap(*args, **kwargs):
#             for i in range(num_times):
#                 func(*args,**kwargs)
#         return inner_wrap
#     return temp_decorator
#
#
# @repeat(num_times=3)  # decorators arguments
# def greet(name):
#     print(f'Hello {name}')
#
#
# greet('pavan')
#
#
# # multiple decorators or nested decorators or chaining decorators
# # code for testing decorator chaining
# def decor_sqr(func):
#     def inner():
#         x = func()
#         return x * x
#     return inner
#
#
# def decor_double(func):
#     def inner():
#         x = func()
#         return 2 * x
#     return inner
#
#
# @decor_sqr
# @decor_double  # same as decor_sqr(decor_double(num))
# def num():
#     return 10
#
#
# @decor_double
# @decor_sqr  # same as decor_double(decor_sqr(num))
# def num2():
#     return 10
#
#
# print(num())
# print(num2())
#
#

# class decorators

# Python program showing
# use of __call__() method

class MyDecorator:
    def __init__(self, func):
        self.func = func
        self.num_calls = 0

    def __call__(self):
        # We can add some code
        # before function call
        print('Hi there')
        self.func()
        self.num_calls += 1
        print(f'no of calls are {self.num_calls}')

        # We can also add some code
        # after function call.


# adding class decorator to the function
@MyDecorator
def say_hello():
    print("Hello")


say_hello()
say_hello()

