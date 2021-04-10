def matrixElementsSum(matrix):
    result = 0

    for x in range(len(matrix[0])):
        for y in range(len(matrix)):

            if(matrix[y][x] == 0):
                break
            result += matrix[y][x]

    return result