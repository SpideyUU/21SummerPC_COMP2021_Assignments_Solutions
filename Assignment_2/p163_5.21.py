for i in range(0, 9):
    for j in range(10 - i):
        print(" ", end=" ")
    for j in range(1, i):
        if j > 2:
            print(2**(j-1), end=" ")
        else:
            print(j, end=" ")
    for r in range(i, 0, -1):
        if r > 2:
            print(2**(r-1), end=" ")
        else:
            print(r, end=" ")
    print("\n")
