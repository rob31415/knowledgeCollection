input = {}
input["A"] = [(2.3, "f"), (0.01, "g"), (0.3, "h")]
input["B"] = [(0.3001,"i"), (0.01,"j"), (9.3,"kx")]
input["C"] = [(1000.7,"l"), (9.3,"m"), (9.2999,"n")]

output = set()
for k,v in input.items():	# map iteration
	# A = comprehension with conditional expression (alt. to filtering); B = lambda invocation; C = tuple creation
	#                             BC                                A                                    
	x = [(lambda element: element)((k,element[1])) for element in v if element[0]>=0.3 and element[0]<9.3]
	output |= set(x)	# make set from list, add that to set

print(output)
