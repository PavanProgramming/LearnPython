"""
Context managers are a great tool for resource management.
They allow you to allocate and release resources precisely when you want to.
A well-known example is the with open() statemtent:
"""

with open('notes.txt', 'w') as f:
    f.write('some todo...')

"""
This will open a file and makes sure to automatically close it after 
program execution leaves the context of the with statement. 
It also handles exceptions and makes sure to properly close the file even in case of an exception. 
Internally, the above code translates to something like this:
"""

f = open('notes.txt', 'w')
try:
    f.write('some todo...')
finally:
    f.close()

# We can see that using a context manager and the with statement is much shorter and more concise.

"""
Examples of context managers:
Open and close files
open and close database connections
Acquire and release locks
"""

from threading import Lock
lock = Lock()

# error-prone:
lock.acquire()
# do stuff
# lock should always be released!
lock.release()

# Better:
with lock:
    # do stuff

"""
Implementing a context manager as a class¶
To support the with statement for our own classes, we have to implement 
the __enter__ and __exit__ methods. 
Python calls __enter__ when execution enters the context of the with statement. 
In here the resource should be acquired and returned. 
When execution leaves the context again, __exit__ is called and the resource is freed up.
"""

class ManagedFile:
    def __init__(self, filename):
        print('init', filename)
        self.filename = filename

    def __enter__(self):
        print('enter')
        self.file = open(self.filename, 'w')
        return self.file

    def __exit__(self, exc_type, exc_value, exc_traceback):
        if self.file:
            self.file.close()
        print('exit')

with ManagedFile('notes.txt') as f:
    print('doing stuff...')
    f.write('some todo...')

"""
Handling exceptions:
If an exception occurs, Python passes the type, value, and traceback to the __exit__ method. 
It can handle the exception here. 
If anything other than True is returned by the __exit__ method, 
then the exception is raised by the with statement.
"""

class ManagedFile:
    def __init__(self, filename):
        print('init', filename)
        self.filename = filename

    def __enter__(self):
        print('enter')
        self.file = open(self.filename, 'w')
        return self.file

    def __exit__(self, exc_type, exc_value, exc_traceback):
        if self.file:
            self.file.close()
        print('exc:', exc_type, exc_value)
        print('exit')

# No exception
with ManagedFile('notes.txt') as f:
    print('doing stuff...')
    f.write('some todo...')
print('continuing...')

print()

# Exception is raised, but the file can still be closed
with ManagedFile('notes2.txt') as f:
    print('doing stuff...')
    f.write('some todo...')
    f.do_something()
print('continuing...')


# We can handle the exception in the __exit__ method and return True.

class ManagedFile:
    def __init__(self, filename):
        print('init', filename)
        self.filename = filename

    def __enter__(self):
        print('enter')
        self.file = open(self.filename, 'w')
        return self.file

    def __exit__(self, exc_type, exc_value, exc_traceback):
        if self.file:
            self.file.close()
        if exc_type is not None:
            print('Exception has been handled')
        print('exit')
        return True


with ManagedFile('notes2.txt') as f:
    print('doing stuff...')
    f.write('some todo...')
    f.do_something()
print('continuing...')


"""
Implementing a context manager as a generator:
Instead of writing a class, we can also write a generator function and decorate it 
with the contextlib.contextmanager decorator. 
Then we can also call the function using a with statement. 
For this approach, the function must yield the resource in a try statement, 
and all the content of the __exit__ method to free up the resource goes now inside 
the corresponding finally statement.
"""

from contextlib import contextmanager

@contextmanager
def open_managed_file(filename):
    f = open(filename, 'w')
    try:
        yield f
    finally:
        f.close()

with open_managed_file('notes.txt') as f:
    f.write('some todo...')

"""
The generator first acquires the resource. It then temporarily suspends its own execution 
and yields the resource so it can be used by the caller. 
When the caller leaves the with context, the generator continues to execute and frees up 
the resource in the finally statement.
"""
