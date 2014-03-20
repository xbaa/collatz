import collatz

"""Returns False if list_of_run[n] equals zero"""
#this part doesn't take into account having a non-zero start number.  currently handled when calling this procedure.
def check(n,run_list):
	if run_list[n] == 0:
		return False

"""Accepts a start and stop number, then populates a list with the appropriate power of two by calling collatz"""
def run_range(start,stop):
	run_list = [0] * (stop-start)
#	populist(start,stop,run_list)
	test_num = start
	while  test_num < stop:
		if check((test_num-start),run_list) == False:
			power_of_two, level = collatz.collatz(mod52dec(test_num))
			add_to_db(test_num,power_of_two,level)
#This while loop is just to fill run_list with identically permuted numbers.  It's irrelevant once we are at numbers higher than we can fit in RAM.
			x = test_num
			while x < stop:
				run_list[(x-start)] = 1
				x += 5 * (2**(power_of_two-5))
		test_num += 1
	#when we reach here, we can send something back to MySQL proving we've completed this group of numbers.

test_dic = {} #just using to test speed compared to older collatz program.

"""Adds entry to MySQL Database.  Requires open MySQL connection."""
def add_to_db(n,power_of_two,level):
	#MySQL jibberish.  Add the level (i.e. len(permut)) to MySQL.  Then we can later confirm level is the same for all power_of_two.
	if power_of_two in test_dic:
		test_dic[power_of_two].append(n)
	else:
		test_dic[power_of_two] = [n]  #this is just for testing before we set up MySQL

#def populist(start,stop,list):
	#MySQL jibberish.  Use all numbers that repeat within "stop".  Some won't exist at all, but we definitely won't miss any.

#Doesn't accept any decimal.  Only accepts if it fits within the scheme of 7, 15, 23, 27, 31, 39... (i.e. odd numbers beyond Level 2)
def dec2mod5(n):
	modlist = {7:0,15:1,23:2,27:3,31:4}
	x = (n % 32)
	multiplier = (n-x)/32
	mod5 = (multiplier * 5) + modlist[x]
	return mod5

def mod52dec(n):
	modlist = [7,15,23,27,31]
	x = (n % 5)
	multiplier = (n - x)/5
	dec = (multiplier * 32) + modlist[x]
	return dec

#test_range = 100000
#test_range = 1093750000 #7 billion
#test_range = 937500000 #6 billion
#test_range = 781250000 #5 billion
#test_range = 625000000 #4 billion
test_range = 468750000 #3 billion
#test_range = 156250000 #billion
run_range(0,test_range)
for i in test_dic:
	print("Level " + str(i) + " " + str(len(test_dic[i])))
