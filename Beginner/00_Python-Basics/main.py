
# Special properties of and & or

a,b,c,d = 60,70,80,0
print(f'{a},{b},{c},{d}')

temp = a and b and c
print(f'{temp}')  # if all are true then returns last true value

temp = a and b and c and d
print(f'{temp}')

temp = a or b or c  # returns first true occurrence value
print(f'{temp}')

temp = d or c or b or a
print(f'{temp}')

# conditional expression
temp = b if a < b else a
print(f'{temp}')

# for-loops:
"""
A for-loop steps through each of the items in a collection type, or any other type of object 
which is “iterable”
for <item> in <collection>:
    <statements>
<item> can be more than a single variable name
If <collection> is a list or a tuple, then the loop steps through each element of the sequence
When the <collection> elements are themselves sequences, then <item> can match the structure 
of the elements.
This multiple assignment can make it easier to access the individual parts of each element

for (x,y) in [(a,1),(b,2),(c,3),(d,4)]:
    print x

If <collection> is a string, then the loop steps through each character of the string  
for someChar in “Hello World”:
   print someChar

"""

# list comprehensions
li = [1,2,3]
temp = [ele * 2 for ele in li]
print(temp)

li = [('a', 1), ('b', 2), ('c', 3)]
temp = [n * 3 for (x, n) in li]
print(temp)


# filtered list comprehension
"""
Filter  determines whether expression is performed on each member of the list.
For each element of list, checks if it satisfies the filter condition.
If the filter condition returns False, that element is omitted from the list 
before the list comprehension is evaluated.

[ expression for name in list if filter]

"""
li = [3, 6, 2, 7, 1, 9]
temp = [elem*2 for elem in li if elem > 4]
print(temp)

