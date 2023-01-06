# File Objects

# The Basics:
# f = open("test.txt", "r")
# f = open("test.txt", "w")
# f = open("test.txt", "a")
f = open("test.txt", "r+")
print(f.name)
print(f.mode)
f.close()
print("***********************")
# Reading Files:
with open("test.txt", "r") as f:
    pass
# automatically file close will happen
# print(f.read()) # results error as I/O operation on closed file.
print("***********************")
with open("test.txt", "r") as f:
    f_contents = f.read()
    print(f_contents)

print("***********************")
# #Small Files:
with open("test.txt", "r") as f:
    f_contents = f.readlines() # create individual lines as items in the list
    print(f_contents)
print("***********************")

# #With the extra lines:
with open("test.txt", "r") as f:
    f_contents = f.readline() # read a single line
    print(f_contents)
    f_contents = f.readline()  # read a single line
    print(f_contents, end = '')
    f_contents = f.readline()  # read a single line
    print(f_contents)
print("***********************")

# ##Iterating through the file:
with open("test.txt", "r") as f:
    for x in f:
        print(x, end = ' ')
print("***********************")

# Going Back....: reading full file
with open("test.txt", "r") as f:
    f_contents = f.read()
    print(f_contents, end = ' ')
print('')
print("***********************")

# Printing by no.(100) of characters:
with open("test.txt", "r") as f:
    f_contents = f.read(15)
    print(f_contents, end = ' ')
print('')
print("***********************")


# Iterating through small chunks:
# Printing by no.(100) of characters:
with open("test.txt", "r") as f:
    size_to_read = 30
    f_contents = f.read(size_to_read)
    while len(f_contents) > 0:
        print(f.tell())  # it will tell the current position
        print(f_contents, end ='***')
        f_contents = f.read(size_to_read)

print('')
print("***********************")

# to move the reading position to particular location
with open("test.txt", "r") as f:
    size_to_read = 30
    f.seek(60) # to move the reading position to particular location
    f_contents = f.read(size_to_read)
    while len(f_contents) > 0:
        print(f.tell())  # it will tell the current position
        print(f_contents, end ='***')
        f_contents = f.read(size_to_read)

print('')
print("***********************")

print(f.mode)
print(f.closed)



# #Writing Files:
# it will overwrite the previous data
with open("test.txt", "r") as f:
    pass
    #f.write("Test")  # The Error: bcz trying to write reading mode file

# ##Writing Starts: # if file is not available the it will create
with open("test2.txt", "w") as f:
    f.write("Test")
    f.write("Test")
    f.seek(0)
    f.write("R")

# #Copying Files:
with open("test.txt", "r") as rf:
    with open("test_copy.txt", "w") as wf:
        for line in rf:
            wf.write(line)

#  Copying the/your image:
# The Error because of UnicodeDecodeError
#with open("peacock.jpg", "r") as rf:
    #with open("peacock_copy.jpg", "w") as wf:
        #for line in rf:
            #wf.write(line)

# Copying the image with binary mode
# https://docs.python.org/3/library/functions.html#open
# Files opened in binary mode (including 'b' in the mode argument) return contents as bytes objects without any decoding
# In text mode (the default, or when 't' is included in the mode argument), the contents of the file are returned as str
# Python doesn’t depend on the underlying operating system’s notion of text files;
# all the processing is done by Python itself, and is therefore platform-independent.

# copying the image line by line
with open("peacock.jpg", "rb") as rf:
    with open("peacock_copy.jpg", "wb") as wf:
        for line in rf:
            wf.write(line)

# Copying the image with chunk size:
with open("peacock.jpg", "rb") as rf:
    with open("peacock_copy2.jpg", "wb") as wf:
        chunk_size = 2 # chunk_size = 4096
        rf_chunk = rf.read(chunk_size)
        while len(rf_chunk) > 0:
            wf.write(rf_chunk)
            rf_chunk = rf.read(chunk_size)
