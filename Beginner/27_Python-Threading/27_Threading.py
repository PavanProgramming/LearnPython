"""
How to create and start multiple threads
How to wait for threads to complete
How to share data between threads
How to use Locks to prevent race conditions
What is a daemon thread
How to use a Queue for thread-safe data/task processing.
"""

"""
Create and run threads:
You create a thread with threading.Thread(). It takes two important arguments:

target: a callable object (function) for this thread to be invoked when the thread starts
args: the (function) arguments for the target function. This must be a tuple
Start a thread with thread.start()

Call thread.join() to tell the program that it should wait for this thread to 
complete before it continues with the rest of the code.
"""
# Threads basics: Explanation of code after implementation
# from threading import Thread
#
# def square_numbers():
#     for i in range(100):
#         result = i * i
#
#
# if __name__ == "__main__":
#     threads = []
#     num_threads = 10
#
#     # create threads and asign a function for each thread
#     for i in range(num_threads):
#         thread = Thread(target=square_numbers)
#         threads.append(thread)
#
#     # start all threads
#     for thread in threads:
#         thread.start()
#
#     # wait for all threads to finish
#     # block the main thread until these threads are finished
#     for thread in threads:
#         thread.join()

"""
Share data between threads:
Since threads live in the same memory space, they have access to the same (public) data. 
Thus, you can for example simply use a global variable to which all threads have read and write access.

Task: Create two threads, each thread should access the current database value, 
modify it (in this case only increase it by 1), and write the new value back into the database value. 
Each thread should do this operation 10 times.
"""

# # Race condition in threads
# from threading import Thread
# import time
#
# # all threads can access this global variable
# database_value = 0
#
# def increase():
#     global database_value # needed to modify the global value
#     # get a local copy (simulate data retrieving)
#     local_copy = database_value
#     # simulate some modifying operation
#     local_copy += 1
#     time.sleep(0.1)
#     # write the calculated new value into the global variable
#     database_value = local_copy
#
#
# if __name__ == "__main__":
#
#     print('Start value: ', database_value)
#
#     t1 = Thread(target=increase)
#     t2 = Thread(target=increase)
#
#     t1.start()
#     t2.start()
#
#     t1.join()
#     t2.join()
#
#     print('End value: ', database_value)
#
#     print('end main')

# explanation about above code
"""
Notice that in the above example, the 2 threads should increment the value by 1, 
so 2 increment operations are performed. But why is the end value 1 and not 2?

Race condition¶
A race condition happened here. A race condition occurs when two or more threads 
can access shared data and they try to change it at the same time.
Because the thread scheduling algorithm can swap between threads at any time, 
you don't know the order in which the threads will attempt to access the shared data. 
In our case, the first thread accesses the database_value (0) and stores it in a local copy. 
It then increments it (local_copy is now 1). With our time.sleep() function that 
just simulates some time consuming operations, the programm will swap to the second thread 
in the meantime. This will also retrieve the current database_value (still 0) 
and increment the local_copy to 1. Now both threads have a local copy with value 1, 
so both will write the 1 into the global database_value. This is why the end value is 1 and not 2.

Avoid race conditions with Locks
"""

# Avoid race conditions with Locks:
"""
A lock (also known as mutex) is a synchronization mechanism for enforcing limits on access 
to a resource in an environment where there are many threads of execution. 
A Lock has two states: locked and unlocked. If the state is locked, 
it does not allow other concurrent threads to enter this code section until the state is unlocked again.

Two functions are important: 
- lock.acquire() : This will lock the state and block 
- lock.release() : This will unlock the state again.

Important: You should always release the block again after it was acquired!

In our example the critical code section where database values are retrieved and modified is now locked. 
This prevents the second thread from modifying the global data at the same time. 
Not much has changed in our code. All new changes are commented in the code below.
"""
#
# # import Lock
# from threading import Thread, Lock
# import time
#
# database_value = 0
#
# def increase(lock):
#     global database_value
#
#     # lock the state
#     lock.acquire()  # you can also use lock as a context manager
#
#     local_copy = database_value
#     local_copy += 1
#     time.sleep(0.1)
#     database_value = local_copy
#
#     # unlock the state
#     lock.release()
#
#
# if __name__ == "__main__":
#
#     # create a lock
#     lock = Lock()
#
#     print('Start value: ', database_value)
#
#     # pass the lock to the target function
#     t1 = Thread(target=increase, args=(lock,))  # notice the comma after lock since args must be a tuple
#     t2 = Thread(target=increase, args=(lock,))
#
#     t1.start()
#     t2.start()
#
#     t1.join()
#     t2.join()
#
#     print('End value:', database_value)
#
#     print('end main')

