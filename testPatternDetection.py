import re

# test string methods

# string = "<!-- PJG FTAG 4700 -->"
# re.split('[a-f]+', '0a3B9',flags=re.IGNORECASE)
# print(string.startswith("<!--") and string.endswith("-->"))


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
    

# This method only reads files that only has one document
### !!! UPDATE NEEDED LATER !!!
def getFileLines(fileName):
    
    
    testFile = open("test.tex")
    lines = testFile.read().splitlines()
    testFile.close()
    lines = [i for i in lines if not isInvalidLine(i)] # comment line
    
    return lines 
    
    
# after a doucment is read into a strList, parse the list to get dates
def getDates(word):
    dateRegex = r"\b(?:0?[1-9]|1[012]|January|Jan|Feburary|Feb|March|Mar|April|Apr|May|June|Jun|July|Jul|August|Aug|September|Sept|October|Oct|November|Nov|December|Dec)[-/, ]\s*(?:0?[1-9]|[12][0-9]|3[01])[-/,]\s*\d{4}\b"
    datePattern = re.compile(dateRegex,re.IGNORECASE)
    
    # find dates
    dates = datePattern.findall(word)
    
    # remove dates in word
    word = datePattern.sub("",word)
    
    return word, dates

def findPatterns(word):
    
    patterns = []
    
    # get dates
    ####################
    dateRegex = r"\b(?:0?[1-9]|1[012]|January|Jan|Feburary|Feb|March|Mar|April|Apr|May|June|Jun|July|Jul|August|Aug|September|Sept|October|Oct|November|Nov|December|Dec)[-/, ]\s*(?:0?[1-9]|[12][0-9]|3[01])[-/,]\s*\d{4}\b"
    datePattern = re.compile(dateRegex,re.IGNORECASE)
    
    # find dates
    patterns.extend(datePattern.findall(word))
    
    # remove dates in word
    word = datePattern.sub("",word)
    ####################
    
    
    
    # get digit-alphabet 
    ####################
    numAlphaRegex = r'\b\d+-[A-z]+\b'
    numAlphaPattern = re.compile(numAlphaRegex)
    
    # find digit-alphabet
    patterns.extend(numAlphaPattern.findall(word))
    
    # remove pattern in word
    word = numAlphaPattern.sub("",word)
    ####################
    
    
    
    # get alphabet-digit
    ####################
    alphaNumRegex = r'\b[A-z]+-\d+\b'
    alphaNumPattern = re.compile(alphaNumRegex)
    
    # find digit-alphabet
    patterns.extend(alphaNumPattern.findall(word))
    
    # remove pattern in word
    word = alphaNumPattern.sub("",word)
    ####################

    
    
def formatDates(word):
    
    # define formatserlrekg
    dateRegex = r"\b(?:0?[1-9]|1[012]|January|Jan|Feburary|Feb|March|Mar|April|Apr|May|June|Jun|July|Jul|August|Aug|September|Sept|October|Oct|November|Nov|December|Dec)[-/, ]\s*(?:0?[1-9]|[12][0-9]|3[01])[-/,]\s*\d{4}\b"
    datePattern = re.compile(dateRegex,re.IGNORECASE)
    
    # find dates
    patterns.extend(datePattern.findall(word))
    
    # remove dates in word
    word = datePattern.sub("",word)



testFile = open("test.tex")
lines = testFile.read().splitlines()
testFile.close()
lines = [i for i in lines if not isInvalidLine(i)] # comment line

print(lines)

# pattern detection1: date


# Date {January 4, 1994}{Jan. 4, 3000}{January 4 1994}{mm/dd/yyyy mm-dd-yyyy mm/dd/yyyy}  
# /\b(?:0?[1-9]|1[012]|(January|Jan|Feburary|Feb|March|Mar|April|Apr|May|June|Jun.|July|Jul|August|Aug|September|Sept|October|Oct|November|Nov|December|Dec))[-/, ](?:0?[1-9]|[12][0-9]|3[01])[-/, ]\s*\d{4}\b/

