#!/usr/bin/python3

# powerset is the set of all subsets
# count = n² (inclusive empty set)

def generatePowerset(soFar, rest):
	if(rest == ""):
		print("["+soFar+"]")
	else:
		generatePowerset(soFar, rest[1:])	#don't take it
		generatePowerset(soFar + rest[0], rest[1:])	#take it

generatePowerset("","ab")
