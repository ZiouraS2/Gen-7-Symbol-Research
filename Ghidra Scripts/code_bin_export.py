#TODO write a description for this script
#@author 
#@category Symbol
#@keybinding 
#@menupath 
#@toolbar 
#@runtime Jython


import os

symbolTable = currentProgram.getSymbolTable()
functionSymbols = symbolTable.getAllSymbols(True)

strsizelen = 0
strtypelen = 4
straccesslen = 5
strsymbollen = 0
straddresslen = 0

#for size calc
prevaddrchecked = 0

#clear output
clear = lambda: os.system('cls')
clear()

#calc biggest string for each
for sym in functionSymbols:
    namespace = sym.getParentNamespace().getName(True)  
    addr = sym.getAddress()
    name = sym.getName()
    if "DAT_" not in name and "FUN_" not in name and "SUB_" not in name and "LAB_" not in name and "caseD_" not in name and "switchD" not in name and "switchdataD_" not in name:
	if "s_" not in name[:3] and "u_" not in name[:3]:
		if name != "default":
			if str(sym.getParentNamespace()) != "Global" and "switchD" not in str(sym.getParentNamespace()):
    				name = str(sym.getParentNamespace())+"::"+sym.getName()
			if len(name) > strsymbollen:
    				strsymbollen = len(name)
			if len(str(addr.getOffset())) > straddresslen:
				straddresslen = len(" @ "+str(addr.getOffset()))
			if len(str(addr.getOffset() - prevaddrchecked)) > strsizelen:
				strsizelen = len(str(addr.getOffset() - prevaddrchecked))
    if "DAT_" not in name and "+" not in name:
	prevaddrchecked = addr.getOffset()

#actually print stuff
prevaddrchecked2 = 0
strsizelen = strsizelen + 2
strtypelen = strtypelen + 2
straccesslen = straccesslen + 2
strsymbollen = strsymbollen + 2
print("Size"+" "*(strsizelen-4)+"Type"+" "*(strtypelen-4)+"Access"+" "*(straccesslen-6)+"Symbol"+" "*(strsymbollen-6)+"Address"+" "*straddresslen)
print("---------------------------------------------------------------")

functionSymbols2 = symbolTable.getAllSymbols(True)

for sym in functionSymbols2:
    name = sym.getName()
    addr = sym.getAddress()
    size = addr.getOffset() - prevaddrchecked2
    type1 = "Code"
    access = "RO" 

    if addr.getOffset() >= 4956160:
	type1 = "Data"
    if addr.getOffset() >= 5664768:
	access = "RW"
    if "DAT_" not in name and "FUN_" not in name and "SUB_" not in name and "LAB_" not in name and "caseD_" not in name and "switchD" not in name and "switchdataD_" not in name and "+" not in name:
	if "s_" not in name[:3] and "u_" not in name[:3]:
		if name != "default":
			if str(sym.getParentNamespace()) != "Global" and "switchD" not in str(sym.getParentNamespace()):
    				name = str(sym.getParentNamespace())+"::"+sym.getName()
    			print(str(size)+" "*(strsizelen- len(str(size)) )+type1+" "*(strtypelen- len(str(type1)) )+access+" "*(straccesslen- len(str(access)) )+name+" "*(strsymbollen- len(name) )+str(" @ "+hex(addr.getOffset())).split("L")[0]+" "*(straddresslen- len(" @ "+str(addr.getOffset())) ))
    if "DAT_" not in name and "+" not in name:
	prevaddrchecked2 = addr.getOffset()
