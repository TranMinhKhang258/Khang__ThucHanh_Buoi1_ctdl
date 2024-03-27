def DayConDaiNhat(a, b):
    dp = [[0] * (len(b) + 1) for _ in range(len(a) + 1)]
    max_length = 0
    end_index = 0
    
    for i in range(1, len(a) + 1):
        for j in range(1, len(b) + 1):
            if a[i - 1] == b[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
                if dp[i][j] > max_length:
                    max_length = dp[i][j]
                    end_index = i - 1  
                
    c = a[end_index - max_length + 1: end_index + 1]
    return c

a = [1, 6, 2, 5, 3, 7, 9, 4, 2, 8, 1, 5]
b = [6, 2, 5, 3, 7, 9, 8, 1, 5]

print("Dãy con chung có chiều dài lớn nhất của a và b:", DayConDaiNhat(a, b))
