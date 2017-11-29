# -*_ coding: utf-8 -*-

from sys import argv
import shutil

script, from_file, to_file = argv


f = open(to_file, "w+")
f.truncate()
print "The content of to_file: %r" % (f.read())
f.close()

shutil.copy(from_file, to_file) # This is one line

f = open(to_file, "r")
print "The content of to_file now: %r" % (f.read())
f.close()