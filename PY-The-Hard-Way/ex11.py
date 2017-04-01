# -*- coding: utf-8 -*-

print "How old are you?"
age = raw_input()
print "How tall are you?"
height = raw_input()
print "How much do you weight?"
weight = raw_input()

print "So, you're %r old, %r tall and %r heavy." % (age, height, weight)

# show menu
print (30 * "-")
print ("	M A I N - M E N U")
print (30 * "-")
print ("1. Backup")
print ("2. User management")
print ("3. Reboot the serve")
print (30 * "-")

# get input
choice = raw_input("Enter your choic [1-3]: ")

# convert string to int type
choice = int(choice)

# Take action as per selected menu-option
if choice == 1:
	print ("Starting backup...")
elif choice == 2:
	print ("Starting user management...")
elif choice == 3:
	print ("Rebooting the sever...")
else: # default
	print ("Invalid number. Try again...")