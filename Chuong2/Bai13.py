def Nhan(a, b):
    sign_a = a // 10**10
    sign_b = b // 10**10
    num_a = a % 10**10
    num_b = b % 10**10
    
    result_num = num_a * num_b
    
    if result_num > 10**10 - 1: 
        return [-1]  
    else:
        result_sign = 0 if (sign_a + sign_b) % 2 == 0 else 1
        return result_sign * 10**10 + result_num

a = 1000000001 
b = 1000000002 

print("Kết quả của a * b:", Nhan(a, b))
