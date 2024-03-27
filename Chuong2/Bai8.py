def TamGiacDuoi(matrix):
    if len(matrix) != len(matrix[0]):
        return False
    n = len(matrix)
    for i in range(n):
        for j in range(i):  
            if matrix[i][j] != 0:
                return False
    return True

matrix = [
    [1, 0, 0],
    [2, 3, 0],
    [4, 5, 6]
]

if TamGiacDuoi(matrix):
    print("Ma trận là ma trận tam giác dưới")
else:
    print("Ma trận không phải là ma trận tam giác dưới")
