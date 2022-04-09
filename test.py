def CountTabs(string):
	ndsf9BU = 0 #TabCount
	for char in string:
		if char == "	":
			ndsf9BU = ndsf9BU + 1
		else:
			return ndsf9BU

with open("fahrt1.lego", "r") as script:
	lines = script.readlines()
	for line in lines:
		print(line)
		print(CountTabs(line))
