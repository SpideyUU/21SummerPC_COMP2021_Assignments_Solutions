import math
import random
def main():
    n = int(input("Enter n: "))
    printMatrix(n)


def printMatrix(n):
    for row in range(n):
        for column in range(n):
            print("%3d" % (int(random.random() * 2)), end="")
        print("")

main()
