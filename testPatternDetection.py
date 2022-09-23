import re

# Goal: detect all following patterns
########################################################################
'''
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
'''






# Pattern Detection1: date
########################################################################

# Date {January 4, 1994}{Jan. 4, 3000}{January 4 1994}{mm/dd/yyyy mm-dd-yyyy mm/dd/yyyy}  
# /\b(?:0?[1-9]|1[012]|(January|Jan|Feburary|Feb|March|Mar|April|Apr|May|June|Jun.|July|Jul|August|Aug|September|Sept|October|Oct|November|Nov|December|Dec))[-/, ](?:0?[1-9]|[12][0-9]|3[01])[-/, ]\s*\d{4}\b/

# dateRegex = "(?:0?[1-9]|1[012]|January|Jan|Feburary|Feb|March|Mar|April|Apr|May|June|Jun|July|Jul|August|Aug|September|Sept|October|Oct|November|Nov|December|Dec)[-/, ]\s*(?:0?[1-9]|[12][0-9]|3[01])[-/,]\s*\d{4}"
# datePattern = re.compile(dateRegex)
# testString = 
'''

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
result = re.findall(datePattern,testString)


# Output1
########################################################################
# after a doucment is read into a strList, parse the list to get dates
def findDates(strList):
    dateRegex = "(?:0?[1-9]|1[012]|January|Jan|Feburary|Feb|March|Mar|April|Apr|May|June|Jun|July|Jul|August|Aug|September|Sept|October|Oct|November|Nov|December|Dec)[-/, ]\s*(?:0?[1-9]|[12][0-9]|3[01])[-/,]\s*\d{4}"
    datePattern = re.compile(dateRegex,re.IGNORECASE)
    result = []
    
    # find dates 
    for i in range(0,len(strList)):
        result.extend(re.findall(datePattern,strList[i]))
        strList[i] = datePattern.sub('',strList[i])
    
    # remove empty list element
    strList =list(filter(None, strList))
    result =list(filter(None, result))
    
    return strList, result
