import linecache
import time
from py_expression_eval import Parser
calc = Parser()

vars = {
        
    }

indents = {

}

liinecount = 0

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

def variable(name, value):
    if CheckVar(value) == True:
        value = vars[value]
    if CheckOperation(value) == True:
            value = DoOperation(value)
    vars[name] = value

def falls(args):
    args2 = []
    remove = False
    args.remove("falls")
    for i in args:
        if CheckVar(i):
            for i2, n in enumerate(args):
                if CheckVar(n):
                    args[i2] = str(vars[n])
        print(args)
    if "=" in args:
        #left of "="
        for i in args:
            if i == "=":
                break
            args2.append(i)
        args2str = "".join(args2)
        if CheckOperation(args2str):
            for i in args:
                if i == "=":
                    break
                args.pop(0)
            args.insert(0, DoOperation(args2str))
        #right of "="
        args2 = []
        add = False
        for i in args:
            if add == True:
                args2.append(i)
            if i == "=":
                add = True
        args2str = "".join(args2)
        if CheckOperation(args2str):
            args = args[:args.index('=')+1]
            args.append(DoOperation(args2str))
        if str(args[0]) == str(args[2]):
            return  True
        else:
            return False

def interpreter(code):
    skip = False
    for line in code:
        linecount = linecount + 1 
        if skip == True:
            if "end" in line:
                skip = False
            else:
                pass
        else:
            if line.startswith("end"):
                return        
            if line.startswith("setze"):
                args = line.split()
                name = args[1]
                args = args[3:]
                value = " ".join(args)
                variable(name, value)
            if line.startswith("falls"):
                indents[linecount] = len(line) - len(line.lstrip("    "))
                args = line.split()
                if falls(args) == False:
                    skip = True
            if line.startswith("sage"):
                sage(line)
        lines.pop(0)

with open("fahrt1.lego", "r") as script:
    lines = script.readlines()
    interpreter(script)
    
