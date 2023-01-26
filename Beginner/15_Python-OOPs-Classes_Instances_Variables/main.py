

class Employee:
    raise_amount = 1.04 # class variable
    no_of_emps = 0

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '_' + last + '@email.com'
        self.pay = pay
        Employee.no_of_emps += 1

    def fullname(self):
        # return '{} {}'.format(self.first, self.last)
        return f'{self.first}{self.last}'

    def apply_raise(self):
        # self.pay = int(self.pay* Employee.raise_amount)  # accessing Class variable
        self.pay = int(self.pay * self.raise_amount)
        # self.pay = int(self.pay * raise_amount) # results an error


emp_1 = Employee('abc', 'def', 50000)
emp_2 = Employee('ghi', 'jkl', 60000)

# print(emp_1.email)
# print(emp_2.fullname())  # internally emp_2.fullname() will convert as Employee.fullname(emp_2)
# print(Employee.fullname(emp_2))
# emp_1.apply_raise()
# print(emp_1.pay)

print(emp_1.raise_amount)
print(Employee.raise_amount)

Employee.raise_amount = 1.05
print(emp_1.raise_amount)  # accessing from class variable
print(Employee.raise_amount)

emp_1.raise_amount = 1.06
print(emp_1.raise_amount)  # accessing from class variable
print(Employee.raise_amount)

print(Employee.no_of_emps)

print(emp_1.__dict__)   # observe that emp_1 doesn't have raise_amount so it will access from Employee class variable
print(Employee.__dict__)

# Python has a set of built-in methods and __call__ is one of them. The __call__ method enables
# Python programmers to write classes where the instances behave like functions and can be called like a function.

class Example:
    def __init__(self):
        print("Instance Created")

    # Defining __call__ method
    def __call__(self):
        print("Instance is called via special method")


# Instance created
e = Example()

# __call__ method will be called
e()


class Product:
    def __init__(self):
        print("Instance Created")

    # Defining __call__ method
    def __call__(self, a, b):
        print(a * b)


# Instance created
ans = Product()

# __call__ method will be called
ans(10, 20)


# Whenever a class is instantiated __new__ and __init__ methods are called.
# __new__ method will be called when an object is created and __init__ method will be called to initialize the object.
# In the base class object, the __new__ method is defined as a static method which requires to pass a parameter cls.
# cls represents the class that is needed to be instantiated, and the compiler automatically provides this parameter
# at the time of instantiation.
class A(object):
    def __new__(cls):
        print("Creating instance")
        return super(A, cls).__new__(cls)

    def __init__(self):
        print("Init is called")


A()

# The above example shows that __new__ method is called automatically when calling the class name,
# whereas __init__ method is called every time an instance of the class is returned by __new__ method,
# passing the returned instance to __init__ as the self parameter, therefore even if you were to save
# the instance somewhere globally/statically and return it every time from __new__, then __init__ will be
# called every time you do just that.

# note: __init__() should return None


