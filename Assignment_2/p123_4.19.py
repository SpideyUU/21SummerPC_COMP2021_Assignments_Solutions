import math
edge_1, edge_2, edge_3 = map(int, input("Enter three edges: ").split(","))
valid = bool(((edge_1 + edge_2) > edge_3) and ((edge_1 + edge_3) > edge_2) and ((edge_2 + edge_3) > edge_1))
if valid is False:
    print("The input is invalid!")
elif valid is True:
    print("The perimeter is", edge_1 + edge_2 + edge_3)
