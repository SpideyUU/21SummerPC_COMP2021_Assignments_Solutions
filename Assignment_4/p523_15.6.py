def sumSeries(i):
    if i == 1:
        return 1 / 2
    return i / (i + 1) + sumSeries(i - 1)


for i in range(1, 11):
    print("The sum series for i=", i, "is", sumSeries(i))
