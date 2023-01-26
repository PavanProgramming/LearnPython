# strings: ordered, immutable, text representation

# msg = 'Hello World'  # "Hello World"
#
# print(msg)
# print(type(msg))
# print(len(msg))
#
# # prints 2 to 4
# print(msg[2:5])
#
# # prints 2 to end
# print(msg[2:])
#
# # prints starting to 6
# print(msg[:7])
#
#
# # all attributes and methods access to that variable
# print(dir(name))
#
# # help function for string class
# # print(help(str))
#
# print(help(str.lower))

# # """ triple double quotes generally used for documentation purpose. we can use for multiline strings
# my_str = """ Hello
# World
#     welcome"""
# print(my_str)
#
# my_str2 = "Hello World"
# # my_str2[3] = 'p'  # results an error because strings are immutable
#
# my_str3 = my_str2[::-1]
# print(my_str3)
#
# my_str4 = my_str2 + " , " + my_str3  # string concatenates
# print(my_str4)
#
# for i in my_str4:
#     print(i)
#
# my_str5 = '       Hello   World         '
# my_str6 = my_str5.strip()  # removes the whitespaces at starting and ending
# # remember strip method is not doing inplace operation bcz string is immutable
# print(my_str6)
# print(my_str5)
#
# print(my_str6.upper())  # converts to upper case
# print(my_str6.lower())  # converts to lower case
# print(my_str6.startswith("Hai"))
# print(my_str6.find('lo'))  # returns index value
# print(my_str6.find('o'))  # returns index value
# print(my_str6.find('p'))  # returns -1 if not present
# # count, replace,

# lists and strings
#
# my_str5 = 'Hello World, hai this is pavan'
# my_list = my_str5.split()  # default argument is space i.e., same as split(" ")
# print(my_list)
#
# my_str6 = ",".join(my_list)
# print(my_str6)
#
# # very bad code
# my_str7 = ''
# print(id(my_str7))
# for i in my_list:
#     my_str7 += i
#     print(id(my_str7))
# print(my_str7)
# print(id(my_str7))
# # adding strings like this very bad bcz strings are immutable so everytime it creates new space
# # good way is using join method  # cleaner and faster way

#
# from timeit import default_timer as timer
#
# my_list = ['a']*100000
# #print(my_list)
#
# # bad code
# start = timer()
# my_str8 = ''
# for i in my_list:
#     my_str8 += i
# stop = timer()
# print(stop-start)
# #print(my_str8)
#
# # good and cleaner code
# start = timer()
# my_str9 = ''.join(my_list)
# stop = timer()
# print(stop-start)
# #print(my_str9)
#
# # so join method will be much faster and cleaner way


# string formatting
greeting = 'Hello'
name = 'pavan'

msg = "my name is %s" % name  # thsi tells to interpreter that we have placeholder of string type
# %d for int, %f for floating pt.
# %.4f means after dot 4 values
print(msg)

var = 3.1234567
msg1 = '{}, {}. welcome!, the value is {}'.format(greeting, name, var)  # place holder
print(msg1)

msg2 = '{}, {}. welcome!, the value is {:.3f}'.format(greeting, name, var)  # place holder
print(msg2)

# new style
# python 3.6 and above f-strings are available
msg1 = f'{greeting}, {name.upper()}. welcome!'
print(msg1)

msg1 = f"{greeting}, {name.upper()}. welcome!, the value is {var}"
print(msg1)