dateRegexWithBound = r"\b(?:0?[1-9]|1[012]|January|Jan|Feburary|Feb|March|Mar|April|Apr|May|June|Jun|July|Jul|August|Aug|September|Sept|October|Oct|November|Nov|December|Dec)[-/, ]\s*(?:0?[1-9]|[12][0-9]|3[01])[-/,]\s*\d{4}\b"
datePatternWithBound = re.compile(dateRegexWithBound)

dateRegex = r"(?:0?[1-9]|1[012]|January|Jan|Feburary|Feb|March|Mar|April|Apr|May|June|Jun|July|Jul|August|Aug|September|Sept|October|Oct|November|Nov|December|Dec)[-/, ]\s*(?:0?[1-9]|[12][0-9]|3[01])[-/,]\s*\d{4}"
datePattern = re.compile(dateRegex)


testString ='''

2005;  Oct 10, 2005; 10/10/2005; 10/10/05 5/4

Sept. 12, 2323
<DOCNO> FR940104-0-00001 </DOCNO>', 'Federal Register', '&blank;/&blank;Vol. 59, No. 2&blank;/&blank;Tuesday, January 4, 1994&blank;/&blank;Rules and Regulations', 'Vol. 59, No. 2', 'Tuesday, January 4, 1994
0-9999
06 13 3055 04 11 7356
04 22 6373
12 5 5719
01 9 8918
07 3 3484
12 30 4944
09 23 3746
12 24 9918
36/7/8567
4/29/2591
33/16/2090
12/17/6423
59/24/4066
48/4/2704
36/9/4232
49/20/6613
49/23/5671
54/23/5989
08/5/7580
05/28/8850
08/21/8479
11/28/9884
05/23/5891
08/23/3149
05/26/5492
08/14/8789
02/28/7682
07/20/5858
03-2-6161
12-21-3883
10-18-5597
12-28-5970
10-23-5237
12-29-6864
04-24-2177
08-22-8392
02-13-8783
11-24-9556

'''

##### pattern detection result1  -- print findAll
'''
resultWithBound  = re.findall(datePatternWithBound,testString)
result  = re.findall(datePattern,testString)


print(result,'\n\n')
print(resultWithBound,'\n\n')
print(set(result)-set(resultWithBound))
'''


##### pattern detection result2  -- try sub

resultWithBound  = re.sub(datePatternWithBound,'PATTERN',testString)
result  = re.sub(datePattern,'PATTERN',testString)


print(result,'\n\n')
print(resultWithBound,'\n\n')
print(set(result)-set(resultWithBound))





##### try apply to stirngList
'''
print(result)

def findDates(strList):
    datePattern = re.compile(dateRegex)
    result = []
    
    for i in range(0,len(strList)):
        result.append(re.findall(datePattern,strList[i]))
        strList[i] = datePattern.sub('',strList[i])
        
    return strList, result
'''

    
# pattern detection2: Digit-alphabet 1-hour
'''
numAlphaRegex = r'\b\d+-[A-z]+\b'
numAlphaPattern = re.compile(numAlphaRegex)

testString1= 
'''''''
   1-hour   
 820-TElQHZWzEM 
53233624-QUf`JbnzzP
67254-paP
608841635-IGZoYZLqyM
4857-
-X]REfFeXoB
3-Rz
4470689-WQ^f
64057172-s
-TrNduu''''''

result = re.findall(numAlphaPattern,testString1)
print(result)
'''

