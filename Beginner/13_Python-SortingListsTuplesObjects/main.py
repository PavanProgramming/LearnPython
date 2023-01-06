#
# li = [9,1,5,7,6,4,2,3,8]
#
# s_li = sorted(li) # returns sorted list
# print(s_li)
#
# s_li2 = sorted(li,reverse=True) # returns sorted list
# print(s_li2)
#
# li2 = li
# temp = li2.sort() #  inplace sorting, returns none
# print(li2)
# print(temp)
#
# li3 = li
# temp = li3.sort(reverse=True) #  inplace sorting, returns none
# print(li2)
#
# li4 =  [-6,1,2,-4, 3,0]
# s_li3 = sorted(li4, key =abs) # [0, 1, 2, 3, -4, -6]
# print(s_li3)
#
# tup = (9,1,5,7,6,4,2,3,8) # as tuple are immutable so can't do inplace
# s_tup = sorted(tup)
# print(s_tup)
#
# # di = {'name':'python', 'age':12, 5:'56'} # TypeError: '<' not supported between instances of 'int' and 'str'
#
# di = { 'bcd': 'temp' ,'name':'python', 'age':12} # sorts the keys
# s_di = sorted(di)
# print(s_di)

class Employee():
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def __repr__(self):
        return f'{self.name},{self.age},Rs:{self.salary}'


e1 = Employee('abc', 25, 50000)
e2 = Employee('bcd', 28, 55000)
e3 = Employee('cde', 26, 30000)

print(e1)

emp_list = [e1, e2, e3]
print(emp_list)


def e_sort(temp):
    return temp.salary


s_emp_list = sorted(emp_list, key=e_sort , reverse=True) # sorting based on e_sort function # reverse will enables sorting in reverse order
print(s_emp_list)

s_emp_list_new = sorted(emp_list, key= lambda e:e.age)  # sorting implemented using lambda function
print(s_emp_list_new)

from operator import attrgetter
s_emp_list_new2 = sorted(emp_list, key=attrgetter('age'))  # sorting implemented using lambda function
print(s_emp_list_new2)
