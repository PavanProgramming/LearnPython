"""
Source: https://www.python-engineer.com/courses/advancedpython/17-multiprocessing/

How to create and start multiple processes
How to wait for processes to complete
How to share data between processes
How to use Locks to prevent race conditions
How to use a Queue for process-safe data/task processing.
How to use a Pool to manage multiple worker processes

"""

"""
Create and run processes:
You create a process with multiprocessing.Process(). 
It takes two important arguments:

target: a callable object (function) for this process to be invoked when the process starts
args: the (function) arguments for the target function. This must be a tuple
Start a process with process.start()

Call process.join() to tell the program that it should wait for this process 
to complete before it continues with the rest of the code.
"""

# from multiprocessing import Process
# import os
#
# def square_numbers():
#     for i in range(1000):
#         result = i * i
#
#
# if __name__ == "__main__":
#     processes = []
#     num_processes = os.cpu_count()
#     # number of CPUs on the machine. Usually a good choise for the number of processes
#
#     # create processes and asign a function for each process
#     for i in range(num_processes):
#         process = Process(target=square_numbers)
#         processes.append(process)
#
#     # start all processes
#     for process in processes:
#         process.start()
#
#     # wait for all processes to finish
#     # block the main programme until these processes are finished
#     for process in processes:
#         process.join()


"""
Share data between processes¶
Since processes don't live in the same memory space, they do not have access to the same (public) data. 
Thus, they need special shared memory objects to share data.

Data can be stored in a shared memory variable using Value or Array.
    Value(type, value): Create a ctypes object of type type. Access the value with .target.
    Array(type, value): Create a ctypes array with elements of type type. Access the values with [].

Task: Create two processes, each process should have access to a shared variable and 
modify it (in this case only increase it repeatedly by 1 for 100 times). 
Create another two processes that share an array and modify (increase) all the elements in the array.

"""

# from multiprocessing import Process, Value, Array
# import time
#
# def add_100(number):
#     for _ in range(100):
#         time.sleep(0.01)
#         number.value += 1
#
# def add_100_array(numbers):
#     for _ in range(100):
#         time.sleep(0.01)
#         for i in range(len(numbers)):
#             numbers[i] += 1
#
#
# if __name__ == "__main__":
#
#     shared_number = Value('i', 0)
#     print('Value at beginning: ', shared_number.value)
#
#     shared_array = Array('d', [0.0, 100.0, 200.0])
#     print('Array at beginning: ', shared_array[:])
#
#     process1 = Process(target=add_100, args=(shared_number,))
#     process2 = Process(target=add_100, args=(shared_number,))
#
#     process3 = Process(target=add_100_array, args=(shared_array,))
#     process4 = Process(target=add_100_array, args=(shared_array,))
#
#     process1.start()
#     process2.start()
#     process3.start()
#     process4.start()
#
#     process1.join()
#     process2.join()
#     process3.join()
#     process4.join()
#
#     print('Value at end:', shared_number.value)
#     # due to race condition the output may be incorrect so using lock in next code
#     print('Array at end:', shared_array[:])
#
#     print('end main')

"""
How to use Locks
Notice that in the above example, the 2 processes should increment the shared value by 1 for 100 times. 
This results in 200 total operations. But why is the end value not 200?

Race condition¶
A race condition happened here. A race condition occurs when two or more processes or threads can 
access shared data and they try to change it at the same time. 
In our example the two processes have to read the shared value, increase it by 1, and write it back 
into the shared variable. If this happens at the same time, the two processes read the same value, 
increase it and write it back. 
Thus, both processes write the same increased value back into the shared object, 
and the value was not increased by 2. 
See https://www.python-engineer.com/learn/advancedpython16_threading/ 
for a detailed explanation of race conditions.

Avoid race conditions with Locks¶
A lock (also known as mutex) is a synchronization mechanism for enforcing limits on access 
to a resource in an environment where there are many processes/threads of execution. 
A Lock has two states: locked and unlocked. If the state is locked, it does not allow other 
concurrent processes/threads to enter this code section until the state is unlocked again.

Two functions are important: 
- lock.acquire() : This will lock the state and block 
- lock.release() : This will unlock the state again.

Important: You should always release the block again after it was acquired!

In our example the critical code section where the shared variable is read and increased is now locked. 
This prevents the second process from modyfing the shared object at the same time. 
Not much has changed in our code. All new changes are commented in the code below.

"""

