def diagonalDifference(arr):
    diagonal1, diagonal2, difference = 0, 0, 0

    for i in range(1):
        for j in range(len(arr[i])):
            diagonal1 += arr[j][j]

    for i in range(1):
        for j in range(len(arr)-1, (len(arr)-len(arr)-1), -1):
            diagonal2 += arr[i][j]
            i += 1
    return abs(diagonal1-diagonal2)
  
print(diagonalDifference([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
print(diagonalDifference([[7, 3, 2], [8, 9, 3], [6, 3, 9]]))
