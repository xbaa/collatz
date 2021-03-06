import collatz
import pseudo_mod_converter
import leveldic

"""Returns False if list_of_run[n] equals zero"""
#this part doesn't take into account having a non-zero start number.  currently handled when calling this procedure.
def check(n,run_list):
	if run_list[n] == 0:
		return False

"""Accepts a start and stop number, then populates a list with the appropriate power of two by calling collatz"""
def run_range(start,stop):
	test_dic = {}
	run_list = [0] * (stop-start+1) #can be handled by populist() when we finish that.
	level_dic = leveldic.load_leveldic()
#	run_list = mysql_module.populist(start,stop,run_list)
	test_num = start
	while  test_num <= stop:
		if check((test_num-start),run_list) == False:
			power_of_two, level = collatz.collatz(pseudo_mod_converter.mod52dec(test_num))
			if power_of_two not in level_dic:
				level_dic[power_of_two] = level
			elif level_dic[power_of_two] != level:
				print("We have found a discrepancy between level and power_of_two in test_num " + str(test_num+start))
			add_to_db(test_num,power_of_two,level)
			#This while loop is just to fill run_list with identically permuted numbers.  It's irrelevant once we are at numbers higher than we can fit in RAM.
			x = test_num
			while x < stop:
				run_list[(x-start)] = 1
				x += 5 * (2**(power_of_two-5))
		test_num += 1
	leveldic.save_leveldic(level_dic)
	#mysql_module.mysql_dump(test_dic) #this will send all the test_dic info to be saved on MySQL

"""Adds entry to test_dic."""
def add_to_db(n,power_of_two,level):
	if power_of_two in test_dic:
		test_dic[power_of_two].append(n)
	else:
		test_dic[power_of_two] = [n]

#def populist(start,stop,list):
	#MySQL jibberish.  Use all numbers that repeat within "stop".  Some won't exist at all, but we definitely won't miss any.

test_range = 100000
#test_range = 1093750000 #7 billion
#test_range = 937500000 #6 billion
#test_range = 781250000 #5 billion
#test_range = 625000000 #4 billion
#test_range = 468750000 #3 billion
#test_range = 156250000 #billion
run_range(0,test_range)
#for i in test_dic:
#	print("Level " + str(i) + " " + str(len(test_dic[i])))

