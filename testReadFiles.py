import re

# testing block
#####################################################
# test string methods

# string = "<!-- PJG FTAG 4700 -->"
# re.split('[a-f]+', '0a3B9',flags=re.IGNORECASE)
# print(string.startswith("<!--") and string.endswith("-->"))


testFile = open("test.tex")
lines = testFile.read().splitlines()
testFile.close()
lines = [i for i in lines if not isInvalidLine(i)] # comment line

print(lines)





# Output1
#####################################################
def isInvalidLine(s):
    
    # comments 
    if(s.startswith("<!--") and s.endswith("-->")): return True 
    
    # empty str
    if(not s):  return True
    
    # str of spaces
    if(s.isspace()): return True   
    
    # tags
    if(s in ['<DOC>','</DOC>','<TEXT>','</TEXT>']): return True
    
    # invalid line
    if(s.startswith('<PARENT>') and s.endswith('</PARENT>')): return True   
    
    
    

    
# Output2
#####################################################
# This method only reads a file that only has one document

### !!! UPDATE NEEDED LATER !!!
def getFileLines(fileName):
    
    
    testFile = open("test.tex")
    lines = testFile.read().splitlines()
    testFile.close()
    lines = [i for i in lines if not isInvalidLine(i)] # comment line
    
    return lines 
