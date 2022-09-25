
import re
def readFiles():
    
    documents = readFilesHelper()
    
    for doc in readFilesHelper:
        
        
        wordList = readDocuments(doc)
        lexicon.add(wordList)


# split the file by documents
def readFilesHelper(file):
    
    abc =2
    
    
def readDocuments():
    
    index = 0
    
    docID = getDocumentID()
    lines = getLines()
    
    wordList = []
    
    for line in lines:
        
        parseLine = readLines(line, docID, index)
        wordList.extend(parseLine)
        
    return wordList


def readLines(line):
    
    wordList = []
    
    # e.g: Jan 3, 2002   02/03/19
    line = formatDates(line)
    
    # e.g: files.txt
    line = formatExtensions(line)
    
    # e.g: part-of-speech
    line = formatHyphens(line)
    
    # e.g: Ph.D
    line = formatCapDot(line)
    
    # e.g: 1,234,432.123 ==> 1234432.123 
    line = formatDigits(line)
    
    


# In[465]:


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
       
    


# In[466]:


def formatHyphens(line):
    
    # format number-letter
    line = digitAlpha(line)
    
    # format letter-number
    line = alphaDigit(line)
    
    # format words with prefixes
    line = alphaAlpha(line)
    
    return line
        

    
    
def digitAlpha(line):
    
    numAlphaRegex = r'\b\d+-[a-zA-Z]+\b'
    numAlphaPattern = re.compile(numAlphaRegex)
    
    # find digit-alphabet
    matches = numAlphaPattern.findall(line)
    
    # change pattern in line
    for word in matches:
        line = line.replace(word,splitNConcatHypen(word))
    
    return line
    
    
    
    
def alphaDigit(line):
    
    alphaDigitRegex = r'\b\[a-zA-Z]+-d+\b'
    alphaDigitPattern = re.compile(alphaDigitRegex)
    
    # find alphabet-digit
    matches = alphaDigitPattern.findall(line)
    
    # change pattern in line
    for word in matches:
        line = line.replace(word,splitNConcatHypen(word))
    
    return line    




def alphaAlpha(line):
    
    # alphaAlpha example: pre-processing, part-of-speech
    alphaAlphaRegex = r'\b[a-zA-Z]+(?:-[a-zA-Z]+)+\b'
    alphaAlphaPattern = re.compile(alphaAlphaRegex)
    
    # find alphabet-alphabet
    matches = alphaAlphaPattern.findall(line)
    
    # change pattern in line
    for word in matches:
        line = line.replace(word,splitNConcatHypen(word))
    
    return line




def splitNConcatHypen(word):
    
    commonPrefix = ['pre', 'post', 're', 'sub','non']
    
    # get spilited words
    split = word.split('-')

    
    # get concatednate words
    concat = ""
    for w in split:
        concat += w

    # "A-B" after function will be "AB A B"
    result = concat
     
    for w in split:
        if(w.isalpha() and len(w)>2 and w not in commonPrefix):  # w contains only letters and len >= 3
            result += " " + w 
            
    return result


# In[469]:


def formatCapDot(line):
    
    # e.g: Ph.  Ph.d  Ph.d B.S.
    capDotRegex = r'[A-Z]+h?\.(?:[A-Za-z]*\.?)*'
    capDotRegex = r'(?:[a-zA-Z]+\.)+[a-zA-Z\.]+'
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
    


# In[470]:


def formatExtensions(line):
    
    
    extensionRegex = r'\b\w+.(?:txt|html|pptx?|docx?|zip|mp3|mp4|csv|dat|pdf|jpe?g|xls[xm])\b'
    extensionPattern = re.compile(extensionRegex, re.IGNORECASE)
    
    # find digit-alphabet
    matches = extensionPattern.findall(line)


    # change pattern in line
    for word in matches:
        nWord = word + " " + word.partition('.')[2]
        line = line.replace(word,nWord) 
       
    
    return line
     
# formatExtensions("asdf.txt a.pdf fds.jpegfds a.docx k.jpg r.pptx")


# In[471]:


# • Digit.digit 8.00
# • Digit,digit 8,000

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
        line = line.replace(word,nWord) 
        

       
    
    return line
    


# In[522]:


def getEmailAddress(line):
    
    emailRegex = r"(?:[a-zA-Z0-9_\-\.]+)@(?:[a-zA-Z0-9_\-\.]+)\.(?:[a-zA-Z]{2,5})"
    emailPattern = re.compile(emailRegex)
    
    # find emails 
    matches = emailPattern.findall(line)
    
    return matches




def getUrls(line):
    
    urlRegex = r'''((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\((?:[^\s()<>]+|(?:\([^\s()<>]+\)))*\))+(?:\((?:[^\s()<>]+|(?:\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))'''
    urlPattern = re.compile(urlRegex)
    
    # find urls 
    matches = urlPattern.findall(line)
    
    return matches




def getIPs(line):
    
    # regEx referred from https://www.geeksforgeeks.org/how-to-validate-an-ip-address-using-regex/
    ipRegex = r"^(?:(?:25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(?:25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])$"
    ipPattern = re.compile(ipRegex,re.MULTILINE)
    
    # find IPs 
    matches = ipPattern.findall(line)
    
    
    return matches
    
    
    
    

def getCurrency(line):
    
    currencyRegex = r'[$€¢£¥]\s*[0-9]+.?[0-9]*'
    currencyPattern = re.compile(currencyRegex)
    
    # find currencies 
    matches = currencyPattern.findall(line)
    
    return matches



