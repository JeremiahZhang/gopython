import sys

try:
    f = open("fibo.py")
    s = f.readline()
    i = int(s.strip())
except IOError as e:
    print "I/O error({0}): {1}".format(e.errno, e.strerror)
except ValueError:
    print "Could not convert data to integer."
except:
    print "Unexpected error:", sys.exc_info()[0]
    raise
