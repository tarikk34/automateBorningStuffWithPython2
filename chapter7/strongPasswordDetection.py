# detect if password is strong or not
import re

def passwordDetection(password):
    if len(password) < 8:
        print("This is a weak password")
    else:
        lowerCase = re.compile(r'[a-z]')
        upperCase = re.compile(r'[A-Z]')
        digit = re.compile(r'\d')
        lower = lowerCase.search(password)
        upper = upperCase.search(password)
        num = digit.search(password)
        if lower and upper and num:
            print("This is a strong password")
        else:
            print("This is a weak password")

password = input("Type your password: ")
passwordDetection(password)