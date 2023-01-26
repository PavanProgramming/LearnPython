#
# # Dictionary: key-value pairs, Unordered, Mutable
#
# mydict1 = {'name': 'pavan', 'age': 25, 'city': "calicut"}
# print(mydict1)
#
# mydict2 = dict(name='pavan', age=25, city="calicut")
# print(mydict2)
#
# mydict2["city"]="kochi"
# mydict2['email']="temp@xyz.com"
# print(mydict2)
#
# student = {'name': 'pavan', 'age': 25, 'courses': ['Math', 'CompSci'], 5: 'five'}
# print(student)
#
# for key, value in student.items():
#     print(key, value)
#
# print(student.keys())
# print(student.values())
# print(student.items())
#
# print(student)
# print(student['name'])
# print(student[5])
# print(student.get(5)) # get the value of key-5
# print(student.get(6,'Not found')) # get the value of key-6, if no key with name as 6 then returns Not found
# print(student.get(6,10))  # get the value of key-6, if no key with name as 6 then returns 10
#
# del student['name']  # deletes name key-value pair
# print(student)
#
# stud1 = student.pop('age') # removes the age key-value and assign the value to stud1
# print(stud1)
#
# stud1 = student.popitem() # removes the last item declared
# print(stud1)
#
# print(student)
# print(dir(student))
#
#
# student = {'name': 'John', 'age': 25, 'courses': ['Math', 'CompSci'], 5: 'five'}
# for var_keys in student:
#     print(var_keys)
#
# for var_keys in student.keys():
#     print(var_keys)
#
# for var_values in student.values():
#     print(var_values)
#
# for var_keys in student.items():
#     print(var_keys)
#
# for var_key, var_value in student.items():
#     print(var_key, var_value)
#
# # to check whether key is present or not use if or use try-except
# if 'name' in student:
#     print(student['name'])

# copying

student = {'name': 'John', 'age': 25, 'courses': ['Math', 'CompSci']}

stud_cpy1 = student
stud_cpy1['new'] = 'temp'
print(student)

stud_cpy2 = student.copy()
stud_cpy2['email'] = "temp@mail.com"
print(stud_cpy2)
print(student)
stud_cpy3 = dict(student)
stud_cpy3['email'] = "temp@mail.com"
print(stud_cpy3)
print(student)
student2 = dict(name='pavan',age='25',city='calicut')
stud_cpy3.update(student2)  # the key-value pairs of stud_cpy3 are updated with student2 and rest will be added
print(stud_cpy3)


# you can use tuple as key but not list

mytuple = (5,6)
print(type(mytuple))
mydict = {mytuple:15, 'name':'pavan'}  # bcz tuple is immutable so it can be hashable
# but list is mutable,so it is unhashable type so list cannot be a key
print(mydict)
