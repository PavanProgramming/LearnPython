# collections: Counter, namedtuple, OrderedDict, defaultdict, deque


# # counter: The counter is a container that stores the elements as dictionary keys
# # and their counts as dictionary values
#
# from collections import Counter
# str1 = "aaaabbccc"
# my_count = Counter(str1)
# # my_count is Counter object type i.e., collections.Counter object
# print(my_count)
# print(type(my_count))
# print(my_count.items())
# print(my_count.keys())
# print(my_count.values())
# print(my_count.most_common(2))  # displays first 2 most common types as a list of tuples
# print(my_count.most_common(2)[0][0])  # to get most common element
# print(my_count.elements())  # this will give us an iterable over elements repeating each as
# # many times as it counts so I have to convert this to a list in order to print it
# print(list(my_count.elements()))
#


# # named tuples is an easy to create and lightweight object type similar to a struct
# # Python supports a type of container dictionaries called “namedtuple()” present in the module, “collections“.
# # Like dictionaries, they contain keys that are hashed to a particular value. But on contrary,
# # it supports both access from key-value and iteration, the functionality that dictionaries lack.
# from collections import namedtuple
#
# # Declaring namedtuple()
# Student = namedtuple('Student', ['name', 'age', 'DOB'])
# # Adding values
# S = Student('Pavan', '19', '2541997')
# print(S)
# # Access using index
# # The attribute values of namedtuple() are ordered and can be accessed using the index number
# # unlike dictionaries which are not accessible by index.
# print("The Student age using index is : ", end="")
# print(S[1])
# # Access using keyname:  Access by keyname is also allowed as in dictionaries.
# print("The Student name using keyname is : ", end="")
# print(S.name)
#
# # Access using getattr():
# # using getattr(): This is yet another way to access the value by giving namedtuple and key value as its argument.
# print("The Student DOB using getattr() is : ", end="")
# print(getattr(S, 'DOB'))
#
# Point = namedtuple('Point', 'x,y')
# pt = Point(1, -4)
# print(pt)
# print(pt.x, pt.y)


# # Ordered Dictionary
# # the ordered dict is just like a regular dictionary but they remember the order that the
# # items were inserted so they have become less important now since the built in
# # dictionary class has also the ability to remember the order since Python 3.7
# # from pyton 3.7version we can replace orderedDict with normal dictionary
# from collections import OrderedDict
# ordered_dict = OrderedDict()
# ordered_dict['b'] = 2
# ordered_dict['c'] = 3
# ordered_dict['d'] = 4
# ordered_dict['a'] = 1
# print(ordered_dict)


# # defaultDict:  default dict is also similar to the usual dictionary container with the
# # only difference that it will have a default value if the key has not been set
# from collections import defaultdict
#
# d= defaultdict(int)
# d['a'] = 1
# d['b'] = 2
# print(d['b'])
# print(d['c'])  # returns 0 bcz it is not present
#
# d= defaultdict(list)
# d['a'] = 1
# d['b'] = 2
# print(d['b'])
# print(d['c'])  # returns empty list bcz it is not present

#  the deck is a double ended queue and it can be used to add or remove elements from
#  both ends and both are implemented in a way that this will be very efficiently

from collections import deque
d= deque()
d.append(1)
d.append(3)
print(d)
d.appendleft('hai')
print(d)
d.pop()
print(d)
d.popleft()
print(d)
d.extend([10,85,19])
print(d)
d.extendleft([10,85,19])
print(d)
d.rotate(2) # rotate right by 2 times
print(d)
d.rotate(-3) # rotate left by 3 times
print(d)

