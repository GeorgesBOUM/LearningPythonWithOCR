"""
---------------------
Control structures :
---------------------
an app telling if a  
given year is leap or
not
"""

year = input("choose a year: ")

try:
	year = int(year)
	assert(year > 0)
except ValueError:
	print("you did not type an integer")
except AssertionError:
	print("you did not type an integer greater than 0")
else:
	print("you typed "+str(year))
	if (year % 4 == 0):
		if (year % 100 == 0):
			if (year % 400 == 0):
				print("{} is a leap year".format(year))
			else:
				print("{} is not a leap year".format(year))
		else:
			print("{} is a leap year".format(year))
	else:
		print("{} is not a leap year".format(year))


