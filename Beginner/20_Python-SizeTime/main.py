# Note: tuple is more efficient than list, let us check the sizes and iteration time
import sys
my_list = ['india', 28, True, "Temp", 10]
my_tuple = ('india', 28, True, "Temp", 10)
print(sys.getsizeof(my_list), "bytes")
print(sys.getsizeof(my_tuple), "bytes")

import timeit
# syntax: timeit.timeit(stmt="expression", number=no. of times you want to repeat) # returns time in seconds
print(timeit.timeit(stmt="['india', 28, True, 'Temp', 10]", number=1000000))
print(timeit.timeit(stmt="('india', 28, True, 'Temp', 10)", number=1000000))