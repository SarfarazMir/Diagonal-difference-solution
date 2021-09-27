def diagonalDifference(arr):
    diagonal1, diagonal2 = 0, 0

    for i in range(len(arr)):
            diagonal1 += arr[i][i]
            diagonal2 += arr[i][len(arr)-i-1]
    return abs(diagonal1-diagonal2)

#test case 1
print(diagonalDifference([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
#test case 2
print(diagonalDifference([[7, 3, 2], [8, 9, 3], [6, 3, 9]]))
