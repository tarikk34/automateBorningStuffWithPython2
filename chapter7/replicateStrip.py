# Write a function that replicates pythons strip method
import re,sys

def stripString(userString, userDelimiter):
    whitespaceLeft = re.compile(r'(^\s*)')
    whitespaceRight = re.compile(r'(\s*$)')
    userString = whitespaceLeft.sub('',userString)
    userString = whitespaceRight.sub('',userString)
    if userDelimiter == '':
        print(userString)
    elif userDelimiter not in userString:
        print(userString)
    else:
        delim = re.compile('(.*)(%s)(.*)'%userDelimiter)
        delim1 = delim.search(userString).group(1)
        delim2 = delim.search(userString).group(3)
        print(delim1+delim2)

userString = input("Give a sentence:")
userDelimiter = input("Provide a delimter, if none then press enter: ")
stripString(userString,userDelimiter)
