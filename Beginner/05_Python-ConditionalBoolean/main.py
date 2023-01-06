# Comparisons:
# Equal:            ==
# Not Equal:        !=
# Greater Than:     >
# Less Than:        <
# Greater or Equal: >=
# Less or Equal:    <=
# Object Identity:  is


# False Values:
    # False
    # None
    # Zero of any numeric type
    # Any empty sequence. For example, '', (), [].
    # Any empty mapping. For example, {}.

# condition = False
# condition = {}
condition = 0.00
if condition:
    print('Evaluated to True')
else:
    print('Evaluated to False')

condition = 'Test'
if condition:
    print('Evaluated to True')
else:
    print('Evaluated to False')


a = [1, 2, 3]
b = a
c = [1, 2, 3]
print(id(a))
print(id(b))
print(id(c))
print(a == b)
print(id(a) == id(c))