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

#calc biggest string for each and size table
sizetbl = [0,]
i = 0
for sym in functionSymbols:
    namespace = sym.getParentNamespace().getName(True)  
    addr = sym.getAddress()
    name = sym.getName()
    type1 = "Code"

    if addr.getOffset() >= 4956160:
	type1 = "Data"
    printstr = ""
    if i > 0:
        if "DAT_" not in name and "+" not in name or type1 == "Data":
            debugprevstart = sizetbl[i]
            sizetbl[i-1] = addr.getOffset() - sizetbl[i]
            #printstr = ("end: "+str(addr.getOffset())+" - start: "+str(debugprevstart)+" = "+str(sizetbl[i-1]))
    if "DAT_" not in name and "+" not in name or type1 == "Data":
        i = i + 1
        sizetbl.append(addr.getOffset())
    
    
    if "DAT_" not in name and "FUN_" not in name and "SUB_" not in name and "LAB_" not in name and "caseD_" not in name and "switchD" not in name and "switchdataD_" not in name and "+" not in name:
	if "s_" not in name[:3] and "u_" not in name[:3]:
		if name != "default":
			#print(i)        
			#print(addr.getOffset())
			#print(str(sym.getParentNamespace())+"::"+sym.getName()+" : "+printstr)
			if str(sym.getParentNamespace()) != "Global" and "switchD" not in str(sym.getParentNamespace()):
    				name = str(sym.getParentNamespace())+"::"+sym.getName()
			if len(name) > strsymbollen:
    				strsymbollen = len(name)
			if len(str(addr.getOffset())) > straddresslen:
				straddresslen = len(" @ "+str(addr.getOffset()))
			if len(str(addr.getOffset() - prevaddrchecked)) > strsizelen:
				strsizelen = len(str(addr.getOffset() - prevaddrchecked))
    

#actually print stuff
prevaddrchecked2 = 0
strsizelen = strsizelen + 2
strtypelen = strtypelen + 2
straccesslen = straccesslen + 2
strsymbollen = strsymbollen + 2
print("Size"+" "*(strsizelen-4)+"Type"+" "*(strtypelen-4)+"Access"+" "*(straccesslen-6)+"Symbol"+" "*(strsymbollen-6)+" Address"+" "*straddresslen)
print("---------------------------------------------------------------")

functionSymbols2 = symbolTable.getAllSymbols(True)
i2 = 0

for sym in functionSymbols2:
    name = sym.getName()
    addr = sym.getAddress()
    type1 = "Code"
    access = "RO" 

    if addr.getOffset() >= 4956160:
	type1 = "Data"
    if addr.getOffset() >= 5664768:
	access = "RW"
    
    if "DAT_" not in name and "+" not in name or type1 == "Data":
        i2 = i2 + 1
    size = sizetbl[i2]  
    
    if "DAT_" not in name and "FUN_" not in name and "SUB_" not in name and "LAB_" not in name and "caseD_" not in name and "switchD" not in name and "switchdataD_" not in name and "+" not in name:
	if "s_" not in name[:3] and "u_" not in name[:3]:
		if name != "default":
			if str(sym.getParentNamespace()) != "Global" and "switchD" not in str(sym.getParentNamespace()):
    				name = str(sym.getParentNamespace())+"::"+sym.getName()
    			print(str(size)+" "*(strsizelen- len(str(size)) )+type1+" "*(strtypelen- len(str(type1)) )+access+" "*(straccesslen- len(str(access)) )+name+" "*(strsymbollen- len(name) )+str(" @ "+hex(addr.getOffset())).split("L")[0]+" "*(straddresslen- len(str(addr.getOffset())) ))