# # import Lock
# from multiprocessing import Lock
# from multiprocessing import Process, Value, Array
# import time
#
# def add_100(number, lock):
#     for _ in range(100):
#         time.sleep(0.01)
#         # lock the state
#         lock.acquire()
#         number.value += 1
#         # unlock the state
#         lock.release()
#
# def add_100_array(numbers, lock):
#     for _ in range(100):
#         time.sleep(0.01)
#         for i in range(len(numbers)):
#             lock.acquire()
#             numbers[i] += 1
#             lock.release()
#
#
# if __name__ == "__main__":
#
#     # create a lock
#     lock = Lock()
#
#     shared_number = Value('i', 0)
#     print('Value at beginning:', shared_number.value)
#
#     shared_array = Array('d', [0.0, 100.0, 200.0])
#     print('Array at beginning:', shared_array[:])
#
#     # pass the lock to the target function
#     process1 = Process(target=add_100, args=(shared_number, lock))
#     process2 = Process(target=add_100, args=(shared_number, lock))
#
#     process3 = Process(target=add_100_array, args=(shared_array, lock))
#     process4 = Process(target=add_100_array, args=(shared_array, lock))
#
#     process1.start()
#     process2.start()
#     process3.start()
#     process4.start()
#
#     process1.join()
#     process2.join()
#     process3.join()
#     process4.join()
#
#     print('Value at end:', shared_number.value)
#     print('Array at end:', shared_array[:])
#
#     print('end main')

"""
Use the lock as a context manager¶
After lock.acquire() you should never forget to call lock.release() to unblock the code. 
You can also use a lock as a context manager, wich will safely lock and unlock your code. 
It is recommended to use a lock this way:
def add_100(number, lock):
    for _ in range(100):
        time.sleep(0.01)
        with lock:
            number.value += 1
"""

"""
Using Queues in Python
Data can also be shared between processes with a Queue. 
Queues can be used for thread-safe/process-safe data exchanges and data processing both 
in a multithreaded and a multiprocessing environment, which means you can avoid having 
to use any synchronization primitives like locks.

The queue
A queue is a linear data structure that follows the First In First Out (FIFO) principle. 
A good example is a queue of customers that are waiting in line, where the customer that 
came first is served first.

"""

# from multiprocessing import Queue
#
# # create queue
# q = Queue()
#
# # add elements
# q.put(1) # 1
# q.put(2) # 2 1
# q.put(3) # 3 2 1
#
# # now q looks like this:
# # back --> 3 2 1 --> front
#
# # get and remove first element
# first = q.get() # --> 1
# print(first)
#
# # q looks like this:
# # back --> 3 2 --> front


"""
Using a queue in multiprocessing: Operations with a queue are process-safe. 
The multiprocessing Queue implements all the methods of queue.Queue except for task_done() and join(). 

Important methods are:
q.get() : Remove and return the first item. By default, it blocks until the item is available.
q.put(item) : Puts element at the end of the queue. By default, it blocks until a free slot is available.
q.empty() : Return True if the queue is empty.
q.close() : Indicate that no more data will be put on this queue by the current process.
"""

# # communicate between processes with the multiprocessing Queue
# # Queues are thread and process safe
# from multiprocessing import Process, Queue
#
# def square(numbers, queue):
#     for i in numbers:
#         queue.put(i*i)
#
# def make_negative(numbers, queue):
#     for i in numbers:
#         queue.put(i*-1)
#
# if __name__ == "__main__":
#
#     numbers = range(1, 6)
#     q = Queue()
#
#     p1 = Process(target=square, args=(numbers,q))
#     p2 = Process(target=make_negative, args=(numbers,q))
#
#     p1.start()
#     p2.start()
#
#     p1.join()
#     p2.join()
#
#     # order might not be sequential
#     while not q.empty():
#         print(q.get())
#
#     print('end main')


""""
Process Pools:
A process pool object controls a pool of worker processes to which jobs can be submitted 
It supports asynchronous results with timeouts and callbacks and has a parallel map implementation. 
It can automatically manage the available processors and split data into smaller chunks which can 
then be processed in parallel by different processes. 
See https://docs.python.org/3.7/library/multiprocessing.html#multiprocessing.pool for all possible methods. 

Important methods are:
1. map(func, iterable[, chunksize]) : This method chops the iterable into a number of chunks which it 
submits to the process pool as separate tasks. 
The (approximate) size of these chunks can be specified by setting chunksize to a positive integer. 
It blocks until the result is ready.

2. close() : Prevents any more tasks from being submitted to the pool. 
Once all the tasks have been completed the worker processes will exit.

3. join(): Wait for the worker processes to exit. 
One must call close() or terminate() before using join().
apply(func, args): Call func with arguments args. 
It blocks until the result is ready. 
func is only executed in ONE of the workers of the pool.

Note: There are also asynchronous variants map_async() and apply_async() that will not block. 
They can execute callbacks when the results are ready.
"""

from multiprocessing import Pool


def cube(number):
    return number * number * number


if __name__ == "__main__":
    numbers = range(10)

    p = Pool()

    # by default this allocates the maximum number of available
    # processors for this task --> os.cpu_count()
    result = p.map(cube,  numbers)
    # result = [p.apply(cube, args=(i,)) for i in numbers]

    p.close()
    p.join()

    print(result)





