import linecache
from py_expression_eval import Parser

from interpreter import LineInterpreter
calc = Parser()

vars = {
        
    }

tabs = {

}

liinecount = 0


def sage(string):
	args = string.split("")
	args.strip('\n')
	args.pop(0)
	if CheckVar("".join(args)) == True:
		print(vars["".join(args)])
	else:
		print("".join(args))

def CountTabs(string):
	TabCount = 0 
	for char in string:
		if char == "	":
			TabCount = TabCount + 1
		else:
			return TabCount

def CheckVar(string):
    if string in vars:
        return True

def CheckOperation(string):
    if str(string).find("+") != -1 or str(string).find("-") != -1 or str(string).find("*") != -1 or str(string).find("/") != -1:
        return True
    else:
        return 

def DoOperation(string):
    if CheckOperation(string):
        operation_list = string.split()
        for item in operation_list:
            if item.startswith("+") == True or item.startswith("-") == True or item.startswith("*") == True or item.startswith("/") == True:
                pass
            else:
                if CheckVar(item) == True:
                    for i, n in enumerate(operation_list):
                        if n == item:
                            operation_list = [w.replace(item, str(vars[item])) for w in operation_list]
        operation = calc.parse(" ".join(operation_list))
        operation_str = " ".join(operation_list)
        try:
            return operation.evaluate({})
        except:
            return operation_str
    else:
        return False

def variable(line):
	args = line.spit("")
	args.remove("setze")
	name = args[0]
	value = args[:2]
	if CheckVar(value) == True:
		value = vars[value]
	if CheckOperation(value) == True:
			value = DoOperation(value)
	vars[name] = value

def checkIfFalseOrTrue(args):
	for i in args:
		if CheckVar(i):
			for i2, n in enumerate(args):
				if CheckVar(n):
					args[i2] = str(vars[n])
		def falseortrue(operator):
			args2 = []
			#left of operator
			for i in args:
				if i == operator:
					break
				args2.append(i)
			args2str = "".join(args2)
			if CheckOperation(args2str):
				for i in args:
					if i == operator:
						break
					args.pop(0)
				args.insert(0, DoOperation(args2str))
			#right of operator
			args2 = []
			add = False
			for i in args:
				if add == True:
					args2.append(i)
				if i == operator:
					add = True
			args2str = "".join(args2)
			if CheckOperation(args2str):
				args = args[:args.index(operator)+1]
				args.append(DoOperation(args2str))
			if operator == "=":
				if str(args[0]) == str(args[2]):
					return  True
				else:
					return False
			if operator == "<":
				if str(args[0]) < str(args[2]):
					return  True
				else:
					return False
			if operator == ">":
				if str(args[0]) > str(args[2]):
					return  True
				else:
					return False
			if operator == ">=" or "=>":
				if str(args[0]) >= str(args[2]):
					return  True
				else:
					return False
			if operator == "<=" or "=<":
				if str(args[0]) <= str(args[2]):
					return  True
				else:
					return False
		if "=" in args:
			return falseortrue("=")
		if "<" in args:
			return falseortrue("<")
		if ">=" or "=>" in args:
			return falseortrue(">=")
		if "<=" or "=<" in args:
			return falseortrue("<=")
	
def falls(line):
	args = line.split("")
	args.remove("falls")
	if checkIfFalseOrTrue(args) == True:
		return True
	else:
		return False
	


def LineInterpreter(line):
	#"setze" Command (var)
	if line.startswith("setz"):
		variable(line)
	if line.startwith("sage"):
		sage(line)
	#"falls" Command
	if line.startswith("falls"):
		if falls(line) == True:
			return True
		else:
			return False

def interpreter(code, indent=0):
	skip = False
	code_backup = code 			# <-- creates a backup of tabs to prevent that the popitem function changes the behavior of the for loop
	for line in code_backup:
		tabs.popitem() 			# <-- removes first element of tabs dict, for the nested interpreters to start at the right line
		linetabs = CountTabs(line)
		if linetabs == indent:  # <-- check if loop is over (techically only needed when skip==True)
			skip=False
		if skip == True:
			if linetabs < indent:
				return
		else:
			LineInterpreter(line)# <-- execute code in line
			if LineInterpreter(line) == True or False:       # <-- Checks in LineInterpreter has detected a "falls" command
				skip = True                                  # <-- always sets skip to True, because even when the "falls" command is true the nested interpreter should execute it, not this one
				if LineInterpreter(line) == True:            # <-- only starts nested interpreter if the "falls" command should be executed
					interpreter(tabs)



	


with open("fahrt1.lego", "r") as script:
    lines = script.readlines()
    for line in lines:
        tabs[line.strip("	")] = [CountTabs(line)]
    interpreter(tabs)
    