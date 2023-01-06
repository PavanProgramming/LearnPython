'''
LEGB
Local, Enclosing, Global, Built-in
'''

# x = 'global_x'
#
# def test():
#     y = 'local_y'
#     print(x)
#     print(y)
#
#
# test()
# print(y) # out of scope
#
#

# x = 'global_x'
#
# def test():
#     global x # telling that accessing global x , if not created it will create at here
#     x = 'new global x in local'
#     print(x)
#
#
# print(x)
# test()
# print(x) # out of scope

# import builtins
#
# print(dir(builtins))
#
# # note: if you use the same name of built-in function for user defined function then first priority for locally declared function
#
# m = min([5,8,1,2,3])
# print(m)
#
#
# def min(x):
#     return x[0]
#
# r = min([5,8,1,2,3]) # our min function have higher priority than buildin min function
# print(r)


# def outer():
#     x = 'outer_x'
#
#     def inner():
#         x = 'inner_x'
#         print(x)
#
#     inner()
#     print(x)
#
# outer()

x= 'global_x'
def outer():
    x = 'outer1_x'
    print(x)

    def inner():
        #nonlocal x  # teels that calling nonlocal variable which is not global
        x='outer2_x'
        print(x)

        def inner2():
            nonlocal x  # teels that calling nonlocal variable which is not global
            x = 'inner_x'
            print(x)

        inner2()
        print(x)

    inner()
    print(x)

outer()
print(x)