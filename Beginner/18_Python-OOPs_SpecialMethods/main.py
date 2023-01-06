class Employee:

    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '_' + last + '@email.com'
        self.pay = pay

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    # defining our own special methods we'll be able to change some of
    # this built-in behavior and operations so these special methods are always
    # surrounded by double underscores so a lot of people call these double underscores as dunder

    # repr() is met to be an unambiguous representation of the object and should be used for
    # debugging and logging and things like that it's really meant to be seen by
    # other developers and str is meant to be more of a readable representation of an
    # object and is meant to be used as display to the end-user
    def __repr__(self):
        # as __str__ is used to display for end-user during __str___ call time debug will off automatically
        # if you want to call you have to call it
        return "Employee('{}', '{}', {})".format(self.first, self.last, self.pay)

    def __str__(self):
        return '{} - {}'.format(self.fullname(), self.email)

    def __add__(self, other):  # operating overloading for type Employee class
        return self.pay + other.pay

    def __len__(self):
        return len(self.fullname())


emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'Employee', 60000)

print(emp_1)

print(repr(emp_2))
print(str(emp_2))
print(emp_1.__repr__())  # same as print(repr(emp_1))
print(emp_2.__str__())  # same as print(str(emp_2))

print(int.__add__(1, 2))  # same as print(1+2)
print(str.__add__('a', 'b'))  # same as print('a'+'b')

print(emp_1 + emp_2)   # same as emp_1.__add__(emp_2)

print('test'.__len__())  # same as print(len('test'))
print(str.__len__('test'))  # same as print('test'.__len__()) , same as print(len('test'))
print(len(emp_1))