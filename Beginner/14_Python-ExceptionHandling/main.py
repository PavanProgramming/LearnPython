
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

try:
    x = 15 + 'a'
    f = open('file.txt')
except NameError:
    print("Invalid types")
except FileNotFoundError:
    print('file is not present')
except Exception as e:
    print(e)
else:   # if no exceptions then else class will run
    print(f.read())
    f.close()
finally: # code regardless of exceptions is succesfull or not
    print("Executing finally...")

