import math
def main():
    year = int(input("Please enter a year: "))
    day = int(input("Please enter the first day of the year: "))
    output = str
    for month in range(1, 13, 1):
        output = ""
        if month == 1:
            output += "January"
        elif month == 2:
            output += "February"
        elif month == 3:
            output += "March"
        elif month == 4:
            output += "April"
        elif month == 5:
            output += "May"
        elif month == 6:
            output += "June"
        elif month == 7:
            output += "July"
        elif month == 8:
            output += "August"
        elif month == 9:
            output += "September"
        elif month == 10:
            output += "October"
        elif month == 11:
            output += "November"
        elif month == 12:
            output += "December"
        output += " 1," + str(year) + " is"
        day %= 7
        if day == 0:
            print(output, "Sunday")
        elif day == 1:
            print(output, "Monday")
        elif day == 2:
            print(output, "Tuesday")
        elif day == 3:
            print(output, "Wednesday")
        elif day == 4:
            print(output, "Thursday")
        elif day == 5:
            print(output, "Friday")
        elif day == 6:
            print(output, "Saturday")

        if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
            day += 31
        elif month == 4 or month == 6 or month == 9 or month == 11:
            day += 30
        else:
            if ((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0):
                day += 29
            else:
                day += 28

main()
