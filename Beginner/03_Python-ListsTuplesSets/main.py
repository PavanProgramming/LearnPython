# #
# # lists: ordered, mutable, allows duplicate elements
#
# # Empty Lists     # mutable
# empty_list1 = []
# empty_list2 = list()
# list_1 = ['History', 'Math', 'Physics', 'CompSci']
#
# print(list_1[-1])  # prints last element
#
# for item in list_1:
#     print(item)
#
# for index, item in enumerate(list_1):
#     print(index, item)
#
# mylist = [5, True, 'apple', "apple"]
# # print(mylist)
# # print(dir(mylist))
# # append : adds at the end
# # insert: insert at specific location
# # pop: removes the last item
# # remove: removes the specific item
# # reverse: reverse the list
# # sort: inplace sort the items if all items are same datatype, returns none
# # sorted: sort the items if all items are same datatype and returns the new sorted list
#
# newlist = list_1 + mylist  # appends list items
# newlist1 = list_1.__add__(mylist)  # same as above
# print(newlist1)
#
# mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# # slicing in lists
# print(mylist[3:])
# print(mylist[:6])
# print(mylist[::2])
# print(mylist[::-1])  # reverse the list
#
# list_1 = ['History', 'Math', 'Physics', 'CompSci']
# list_2 = list_1  # assignment so operation on one list affect others
# list_2.append('chemistry')
# print(list_1)  # observe list2 appends reflects in list1 also
# print(id(list_1))
# print(id(list_2))

# # other ways to copy
# # 1
# list_3 = list_1.copy()  # copies at different location
# print(id(list_1))
# print(id(list_3))
# list_3.append('biology')
# print(list_1)
# print(list_3)
# # 2
# list_4 = list(list_1)  # copies at different location
# print(id(list_1))
# print(id(list_4))
# list_4.append('biology')
# print(list_1)
# print(list_4)
# # 3
# list_5 = list_1[:]  # copies at different location
# print(id(list_1))
# print(id(list_5))
# list_5.append('food tech')
# print(list_1)
# print(list_5)
#
# # creating a list with expression
# mylist = [1, 2, 3, 4, 5]
# sqr_list = [i*i for i in mylist]  # [expression  iterable_item]
# print(sqr_list)

# #  *********************Tuples***********************
# # Tuple: ordered, immutable, allows duplicate elements
# # Empty Tuples      # Immutable
# empty_tuple1 = ()
# empty_tuple2 = tuple()
# tuple_1 = ('History', 'Math', 'Physics', 'CompSci')
# tuple_2 = tuple_1
# print(tuple_1)
# print(id(tuple_1))
# print(id(tuple_2))
# # tuple_1[0] = 'Art' # results an error
# mytuple = 1, 2, 3
# print(mytuple)
# print(type(mytuple))
# # one single element without comma after the element treated as element type only
# mytuple1 = (1)  # integer
# mytuple2 = ('history')  # string
# print(mytuple2)
# print(type(mytuple2))
# # comma after single element is treated as tuple
# mytuple3 = ('history',)  # tuple
# print(mytuple3)
# print(type(mytuple3))
#
# # assigning tuple
# tuple_3 = tuple(['History', 10, 'Math', 'Physics', 'CompSci'])
# print(tuple_3)
# item = tuple_3[-1]
# print(item)
# print(dir(tuple))
#
# mylist = list(tuple_3)
# print(mylist)
#
# mytuple = tuple(mylist)
# print(mytuple)
#
# mytuple4 = (1, 2, 3, 4, 5)
# mytuple5 = mytuple4[::-1]
# print(mytuple5)
#
# # unpacking
# emp1 = 'pavan', 30, 'scientist'  # tuple  # same as ('pavan', 30, 'scientist')
# print(emp1)
# name, age, role = emp1
# print(name)
# print(type(name))
#
# # unpacking multiple elements
# mytuple6 = (1, 2, 3, 4, 5)
# i1, *i2, i3 = mytuple6  # *i2 will save more values as lists
# print('i1:', i1, ', i2:', i2, ', i3:', i3)


# # Note: tuple is more efficient than list, let us check the sizes and iteration time
# import sys
# my_list = ['india', 28, True, "Temp", 10]
# my_tuple = ('india', 28, True, "Temp", 10)
# print(sys.getsizeof(my_list), "bytes")
# print(sys.getsizeof(my_tuple), "bytes")
#
# import timeit
# # syntax: timeit.timeit(stmt="expression", number=no. of times you want to repeat) # returns time in seconds
# print(timeit.timeit(stmt="['india', 28, True, 'Temp', 10]", number=1000000))
# print(timeit.timeit(stmt="('india', 28, True, 'Temp', 10)", number=1000000))

# sets: unordered, mutable, no-duplicates
# Empty Sets  #unordered
empty_set = {}  # This isn't right! It's a dict
empty_set = set()

cs_courses = {'History', 'Math', 'Physics', 'CompSci','History'}
print(cs_courses)
print(dir(cs_courses)) # intersection, union, difference

cs_courses.clear()  # clears or empty the set

myset1 = set(['History', 'Math', 'Physics', 'CompSci','History'])
print(myset1)

myset2 = set("Hello")
print(myset2)
# myset2.add(1)
myset2.add('s')
myset2.add(True)  # true treated as 1
print(myset2)
myset2.remove('o')
print(myset2)
myset2.discard('x')  # remove element if it is member otherwise do nothing

myset2.pop()  # returns arbitrary value
print(myset2)


odds = {1, 3, 5, 7, 9}
evens = {0, 2, 4, 6, 8}
primes = {2, 3, 5, 7}

print(odds.union(evens))
print(evens.intersection(primes))

setA = {1, 2, 3, 4, 5, 6, 7, 8, 9}
setB = {1, 2, 3, 10, 11, 12}
print(setA.difference(setB))
print(setB.difference(setA))
print(setA.symmetric_difference(setB))  # symmetries which are not in both

# update method updates at inplace
setA.update(setB)  # add elements which are not present in the other set
print(setA)
setA = {1, 2, 3, 4, 5, 6, 7, 8, 9}
setA.intersection_update(setB)
print(setA)
# similarly union_update, symmetric_difference_update

setA = {1, 2, 3, 4, 5, 6}
setB = {1, 2, 3}
print(setA.issubset(setB))  # returns false bcz setA is not subset of setB
print(setB.issubset(setA))  # returns True
print(setA.issuperset(setB))
setC = {7, 8}
print(setA.isdisjoint(setC))  # no common elements

# copying sets
setD = setC
setD.add(10)
print(setC)

setE = setC.copy()
setE.add(50)
print(setC)
print(setE)

setF = set(setC)
setF.add(60)
print(setC)
print(setF)


# frozen sets  # Immutable version of set  # you can't change and update creations
fset1= frozenset([1, 2, 3, 4])
print(fset1)
# fset1.add(50)  # results an error
print(dir(fset1))




