#! /usr/bin/python3


def mergeTwoSortedLists(one, two):
	ret = []
	itOne = 0
	itTwo = 0
	run = True
	while(run):
		a = itOne<len(one)
		b = itTwo<len(two)
		if(a and b):
			if(one[itOne]<two[itTwo]):
				ret.append(one[itOne])
				itOne += 1
			else:
				ret.append(two[itTwo])
				itTwo += 1
		if(a and not b):
			ret.append(one[itOne])
			itOne += 1
		if(not a and b):
			ret.append(two[itTwo])
			itTwo += 1
		run = a or b
	print(one, two, " -> ", ret)
	return ret


def mergeSort(lst):
	if(len(lst)>1):
		split = int(len(lst)/2)
		one = mergeSort(lst[:split])
		two = mergeSort(lst[split:])
		return mergeTwoSortedLists(one, two)
	else:
		return lst

A = [6,7,2,1,99,4,3,1]
print(A)
mergeSort(A)

