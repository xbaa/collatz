"""Doesn't accept any decimal.  Only accepts if it fits within the scheme of 7, 15, 23, 27, 31, 39... (i.e. odd numbers beyond Level 2)"""
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
