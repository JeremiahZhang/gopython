"""Given a year, determine whether it is a leap year. 
If it is a leap year, return the Boolean True, 
otherwise return False.

3 conditions are used to identify leap years:
The year can be evenly divided by 4, is a leap year, unless:
	The year can be evenly divided by 100, it is NOT a leap year, unless:
		The year is also evenly divisible by 400. Then it is a leap year.

This means that in the Gregorian calendar, the years 2000 and 2400 are
leap years, while 1800, 1900, 2100, 2200, 2300 and 2500 
are NOT leap years.
"""


def is_leap(year):
	leap = False

	if (year%100 == 0) & (year%400 ==0):
		leap = True
	elif (year%4==0) & ((year%100) !=0):
		leap = True

	return leap

def main():
	year = int(input("Enter the year to determine -->"))
	answer = is_leap(year)
	
	print(answer)

if __name__ == '__main__':
	main()