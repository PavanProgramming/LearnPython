# Exception: even if a statement is syntactically correct if it cause an error
# when it is executed and this is called an exception error

# # raising exceptions
# x = 5
# if x < 0:
#     raise Exception('x should be positive')
#
# # assert statement : returns assertion error if assertion is not true
# x = -5
# # assert (x>=0)  # without message
# assert (x>=0), 'x should be positive'  # with assert statement

# try:
#     pass
# except Exception:
#     pass
# else:
#     pass
# finally:
#     pass

# try:
#     x = 15 + a
# except Exception:
#     print("Invalid types")

# try:
#     x = 15 + 'a'
#     f = open('file.txt')
# except NameError:
#     print("Invalid types")
# except FileNotFoundError:
#     print('file is not present')
# except Exception as e:
#     print(e)
# else:   # if no exceptions then else class will run
#     print(f.read())
#     f.close()
# finally:  # code regardless of exceptions is successful or not
#     print("Executing finally...")
#


