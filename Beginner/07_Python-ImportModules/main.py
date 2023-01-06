

import own_module as om

courses = ['History', 'Math', 'Physics', 'CompSci']
index = om.find_index(courses, 'Math')
print(index)
print(om.test)

from own_module import find_index as fi, test as ti
index1 = fi(courses, 'Math')
print(index1)
print(ti)

import sys
# so this is the list of directories on my machine where Python
# looks for modules when we run an import and it looks in this order now this
# first value here is just the directory where I'm currently running the script
print(sys.path)

sys.path.append('D:\pavanfiles\LearningResources')  # adds the path provided to list of system directories for this script
# if you want to permanently then add to environment variables
print(sys.path)


import random
print(random.choice(courses))

import math
print(math.radians(90))
print(math.sin(90))

import datetime
print(datetime.date.today())

import calendar
print(calendar.isleap(2000))

import os
print(os.getcwd())
print(os.__file__)    # provides the path of the module