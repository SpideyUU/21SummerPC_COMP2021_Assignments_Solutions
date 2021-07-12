def printMatrix(m):
    for row in range(len(m)):
        for column in range(len(m[row])):
            print(m[row][column], end=" ")
        print()


def MultiplyMatrices(m1, m2):
    lst = len(m2[0]) * [0]
    result = []
    for i in range(len(m1)):
        result.append([x for x in lst])

    for i in range(len(result)):
        for j in range(len(result[0])):
            for k in range(len(m2)):
                result[i][j] += m1[i][k] * m2[k][j]

    printMatrix(result)


def main():
    matrix1 = []
    matrix2 = []
    number_of_rows = eval(input("Enter the number of rows: "))
    number_of_columns = eval(input("Enter the number of columns: "))
    numbers = input("Enter the matrix1: ")
    value = numbers.split(" ")

    count = 0
    for row in range(number_of_rows):
        matrix1.append([])
        for column in range(number_of_columns):
            matrix1[row].append(int(value[count]))
            count += 1

    numbers2 = input("Enter the matrix2: ")
    value2 = numbers2.split(" ")

    count = 0
    for row in range(number_of_rows):
        matrix2.append([])
        for column in range(number_of_columns):
            matrix2[row].append(int(value2[count]))
            count += 1

    print("The multiplication of matrix 1 and 2 is:")
    MultiplyMatrices(matrix1, matrix2)


main()
