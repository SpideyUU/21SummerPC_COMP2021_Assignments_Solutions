import math
e = 1.0
denominator = 1.0
for i in range(2, 100001, 1):
    denominator /= float(i)
    e += denominator
    if i % 10000 == 0:
        print("i is ", i, " and e is ", e)
