"""
In Python, assignment statements (obj_b = obj_a) do not create real copies.
It only creates a new variable with the same reference.
So when you want to make actual copies of mutable objects (lists, dicts)
and want to modify the copy without affecting the original, you have to be careful.

For 'real' copies we can use the copy module.
However, for compound/nested objects (e.g. nested lists or dicts) and custom objects
there is an important difference between shallow and deep copying:
- shallow copies: Only one level deep.
It creates a new collection object and populates it with references to the nested objects.
This means modyfing a nested object in the copy deeper than one level affects the original.

- deep copies: A full independent clone.
It creates a new collection object and then recursively populates it with copies of the
nested objects found in the original.

"""

org = 5
cpy = org  # here cpy is reference to org
print(id(org))
print(id(cpy))
cpy = 6  # here cpy is new variable
print(id(org))
print(id(cpy))

"""
Assignment operation:
This will only create a new variable with the same reference. Modifying one will affect the other.
"""

list_a = [1, 2, 3, 4, 5]
list_b = list_a

list_a[0] = -10
print(list_a)
print(list_b)

"""
Shallow copy¶
One level deep. Modifying on level 1 does not affect the other list. 
Use copy.copy(), or object-specific copy functions/copy constructors.
"""

import copy
list_a = [1, 2, 3, 4, 5]
list_b = copy.copy(list_a)

# not affects the other list
list_b[0] = -10
print(list_a)
print(list_b)

"""
But with nested objects, modifying on level 2 or deeper does affect the other!
"""
import copy
list_a = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]]
list_b = copy.copy(list_a)

# affects the other!
list_a[0][0]= -10
print(list_a)
print(list_b)

# You can also use the following to create shallow copies:
list_b = list(list_a)
list_b = list_a[:]
list_b = list_a.copy()

"""
Deep copies:
Full independent clones. Use copy.deepcopy().
"""

import copy
list_a = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]]
list_b = copy.deepcopy(list_a)

# not affects the other
list_a[0][0]= -10
print(list_a)
print(list_b)

"""
Custom objects¶
You can use the copy module to get shallow or deep copies of custom objects.
"""


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


# Only copies the reference
p1 = Person('Alex', 27)
p2 = p1
p2.age = 28
print(p1.age)
print(p2.age)

# shallow copy
import copy
p1 = Person('Alex', 27)
p2 = copy.copy(p1)
p2.age = 28
print(p1.age)
print(p2.age)


# Now let's make a nested object:


class Company:
    def __init__(self, boss, employee):
        self. boss = boss
        self.employee = employee

# shallow copy will affect nested objects
boss = Person('Jane', 55)
employee = Person('Joe', 28)
company = Company(boss, employee)

company_clone = copy.copy(company)
company_clone.boss.age = 56
print(company.boss.age)
print(company_clone.boss.age)

print()
# deep copy will not affect nested objects
boss = Person('Jane', 55)
employee = Person('Joe', 28)
company = Company(boss, employee)
company_clone = copy.deepcopy(company)
company_clone.boss.age = 56
print(company.boss.age)
print(company_clone.boss.age)


