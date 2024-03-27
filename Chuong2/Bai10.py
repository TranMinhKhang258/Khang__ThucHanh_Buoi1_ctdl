def NhomCot(matrix):
    if len(matrix) != len(matrix[0]):
        print("Ma trận không phải là ma trận vuông")
        return
    cols_dict = {}
    n = len(matrix)
    for j in range(n): 
        col_string = ''.join(str(matrix[i][j]) for i in range(n))
        if col_string in cols_dict:
            cols_dict[col_string].append(j) 
        else:
            cols_dict[col_string] = [j] 
    for col_indices in cols_dict.values():
        if len(col_indices) > 1:  
            print("Nhóm chỉ mục cột:", col_indices)

matrix = [
    [1, 2, 1],
    [4, 5, 4],
    [1, 2, 1]
]

print("Các nhóm chỉ mục cột của các cột giống nhau:")
NhomCot(matrix)
