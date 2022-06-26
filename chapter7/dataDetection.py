import re, sys

def dataDetection(inputDate):
    print("Inputted Data: " + inputDate)
    date = re.compile(r'(\d{2})/(\d{2})/(\d{4})')
    datesFound = date.findall(inputDate)
    day = int(datesFound[0][0])
    month = datesFound[0][1]
    year = int(datesFound[0][2])
    if int(month) > 12:
        print("Month cannot be greater then 12")
    elif day > 32:
        print("Not a valid date day is above 31")
    elif day == 31:
        if (month == '04' or month == '06' or month == '09' or month == '11' or month == '02'):
            print("The date " + inputDate + " is not valid date as the month does not have 31 days")
        else:
            print("The date "+ inputDate + " is a valid date!")
    elif month == '02':
        if day > 29:
            print("February does not have more then 29 days")
        elif day == 29:
            if year % 400 == 0:
                print("The date "+ inputDate + " is a valid date!")
            elif year % 100 == 0:
                print("The date "+ inputDate + " is a not valid date!")
            elif year % 4 == 0:
                print("The date "+ inputDate + " is a valid date!")
            else:
                print("The date "+ inputDate + " is a not valid date!")
    else:
        print("The date "+ inputDate + " is a valid date!")


print("Give a date in the format DD/MM/YYYY (including slashes /) to see if it is a real date")
inputDate = input("Date: ")
dataDetection(inputDate)