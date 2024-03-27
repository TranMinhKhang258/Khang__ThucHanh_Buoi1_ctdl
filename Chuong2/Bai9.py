def TrungCot(matrix):
    if len(matrix) != len(matrix[0]):
        return False
    cols_dict = {}
    n = len(matrix)
    for j in range(n): 
        col_string = ''.join(str(matrix[i][j]) for i in range(n))
        if col_string in cols_dict:
            return True 
        else:
            cols_dict[col_string] = True
    return False

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [1, 2, 3]
]

if TrungCot(matrix):
    print("Ma trận có ít nhất hai cột giống nhau")
else:
    print("Ma trận không có ít nhất hai cột giống nhau")