# pattern detection3: Alphabet-digit F-16; I-20
'''
alphaNumRegex = r'\b[A-z]+-\d+\b'
alphaNumPattern = re.compile(alphaNumRegex)

testString2= ''''''
t[Lac[-64417971
shXcXNY-24106
\cMbUKA-37
L-4153540793
gbU]CWzJw-00506
idNSZLdzuw-485707096
qfaA-281666
-00672
G^ajsuuKd-9281103493
MBw[ndc-642241
S\-1656806527
sIVJWvhuTp-753707
bXlSBurimZ-34776
-0
TH-1901''''''

result = re.findall(alphaNumPattern,testString2)
print(result)
'''
wordHyphenWord = r'\b[A-z]+-[A-z]+\b'
numAlphaPattern = re.compile(numAlphaRegex)
# • Dates 2005;  Oct 10, 2005; 10/10/2005; 10/10/05
# • Digit-alphabet 1-hour
# • Alphabet-digit F-16; I-20
# • Hyphenation co-existence; black-tie party
# • All caps CNN, BBC
# • Cap period (initial) N.
# • Digit.digit 8.00
# • Digit,digit 8,000
# • Currency symbol $, ....
# • Cultural known names M*A*S*H
# • Email address mouse@hotmail.com
# • URLs http://www.cnn.com
# • IP address 123.67.65.870
# • Names New York;  Los Angles  (Los Angles-New  York flights  ????)
def formatDates(line):
    
    
    # get potential valid lines
    dateRegex = r"\b(?:0?[1-9]|1[012]|January|Jan|Feburary|Feb|March|Mar|April|Apr|May|June|Jun|July|Jul|August|Aug|September|Sept|October|Oct|November|Nov|December|Dec)[-/, ]\s*(?:0?[1-9]|[12][0-9]|3[01])[-/,]\s*[\d{2}|\d{4}\b"
    datePattern = re.compile(dateRegex)
    dates = datePattern.findall(line)
    
    for d in dates:
        
        # if find a valid date, format it
        if(getValidDate(d)[0]):
            line = line.replace(d,getValidDate(d)[1])
            
    return line
            
        
        
# check the validity of the date and format date
def getValidDate(word):
    
    invalidResult = word
    
    # format dates
    word = word.replace(',' , '/')
    word = word.replace('-' , '/')
    word = word.replace(' ' , '/')
    word = word.replace('//' , '/')
    
    
    splitDate = word.split("/")
    month = splitDate[0] 
    day   = splitDate[1]
    year  = splitDate[2]
    
    # not numeric months
    if(not month[1].isdigit()):
        
        newMonth = toDigitMonth(month)
        
        # get numerical month
        word = word.replace(month,newMonth)
        month = newMonth
        
        
        
        
    # change 2digit YY to YYYY
    if(len(year)==2):
        
        newY = "20" + year if int(year)<50 else "19"+year
        word = word.replace(year,newY)
        year = newY
        
        
        
        
    # check date validity
    
    # month with 30 days
    if(int(month) in [4,6,9,11] and int(day) <= 30): return True, word
    # month with 31 days
    elif(int(month) in [1,3,5,7,8,10,12] and int(day) <= 31): return True, word
    # check April
    elif(int(month) == 2):
        # normal year
        if(int(day) <= 28): return True, word
        # leap year
        elif(int(day) == 29 and ((year%4 == 0 and year%100 != 0) or (year%400 == 0))):
            return True, word
   
    return False, invalidResult
        
       
       
       
def toDigitMonth(month):
       
       if(  month in ["January","Jan" ,"january","jan","Jan.","jan." ]     ): return "01"
       elif(month in ["Feburary","Feb","feburary","feb","Feb.","feb."]     ): return "02"
       elif(month in ["March","Mar","Mar.","mar."                    ]     ): return "03"
       elif(month in ["April","Apr","april","apr","Apr.","apr."      ]     ): return "04"
       elif(month in ["May","may"                                    ]     ): return "05"
       elif(month in ["June","Jun","june","jun","Jun.","jun."]             ): return "06"
       elif(month in ["July","Jul","july","jul","Jul.","jul."]             ): return "07"
       elif(month in ["August","Aug","august","aug","Aug.","aug."]         ): return "08"
       elif(month in ["September","Sept","september","sept","Sept.","sept."] ): return "09"
       elif(month in ["October","Oct","october","oct","Oct.","oct."]       ): return "10"
       elif(month in ["November","Nov","november","nov","nov.","Nov."]     ): return "11"
       elif(month in ["December","Dec","december","dec","dec.","Dec."]     ): return "12"
       
       return word
       
    

test = '''Aug 15, 2182
Jul 14, 7939
Jun 02, 5548
Apr 29, 1139
Apr 30, 5957
Oct 20, 5355
Nov 12, 7895
Nov 17, 9637
Jan. 26, 2210
Apr. 12, 1799
November 26, 2210
December 12, 1799
52-88-56
59-1212-76
51-55-38
27-33-53
19-77-51
31-07-2035
28-15-1949
30-25-1931
36-21-1943
52-23-2021
07-03-1976
05-26-2073
03-03-2015
05-19-2064
09-19-2013
02-22-77
10-16-79
09-20-78
09-29-50
12-10-52
02-22-17
10-16-19
09-20-18
09-29-15'''

