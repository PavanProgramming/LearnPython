# Numbers and random module
# num1 = 3
# print(type(num1))
#
# num2 = 3.4
# print(type(num2))
#
# # division
# print(15/4)
#
# # floor division
# print(15//4)
#
# # round
# print(round(3.75947))
# print(round(3.75947,1))
# print(round(3.75947,3))
#
# # conversion of string in to integer
# num3 = '123'
# num4 = int(num3)
#
# print(type(num4))
#

import random
# a = random.random()  # in the range 0 to 1
# print(a)
#
# a = random.uniform(1, 10)  # in the specified range
# print(a)
#
# a = random.randint(1, 10)  # integers in the specified range
# print(a)
#
# a = random.randrange(1, 10)  # integers in the specified range
# # but never pick last int i.e.,for (1, 10) never picks 10
# print(a)
#
# a = random.normalvariate(0,1)  # normal distribution with mu and sigma
# print(a)
#
# mylist = list("ABCDEF")
# print(mylist)
# a = random.choice(mylist)
# print(a)  # picks a single element
#
# a = random.sample(mylist, 6)  # picks unique elements with specified no. of choices
# print(a)
#
# a = random.choices(mylist, k=3)  # k will tell no. of choices
# print(a)
#
# random.shuffle(mylist)  # shuffles the list
# print(mylist)

# random.seed(1)  # initialize internal state
# # so when executing always generates the same random values
# print(random.random())
# print(random.randint(1, 10))
# # use: even if you run on different systems with same random.seed values
# # generates same random numbers
# # i.e., we can reproduce random values using seed function
# random.seed(2)
# print(random.random())
# print(random.randint(1, 10))
#
# random.seed(1)
# print(random.random())
# print(random.randint(1, 10))
#
# # if we use seed the random numbers are reproducable

# for security purposes we use secrets module
# mainly 3 functions


import secrets

a = secrets.randbelow(10)  # random value between 0 to 9 bcz 10 is not included
print(a)

a = secrets.randbits(4)  # generates the equivalent 4 bit binary number  # so range is 0(0000) to 15 (1111)
print(a)

mylist = list("ABCDEF")
a = secrets.choice(mylist)
print(a)
