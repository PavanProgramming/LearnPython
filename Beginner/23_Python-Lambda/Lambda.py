# # lambda argumnets: expression
#
# add10 = lambda x: x+10
# print(add10(5))
#
#
# # same as above lambda expression
# def add10_func(x):
#     return x+10
#
#
# mult = lambda x, y: x*y
# print(mult(10, 20))
#
# pts_2D = [(1, 2), (15, 1), (5, -1), (10, 4)]
# pts_2D_sorted = sorted(pts_2D)  # by default sorted using first value
#
# print(pts_2D)
# print(pts_2D_sorted)
#
# pts_2D_sorted_y = sorted(pts_2D, key=lambda x: x[1])
# print(pts_2D_sorted_y)
#
#
# # same implementation using function
# def sortby_y(x):
#     return x[1]
#
#
# pts_2D_sorted_y_fun = sorted(pts_2D, key=sortby_y)
# print(pts_2D_sorted_y_fun)
#
# # sort by sum of elements
# pts_2D_sorted_sum = sorted(pts_2D, key=lambda x: x[0]+x[1])
# print(pts_2D_sorted_sum)


# map function: map function transforms each element with a function
a = [1, 2, 3, 4, 5]
b= map(lambda x:x*2, a)
print(list(b))

# using comprehensions
c = [x*2 for x in a]
print(c)

# filter function: filter(func, seq)
a = [1, 2, 3, 4, 5]
b = filter(lambda x: x%2==0 , a)
print(list(b))

# using comprehensions
c= [x for x in a if x%2==0]
print(c)





