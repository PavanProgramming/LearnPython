"""
#  Generators: A generator-function is defined like a normal function, but whenever
#  it needs to generate a value, it does so with the yield keyword rather than return.
#  If the body of a def contains yield, the function automatically becomes a generator function.
#  after yield the iteration will pause
#  Use the next() function to advance iterators, instead of calling .__next__() directly.
#  return in a generator has been equivalent to raise StopIteration()
Generators provide a space-efficient method
"""

# # A generator function that yields 1 for first time,2 second time and 3 third time
# def simpleGeneratorFun():
#     yield 1
#     yield 2
#     yield 3
#
#
# temp = simpleGeneratorFun()
# print(temp)  # prints generator object
#
# print(next(temp))  # Iterating over the generator object using next
# print(next(temp))  # Iterating over the generator object using next
# print(next(temp))  # Iterating over the generator object using next
#
# # Driver code to check above generator function
# # So a generator function returns an generator object that is iterable, i.e., can be used as an Iterators .
# for value in simpleGeneratorFun():  # generator object is iterating in for loop
#     print(value)

# def simpleGeneratorFun():
#     yield 4
#     yield 1
#     yield 2
#     yield 3
#
#
# temp = simpleGeneratorFun()
# # print(sum(temp))  # temp is a iterable object
# print(sorted(temp,reverse=True))

# def simpleGeneratorFun(num):
#     print('Starting')
#     while num>0:
#         yield num
#         num -= 1
#
#
# cd = simpleGeneratorFun(5)
# val = next(cd) # calling the generator and pausing after yield statement
# print(val)
#
# val = next(cd) # resuming from pausing location and pausing after yield statement
# # that's why again it won't print Starting
# print(val)

# # size comparison of Generators and normal functions
# import sys
# def firstn(n):
#     nums = []
#     num = 0
#     while n>num:
#         nums.append(num)
#         num += 1
#     return nums
#
#
# def firstn_generator(n):
#     num = 0
#     while n>num:
#         yield num
#         num += 1
#
#
# print(sys.getsizeof(firstn(1000000)))
# print(sys.getsizeof(firstn_generator(1000000)))
#
# # observe the size differences. In generator we no need to save those values so it saves huge memory
#
# # A simple generator for Fibonacci Numbers
# def fib(limit):
#     # Initialize first two Fibonacci Numbers
#     a, b = 0, 1
#
#     # One by one yield next Fibonacci Number
#     while a < limit:
#         yield a
#         a, b = b, a + b
#
#
# # # Create a generator object
# # x = fib(5)
# #
# # # Iterating over the generator object using next
# # print(next(x))  # In Python 3, __next__()
# # print(next(x))
# # print(next(x))
# # print(next(x))
# # print(next(x))
#
# # Iterating over the generator object using for
# # in loop.
# for i in fib(30):
#     print(i)


mygen = (i for i in range(10) if i % 2 == 1)
print(type(mygen))  # mygen is generator class
# for _ in mygen:
#     print(_)
print(list(mygen))

mygen_list = [i for i in range(10) if i % 2 == 1]
print(type(mygen_list))  # mygen_list is list class


import sys

mygen2 = (i for i in range(1000000) if i % 2 == 1) # mygen is generator class
print(sys.getsizeof(mygen2))

mygen_list2 = [i for i in range(1000000) if i % 2 == 1] # mygen_list is list class
print(sys.getsizeof(mygen_list2))




