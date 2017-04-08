# Catching Exceptions in Python

# import module sys to get the type of exception
import sys

random_list = ['a', 0, 2]

for entry in random_list:
    try:
        print "The entry is", entry
        r = 1.0/int(entry)
        break
    except:
        print "Oops!", sys.exc_info()[0], "occured!"
        print "Next entry.\n"

print "The reciprocal of %r is %.3f." % (entry, r)

# catching specific exceptions in Python
try:
    # do something
    pass
except ValueError:
    # hanle ValueError exception
    pass
except (TypeError, ZeroDivisionError):
    # handle multiple exceptions
    # TypeError and ZeroDivisionError
    pass
except:
    # handle all other exceptions
    pass

# Raising Exceptions

# raise KeyboardInterrupt

raise MemoryError("This is an Argument")

# try:
#     a = int(raw_input("Enter a positive interger: "))
#     if a <= 0:
#         raise ValueError("This is not a positive number!")
#     except ValueError as ve:
#         print(ve)

# try ... finally

# try:
#     f = open('test.txt', encoding = 'utf-8')
# finally:
#     f.close()