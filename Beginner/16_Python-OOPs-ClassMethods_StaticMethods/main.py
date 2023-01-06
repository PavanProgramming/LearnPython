class Employee:

    num_of_emps = 0
    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay

        Employee.num_of_emps += 1

    def fullname(self): # instance method is having instance variable self
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    @classmethod  # class method is having class variable cls
    def set_raise_amt(cls, amount):
        cls.raise_amt = amount

    @classmethod # alternate constructor using constructor method
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay) # returning new Employee class object # same as Employee(first,last,pay)

    @staticmethod # if a method don't use instance or class variable you can make it as static method
    def is_workday(day): # static methods don't pass anything automatically,
        # they are like regular functions except they are in class because of logical connection with class
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'Employee', 60000)

emp_1.raise_amt = 1.08
print(emp_1.raise_amt)
print(Employee.raise_amt)
Employee.set_raise_amt(1.07) # calling class method
print(Employee.raise_amt)
print(emp_1.raise_amt)  # as instance don't have raise_amt variable so it will take class variable

emp_str_1 = 'John-Doe-70000'
emp_str_2 = 'Steve-Smith-30000'
emp_str_3 = 'Jane-Doe-90000'

# first, last, pay = emp_str_1.split('-')
# new_emp_1 = Employee(first, last, pay) # using __init__ constructor
new_emp_1 = Employee.from_string(emp_str_1)

print(new_emp_1.email)
print(new_emp_1.pay)

import datetime
my_date = datetime.date(2021,12,28)
print(my_date)
print(my_date.weekday())
print(Employee.is_workday(my_date))