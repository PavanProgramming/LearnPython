# itertools: product, permutations, combinations,accumulate, groupby, and infinte iterators

# from itertools import product
# a = [1, 2]
# b = [3]
# prod = product(a, b)
# print(prod)
# print(list(prod))
# prod = product(a, b, repeat=2) # create a product from repeat =1 samples
# print(list(prod))
#

# from itertools import permutations
# a= [1, 2, 3]
# perm = permutations(a)  # default length of permutations is size of list
# print(list(perm))
#
# perm = permutations(a, 2)
# print(list(perm))
#
# from itertools import combinations
# a= [1, 2, 3, 4]
# perm = combinations(a,2)  # length for combinations is mandatory
# print(list(perm))
#
# perm = combinations(a, 3)
# print(list(perm))

# from itertools import accumulate
# a = [1, 2, 5, 3, 4]
# acc = accumulate(a) # by default accumulation is sum
# print(a)
# print(list(acc))
#
# import operator
# acc = accumulate(a, func=operator.mul)
# print(list(acc))
# acc = accumulate(a, func=max)  # after maximum all elements are max. value only
# print(list(acc))

# from itertools import groupby
#
# def smaller_than_3(x):
#     return x<3
#
#
# a = [1, 2, 5, 3, 4]
# group_obj = groupby(a, key=smaller_than_3)
# print(group_obj)
# for key,value in group_obj:
#     print(key, list(value))
#
# # using lambda function
# group_obj_1 = groupby(a, key=lambda x: x<3)
# print(group_obj_1)
# for key,value in group_obj_1:
#     print(key, list(value))
#
# persons = [{'name': "abc", 'age': 26}, {'name': 'bcd', 'age': 28},
#            {'name': "cde", 'age': 27}, {'name': 'jkl', 'age': 26}]
# group_obj_3 = groupby(persons, key=lambda x: x['age'])
# # doubt: grouping if successive elements are same
# # otherwise creating a new group
# for key, value in group_obj_3:
#     print(key, list(value))

from itertools import count, cycle, repeat

# for i in count(10): # count starts from 10 to infinity
#     print(i)
#     if i==15:
#         break
#
# a = [1, 2, 3, 4, 5]
# for i in cycle(a):  # cycle will repeat same values infinite times
#     print(i)
#
# for j in repeat(10):  # repeat the value of j as 10 infinite times
#     print(j)

for j in repeat(15, 5):  # repeat 15 for 5 times
    print(j)

