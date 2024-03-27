def Tru(a, b):
    sign_a = a // 10**10
    sign_b = b // 10**10
    num_a = a % 10**10
    num_b = b % 10**10
    
    result_num = num_a - num_b
    
    if result_num < 0:  
        if sign_a == sign_b:  
            return [-1]  
        else:
            return sign_a * 10**10  
    else:
        return sign_a * 10**10 + result_num

a = 1000000002  
b = 1000000001  

print("Kết quả của a - b:", Tru(a, b))
