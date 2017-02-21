input = {}
input["A"] = [(2.3, "f"), (0.01, "g"), (0.3, "h")]
input["B"] = [(0.3001,"i"), (0.01,"j"), (9.3,"kx")]
input["C"] = [(1000.7,"l"), (9.3,"m"), (9.2999,"n")]

output = set()
for k,v in input.items():	# map iteration
	# comprehension with conditional expression; lambda invocation; tuple creation
	x = [(lambda element: element)((k,element[1])) for element in v if element[0]>=0.3 and element[0]>=9.3]
	output |= set(x)	# add set to set

print(output)
