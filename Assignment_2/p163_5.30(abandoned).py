import math

def firstDay():
    firstDayStr = str("")
    if firstDay == 0:
        firstDayStr = "Sunday"
    elif firstDay == 1:
        firstDayStr = "Monday"
    elif firstDay == 2:
        firstDayStr = "Tuesday"
    elif firstDay == 3:
        firstDayStr = "Wednesday"
    elif firstDay == 4:
        firstDayStr = "Thursday"
    elif firstDay == 5:
        firstDayStr = "Friday"
    elif firstDay == 6:
        firstDayStr = "Saturday"
    return firstDayStr


def main():
    year = int(input("Please enter a year: "))
    firstDay = int(input("Please enter the first day of the year: "))
    numberOfDaysPerMonth = int(0)
    firstDayStr = str("")

    for month in range(1, 13, 1):
        if month == 1:
            print("January 1, ", year, " is ")
            numberOfDaysPerMonth = 31
            firstDayStr = firstDay(firstDay)
            print(firstDayStr)
        elif month == 2:
            print("February 1, ", year, " is ")
            if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
                numberOfDaysPerMonth = 29
            else:
                numberOfDaysPerMonth = 28
            firstDayStr = firstDay(firstDay)
            print(firstDayStr)
        elif month == 3:
            print("March 1, ", year, " is ")
            numberOfDaysPerMonth = 31
            firstDayStr = firstDay(firstDay)
            print(firstDayStr)
        elif month == 4:
            print("April 1, ", year, " is ")
            numberOfDaysPerMonth = 30
            firstDayStr = firstDay(firstDay)
            print(firstDayStr)
        elif month == 5:
            print("May 1, ", year, " is ")
            numberOfDaysPerMonth = 31
            firstDayStr = firstDay(firstDay)
            print(firstDayStr)
        elif month == 6:
            print("June 1, ", year, " is ")
            numberOfDaysPerMonth = 30
            firstDayStr = firstDay(firstDay)
            print(firstDayStr)
        elif month == 7:
            print("July 1, ", year, " is ")
            numberOfDaysPerMonth = 31
            firstDayStr = firstDay(firstDay)
            print(firstDayStr)
        elif month == 8:
            print("August 1, ", year, " is ")
            numberOfDaysPerMonth = 31
            firstDayStr = firstDay(firstDay)
            print(firstDayStr)
        elif month == 9:
            print("September 1, ", year, " is ")
            numberOfDaysPerMonth = 30
            firstDayStr = firstDay(firstDay)
            print(firstDayStr)
        elif month == 10:
            print("October 1, ", year, " is ")
            numberOfDaysPerMonth = 31
            firstDayStr = firstDay(firstDay)
            print(firstDayStr)
        elif month == 11:
            print("November 1, ", year, " is ")
            numberOfDaysPerMonth = 30
            firstDayStr = firstDay(firstDay)
            print(firstDayStr)
        elif month == 12:
            print("December 1, ", year, " is ")
            numberOfDaysPerMonth = 31
            firstDayStr = firstDay(firstDay)
            print(firstDayStr)
        firstDay = (firstDay + numberOfDaysPerMonth) % 7
main()
