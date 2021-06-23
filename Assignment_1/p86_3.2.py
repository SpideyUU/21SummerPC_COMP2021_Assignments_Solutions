import math
pt1_x, pt1_y = map(float, input("Enter point 1 (latitude and longitude) in degrees: ").split(', '))
#coma1 = [int(1) for i in pt1.split(',')]
pt2_x, pt2_y = map(float, input("Enter point 2 (latitude and longitude) in degrees: ").split(', '))
#coma2 = [int(1) for i in pt2.split(',')]
radius = 6371.01

distance = float(radius) * math.acos((math.sin(math.radians(pt1_x)) * math.sin(math.radians(pt2_x))) + (math.cos(math.radians(pt1_x)) * math.cos(math.radians(pt2_x)) * math.cos((math.radians(pt1_y) - math.radians(pt2_y)))))
print("The distance between the two points is ", distance, " km")
