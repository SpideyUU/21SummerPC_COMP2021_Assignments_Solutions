import math
dividend = int(input("Enter an integer: "))
print("Is", dividend, "divisible by 5 and 6?", ((dividend % 5 == 0) & (dividend % 6 == 0)))
print("Is", dividend, "divisible by 5 or 6?", ((dividend % 5 == 0) | (dividend % 6 == 0)))
print("Is", dividend, "divisible by 5 or 6, but not both?", ((dividend % 5 == 0) ^ (dividend % 6 == 0)))
