def TrungHang(matrix):
    if len(matrix) != len(matrix[0]):
        return False
    rows_dict = {}
    for row in matrix:
        row_string = ''.join(map(str, row))
        if row_string in rows_dict:
            return True 
        else:
            rows_dict[row_string] = True
    return False

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [1, 2, 3]
]

if TrungHang(matrix):
    print("Ma trận có ít nhất hai hàng giống nhau")
else:
    print("Ma trận không có ít nhất hai hàng giống nhau")
