
student = {'name': 'John', 'age': 25, 'courses': ['Math', 'CompSci'], 5: 'five'}

for key, value in student.items():
    print(key, value)

print(student.keys())
print(student.values())
print(student.items())

print(student)
print(student['name'])
print(student[5])
print(student.get(5))
print(student.get(6,'Not found'))
print(student.get(6,10))

del student['name']  #
print(student)

stud1 = student.pop('age') # removes and assign the value to stud1
print(stud1)

print(student)
print(dir(student))


student = {'name': 'John', 'age': 25, 'courses': ['Math', 'CompSci'], 5: 'five'}
for var_keys in student:
    print(var_keys)

for var_keys in student.items():
    print(var_keys)

for var_key, var_value in student.items():
    print(var_key, var_value)