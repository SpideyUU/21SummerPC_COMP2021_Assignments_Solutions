import os
import random
import sys

filename = input("Enter a filename: ").strip()

if os.path.isfile(filename):
    print("The file already exists")
    sys.exit()

file = open(filename, 'w')

for i in range(100):
    file.write(str(random.randint(0, 100)) + " ")

file.close()

file1 = open(filename, 'r')
nums = []
for line in file1:
    nums = line.split()

nums = [eval(x) for x in nums]
nums.sort()
for n in nums:
    print(n, end=' ')
