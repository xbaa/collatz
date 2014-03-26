"This module saves a dictionary linking power_of_two to level so we can confirm there are no inconsistencies."
import json

def save_leveldic(leveldic):
	with open("levels.json","wb") as fp:
		json.dump(leveldic,fp)

def load_leveldic():
	try:
		with open("levels.json", "rb") as fp:
			leveldic_prep = json.load(fp) #needed because JSON stores dictionary keys as strings
			leveldic ={} # ""
			for i in leveldic_prep: #""
				leveldic[int(i)] = leveldic_prep[i] #""
			return leveldic
	except:
		leveldic = {}
		return leveldic

def print_leveldic(leveldic):
	print json.dumps(leveldic,sort_keys=True,indent=1)

#print_leveldic(load_leveldic()) #prints the levels.json file in a readable format
