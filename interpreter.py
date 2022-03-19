import linecache
import time
from py_expression_eval import Parser
calc = Parser()

vars = {
        
    }

def variable(name, value):
    vars[name] = value
    
def sage(string):
    if CheckVar(string[5:].strip('\n')) == True:
        print(vars[string[5:].strip('\n')])
    else:
        print(string[5:])

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
                opcount = 1
            else:
                if CheckVar(item) == True:
                    for i, n in enumerate(operation_list):
                        if n == item:
                            operation_list = [w.replace(item, str(vars[item])) for w in operation_list]
        operation = calc.parse(" ".join(operation_list))
        return operation.evaluate({})
    else:
        return False


script = open("fahrt1.lego", "r")

for line in script:
    if line.startswith("setze"):
        args = line.split()
        name = args[1]
        args = args[3:]
        value = " ".join(args)
        if CheckOperation(value) == True:
            value = DoOperation(value)
        variable(name, value)
    else:
        if line.startswith("sage"):
            sage(line)
            