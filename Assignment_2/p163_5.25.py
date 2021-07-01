import math
n = 50000
resultFromLeftToRight = 0
resultFromRightToLeft = 0

for i in range(1, n+1, 1):
    resultFromLeftToRight += 1.0 / i
for i in range(n, 0, -1):
    resultFromRightToLeft += 1.0 / i
print("The result of computing from left to right is", resultFromLeftToRight)
print("The result of computing from right to left is", resultFromRightToLeft)