test = test.split('\n')
print(test)
for i,s in enumerate(test):
    
    print(getValidDate(s))

#     print(getValidDate(s))
#     print(s)
    

def formatCapDot(line):
    
    # e.g: Ph.  Ph.d  Ph.dhh
    capDotRegex = r'[A-Z]+h?\.(?:[A-Za-z]+\.?)*'
    capDotPattern = re.compile(capDotRegex)
    
    # find Cap.Cap
    matches = capDotPattern.findall(line)
    
    print(matches)
    # change pattern in line
    for word in matches:
        line = line.replace(word,rmDotNConcat(word)) 
       
    
    return line


def rmDotNConcat(word):
    
    # get spilited words by dot
    split = word.split('.') 
    
    concat = ""
    
    # get concatednate words
    concat = ""
    for w in split:
        concat += w
        
    return concat


line = "Ds.pdf Ph.D U.S.A. Mr. Ph.d. U.S.A B.S. M.S"
line = "Ds.pdf Ph.D U.S.A U.S.A. B.S. Ph.D."
# line = formatExtensions(line)
print(line)
line = formatCapDot(line)
print(line)

#[a-z]{0,1}
# formatCapDot("Ph.D")
def formatDigits(line):
    
    digitRegex = r'\b[0-9]+(?:(?:[,][0-9]{3})|(?:[.][0-9]+))+\b'
    digitPattern = re.compile(digitRegex)
    
    # find digit formats
    matches = digitPattern.findall(line)


    # change pattern in line
    for word in matches:
        
        # format integer part
        sep = word.partition('.')
        nWord = sep[0].replace(',','')

        
        # format decimal part
        if(sep[2]!=''):
            if (int(sep[2]) != 0):
                nWord = nWord+'.'+sep[2] 
        print(word+"==>"+nWord)
        line = line.replace(word,nWord) 
        

       
    
    return line

testL = '''7.54
123,000,432.2
8.0004
8,000,123.12
1,000,001.121232132131
1,212
21,123
12,12
123.00
456,543,343,456,543,343.234432432
123,123,123,321.423432
'''
print(formatDigits(testL))
formatDigits(testL)    

def getEmailAddress(line):
    emailRegex = r"(?:[a-zA-Z0-9_\-\.]+)@(?:[a-zA-Z0-9_\-\.]+)\.(?:[a-zA-Z]{2,5})"
    emailPattern = re.compile(emailRegex)
    
    # find emails 
    matches = emailPattern.findall(line)
    
    return matches

testLine='''
abc@a.com
123@21.io
ads@hjotamil.com
1@w.us'''

print(getEmailAddress(testLine))
def getUrls(line):
    
    urlRegex = r'''((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\((?:[^\s()<>]+|(?:\([^\s()<>]+\)))*\))+(?:\((?:[^\s()<>]+|(?:\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))'''
    urlPattern = re.compile(urlRegex)
    
    # find urls 
    matches = urlPattern.findall(line)
    
    return matches


line = '''
http://localhost:8888/notebooks/Desktop/IR_p1/skeleton.ipynb
https://georgetown.instructure.com/courses/152635/files/folder/Lectures?preview=9308089
http://localhost:8888/notebooks/Desktop/IR_p1/testCode.ipynb
docs.python.org/3/library/re.html#writing-a-tokenizer
'''
print(getUrls(line))
def getIPs(line):
    
    # regEx referred from https://www.geeksforgeeks.org/how-to-validate-an-ip-address-using-regex/
    ipRegex = r"^(?:(?:25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(?:25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])$"
    ipPattern = re.compile(ipRegex,re.MULTILINE)
    
    # find IPs 
    matches = ipPattern.findall(line)
    
    
    return matches
    
line = '''
213.243.130.84
52.215.53.244
138.77.176.214
169.189.194.46
9.43.126.85
138.9.202.85
29.149.155.61
39.48.9.97
111.190.178.170
102.184.66.92
184.47.71.98
151.201.250.146
191.60.127.33
15.101.98.79
94.195.31.221
192.168.0.1
110.234.52.124'''

print(getIPs(line))
