

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



