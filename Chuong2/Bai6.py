def Tru(a, b):
    str_a = ''.join(map(str, a))
    str_b = ''.join(map(str, b))
    result = int(str_a) - int(str_b)
    return result

a = [3, 2, 1]
b = [1, 1, 1]

print("Kết quả của a - b:", Tru(a, b))
