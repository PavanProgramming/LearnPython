msg = 'Hello World'

print(msg)
print(len(msg))

# prints 2 to 4

print(msg[2:5])

# prints 2 to end
print(msg[2:])

# prints starting to 6
print(msg[:7])

greeting = 'Hello'
name = 'pavan'

msg1 = '{}, {}. welcome!'.format(greeting, name)
print(msg1)

# python 3.6 and above f-strings are available
msg1 = f'{greeting}, {name.upper()}. welcome!'
print(msg1)

# all attributes and methods access to that variable
print(dir(name))

# help function for string class
# print(help(str))

print(help(str.lower))
