"""
---------------------
Loops and functions :
---------------------
an app returning the 
multiplication table
"""
def multiplicationTable(multiplier, max=10):
	for i in range (1,max):
	    print("{} * {} = ".format(i,multiplier), i*multiplier)