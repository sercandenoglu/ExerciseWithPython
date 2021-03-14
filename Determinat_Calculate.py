import copy

def GetMatrix():
    #get matrix from user
    print("If you want to exit, please write \"exit\"")
    print("You can split with ',' each value")
    print("Please enter each row")
    matrix = []
    counter = 1
    while True:
        row = input(f"Enter {counter}. row: ")

        if row == "exit":
            break
        else:
            matrix.append(row.split(","))
        counter += 1
    return matrix

def SquareMatrixCheck(matrix):
    #it is square matrix check
    for i in matrix:
        if len(i) != len(matrix):
            return False
    else:
        return True

def TwotoTwo(matrix):
    #If matrix is two to two
    x1 = int(matrix[0][0]) * int(matrix[1][1])
    x2 = int(matrix[0][1]) * int(matrix[1][0])
    return x1 - x2

def Sarrus(matrix):
    #If matrix is three to three
    temporaryMatrix = matrix.copy()
    temporaryMatrix.append(matrix[0])
    temporaryMatrix.append(matrix[1])
    temporarySumForPositive = []
    temproraySumForNegative = []

    #left to right sum
    for n in range(3):
        counter = 0
        product = 1
        #temporary values for result
        x = []
        for j in range(n, n + 3, 1):
            x.append(temporaryMatrix[j][counter])
            counter += 1
        for i in x:
            product *= int(i)
        temporarySumForPositive.append(product)

    #right to left sum
    for n in range(3):
        counter = 2
        product = 1
        #temporary values for result
        x = []
        for j in range(n, n + 3, 1):
            x.append(temporaryMatrix[j][counter])
            counter -= 1
        for i in x:
            product *= int(i)
        temproraySumForNegative.append(product)

    return sum(temporarySumForPositive) - sum(temproraySumForNegative)

def MultilineMatrix(matrix):
    determinant = 0
    for i in range(len(matrix)):
        if matrix[i][0] != 0:
            temporaryMatrix = copy.deepcopy(matrix)
            temporaryDeterminant = temporaryMatrix[i][0] * ((-1) ** ((i+1) + 1))
            #now we are erasing rows and columns
            del temporaryMatrix[i]
            for j in range(len(temporaryMatrix)):
                del temporaryMatrix[j][0]

            if len(temporaryMatrix) == 3:
                temporaryDeterminant *= Sarrus(temporaryMatrix)
            else:
                temporaryDeterminant *= MultilineMatrix(temporaryMatrix)
            determinant += temporaryDeterminant
    return determinant


matrix = GetMatrix()
if SquareMatrixCheck(matrix) is True and len(matrix) > 0:
    if len(matrix) == 1:
        print(f"Determinant is {matrix[0][0]}")
    elif len(matrix) == 2:
        print(f"Determinant is {TwotoTwo(matrix)}")
    elif len(matrix) == 3:
        print(f"Determinant is {Sarrus(matrix)}")
    else:
        print(f"Determinant is {MultilineMatrix(matrix)}")
else:
    print("Matrix is not square")

