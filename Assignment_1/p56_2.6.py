import math
integer = int(input("Enter a number between 0 and 1000: "))
if integer // 10 < 1:
    print("The sum of the digits is ", integer)
elif integer // 10 < 10:
    print("The sum of the digits is ", (integer // 10) + (integer % 10))
elif integer // 10 < 100:
    print("The sum of the digits is ", (integer // 100) + ((integer // 10) % 10) + (integer % 10))(integer // 100)
else:
    print("The sum of the digits is ", integer // 1000)
