import math
name = input("Enter employee's name: ")
numberOfHoursPerWeek = float(input("Enter number of hours worked in a week: "))
hourlyPayRate = float(input("Enter hourly pay rate:  "))
federalTAxWithholdingRate = float(input("Enter federal tax withholding rate: "))
stateTaxWithholdingRate = float(input("Enter state tax withholding rate: "))
grossPay = numberOfHoursPerWeek * hourlyPayRate

print("Employee Name:", name)
print("Hours Worked:", '%.1f' % numberOfHoursPerWeek)
print("Pay Rate:", "$" '%.2f' % hourlyPayRate)
print("Gross Pay:", "$" '%.1f' % grossPay)
print("Deductions: ")
print("  Federal Withholding (", '%.1f%%' % (federalTAxWithholdingRate * 100), "):", "$" '%.1f' % (grossPay * federalTAxWithholdingRate))
print("  State Withholding (", '%.1f%%' % (stateTaxWithholdingRate * 100), "):", "$" '%.2f' % (grossPay * stateTaxWithholdingRate))
print("  Total Deduction:", "$" '%.2f' % ((federalTAxWithholdingRate + stateTaxWithholdingRate) * grossPay))
print("Net Pay:", "$" '%.2f' % (grossPay - ((federalTAxWithholdingRate + stateTaxWithholdingRate) * grossPay)))
