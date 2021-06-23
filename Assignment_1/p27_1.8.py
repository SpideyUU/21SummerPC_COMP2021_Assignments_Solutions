import math
radius = 5.5
area = radius**2 * math.pi
perimeter = radius * 2 * math.pi
print("A circle has a radius of 5.5, \n"
      "it's area is " + str(area) + ", round up to 2 decimal places is " + str(round(area, 2)) +
      "\nand it's perimeter is " + str(perimeter) + ", round up to 2 decimal places is " + str(round(perimeter, 2)))