# After lock.acquire() you should never forget to call lock.release() to unblock the code.
# You can also use a lock as a context manager, wich will safely lock and unlock your code.
# It is recommended to use a lock this way:

# # Lock using context manager
# from threading import Thread, Lock
# import time
#
# database_value = 0
#
# def increase(lock):
#     global database_value
#
#     # lock the state
#     with lock:  # using lock with context manager
#         # unlock the lock at out of scope
#         local_copy = database_value
#         local_copy += 1
#         time.sleep(0.1)
#         database_value = local_copy
#
#
# if __name__ == "__main__":
#
#     # create a lock
#     lock = Lock()
#
#     print('Start value: ', database_value)
#
#     # pass the lock to the target function
#     t1 = Thread(target=increase, args=(lock,))  # notice the comma after lock since args must be a tuple
#     t2 = Thread(target=increase, args=(lock,))
#
#     t1.start()
#     t2.start()
#
#     t1.join()
#     t2.join()
#
#     print('End value:', database_value)
#     print('end main')

# Queues in Python
"""
Queues can be used for thread-safe/process-safe data exchanges and data processing 
both in a multithreaded and a multiprocessing environment.

The queue: A queue is a linear data structure that follows the 
First In First Out (FIFO) principle. A good example is a queue of customers 
that are waiting in line, where the customer that came first is served first.

Operations with a queue are thread-safe. Important methods are:
1. q.get() : Remove and return the first item. 
By default, it blocks until the item is available.
2. q.put(item) : Puts element at the end of the queue. 
By default, it blocks until a free slot is available.
3. q.task_done() : Indicate that a formerly enqueued task is complete. 
For each get() you should call this after you are done with your task for this item.
4. q.join() : Blocks until all items in the queue have been gotten and 
processed (task_done() has been called for each item).
5. q.empty() : Return True if the queue is empty.
"""

# from queue import Queue
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
#
# q.task_done()


# from threading import Thread, Lock, current_thread
# from queue import Queue
#
# def worker(q, ):
#     while True:
#         value = q.get()  # blocks until the item is available
#
#         # do stuff...
#
#             # prevent printing at the same time with this lock
#         print(f"in {current_thread().name} got {value}")
#         # ...
#
#         # For each get(), a subsequent call to task_done() tells the queue
#         # that the processing on this item is complete.
#         # If all tasks are done, q.join() can unblock
#         q.task_done()
#
#
# if __name__ == '__main__':
#     q = Queue()
#     num_threads = 10
#     lock = Lock()
#
#     for i in range(num_threads):
#         t = Thread(name=f"Thread{i+1}", target=worker, args=(q, ))
#         t.daemon = True  # dies when the main thread dies
#         t.start()
#
#     # fill the queue with items
#     for x in range(1, 21):
#         q.put(x)
#
#     q.join()  # Blocks until all items in the queue have been gotten and processed.
#
#     print('main done')

# above multiple threads trying to write at the same time so we use lock

from threading import Thread, Lock, current_thread
from queue import Queue

def worker(q, lock):
    while True:
        value = q.get()  # blocks until the item is available

        # do stuff...
        with lock:
            # prevent printing at the same time with this lock
            print(f"in {current_thread().name} got {value}")
        # ...

        # For each get(), a subsequent call to task_done() tells the queue
        # that the processing on this item is complete.
        # If all tasks are done, q.join() can unblock
        q.task_done()


if __name__ == '__main__':
    q = Queue()
    num_threads = 10
    lock = Lock()

    for i in range(num_threads):
        t = Thread(name=f"Thread{i+1}", target=worker, args=(q, lock))
        t.daemon = True  # dies when the main thread dies , default value is False
        # so thats why while loop is not infinite
        t.start()

    # fill the queue with items
    for x in range(20):
        q.put(x)

    q.join()  # Blocks until all items in the queue have been gotten and processed.

    print('main done')


"""
Daemon threads: In the above example, daemon threads are used. 
Daemon threads are background threads that automatically die when the main program ends. 
This is why the infinite loops inside the worker methods can be exited. 
Without a daemon process we would have to use a signalling mechanism such as a threading.
Event to stop the worker. But be careful with daemon processes: 
They are abruptly stopped and their resources (e.g. open files or database transactions) 
may not be released/completed properly.
"""
