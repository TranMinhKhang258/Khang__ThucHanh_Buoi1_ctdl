def Nhan(a, b):
    str_a = ''.join(map(str, a))
    str_b = ''.join(map(str, b))
    result = int(str_a) * int(str_b)

    if result > 10**10 - 1:  
        return [-1]  
    else:
        return list(map(int, str(result))) 

a = [1, 2, 3]
b = [4, 5, 6]

print("Kết quả của a * b:", Nhan(a, b))
