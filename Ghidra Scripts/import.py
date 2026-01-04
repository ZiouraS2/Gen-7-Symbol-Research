#TODO write a description for this script
#@author 
#@category Symbol
#@keybinding 
#@menupath 
#@toolbar 
#@runtime Jython

from ghidra.program.model.symbol.SourceType import *
import string
import subprocess

functionManager = currentProgram.getFunctionManager()
symbolTable = currentProgram.getSymbolTable()
fille = askFile("Give me a file to open", "..")


#TODO Add User Code Here

with open(fille.getAbsolutePath(), 'r') as documentlines:
        for line in documentlines:
                if(line.find("@") != -1):
                    addresstr = (line.split(" @ ")[1].strip('\x00')).split("0x")[1]
                    addr = int(addresstr, 16)
                    if(line.find("RO") != -1):
                            funcnamestr = line.split(" @ ")[0].strip('\x00').split("RO")[1].strip('\x00')
                    if(line.find("RW") != -1):
                            funcnamestr = line.split(" @ ")[0].strip('\x00').split("RW")[1].strip('\x00')
                    funcnamestr = funcnamestr.strip('\x20') 
		    print(hex(addr).split("L")[0])
		    address = toAddr(hex(addr))
		    func = functionManager.getFunctionAt(address)
	            if func is not None:
                            old_name = func.getName()
                            old_namespace = func.getParentNamespace()
                            if str(func.getParentNamespace()) != "Global":
			           if (str(old_namespace)+"::"+old_name) == funcnamestr:
		                          print("Match Found in code, not renaming: "+(str(old_namespace)+"::"+old_name))
                                   else:
                                          print("No Function Name Match found, renaming")
                                          func.setNameandNamespace(funcnamestr,funcnamestr.split("::", 1),SourceType.IMPORTED)
                            elif str(old_name) == funcnamestr:
                                print("Match Found in code, not renaming: "+old_name)
                            else:
                                   print("No Match Found in code, renaming.")
                                   func.setNameandNamespace(funcnamestr,"Global",SourceType.IMPORTED)
	            else:
			    func = symbolTable.getPrimarySymbol(address)
                            old_name = func.getName()
                            if str(old_name) == funcnamestr:
		                   print("Match Found in data, not renaming: "+old_name)
                            else:
                                   print("No Data Name Match found, renaming.")
                                   func.setName(funcnamestr,SourceType.IMPORTED)