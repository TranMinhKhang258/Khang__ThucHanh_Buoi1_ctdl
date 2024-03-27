def DoiXung(matrix):
    if len(matrix) != len(matrix[0]):
        return False
    n = len(matrix)
    for i in range(n):
        for j in range(i+1, n):  # Chỉ kiểm tra nửa phía trên đường chéo chính
            if matrix[i][j] != matrix[j][i]:
                return False
    return True

matrix = [
    [1, 2, 3],
    [2, 4, 5],
    [3, 5, 6]
]

if DoiXung(matrix):
    print("Ma trận là ma trận đối xứng")
else:
    print("Ma trận không phải là ma trận đối xứng")
