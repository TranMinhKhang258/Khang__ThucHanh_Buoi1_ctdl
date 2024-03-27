def NhomHang(matrix):
    if len(matrix) != len(matrix[0]):
        print("Ma trận không phải là ma trận vuông")
        return
    rows_dict = {}
    for i, row in enumerate(matrix):
        row_string = ''.join(map(str, row))
        if row_string in rows_dict:
            rows_dict[row_string].append(i)  
        else:
            rows_dict[row_string] = [i] 
    for row_indices in rows_dict.values():
        if len(row_indices) > 1:
            print("Nhóm chỉ mục hàng:", row_indices)

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [1, 2, 3]
]

print("Các nhóm chỉ mục hàng của các hàng giống nhau:")
NhomHang(matrix)
