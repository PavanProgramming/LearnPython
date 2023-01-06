#
# class EmployeeTrailA:
#
#     def __init__(self, first, last):
#         self.first = first
#         self.last = last
#         self.email = '{}_{}@email.com'.format(self.first, self.last)
#
#     def fullname(self):
#         return '{} {}'.format(self.first, self.last)
#
#
# emp_a = EmployeeTrailA('abc', 'def')
# print(emp_a.first)
# print(emp_a.email)
# emp_a.first = 'ghi'
# print(emp_a.email)  # as we have not set emp_a.email value or as it is not extracting its value at run time
# # it is not set, so we have to convert it in to property
#
#
# class Employee:
#
#     def __init__(self, first, last):
#         self.first = first
#         self.last = last
#
#     @property
#     # the property decorator allows us to define a method, but we can access it like an attribute
#     # while calling we have to call with name only as it is attribute
#     def email(self):
#         return '{}_{}@email.com'.format(self.first, self.last)
#
#     @property
#     # to set value to property we have to use property setter
#     def fullname(self):
#         return '{} {}'.format(self.first, self.last)
#
# emp_1 = Employee('John', 'Smith')
# # emp_1.fullname = "Corey Schafer" # results an error because you cannot set value to property
# # to set value to property we have to use setter
#
# print(emp_1.first)
# print(emp_1.email)
# print(emp_1.fullname)
#


class Employee:

    def __init__(self, first, last):
        self.first = first
        self.last = last

    @property
    # the property decorator allows us to define a method, but we can access it like an attribute
    # while calling we have to call with name only as it is attribute
    def email(self):
        return '{}_{}@email.com'.format(self.first, self.last)

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last

    @fullname.deleter
    def fullname(self):
        print('Delete Name!')
        self.first = None
        self.last = None


emp_1 = Employee('John', 'Smith')
emp_1.fullname = "Corey Schafer"

print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname)

del emp_1.fullname

print(emp_1.fullname)