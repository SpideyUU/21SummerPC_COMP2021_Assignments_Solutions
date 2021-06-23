import math
finalAccountValue = float(input("Enter final account value: "))
annualInterestRate = float(input("Enter annual interest rate in percent: "))
numberOfYears = float(input("Enter number of years: "))

initialDepositAmount = finalAccountValue / pow((1 + (annualInterestRate / 12 / 100)), numberOfYears*12)

print("Initial deposit value is ", initialDepositAmount)
