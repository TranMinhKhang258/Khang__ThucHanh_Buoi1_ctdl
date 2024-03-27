def define_number(n):
    Sum = sum([i for i in range(1, n) if n % i == 0])
    if Sum < n:
        return "deficient"
    elif Sum == n:
        return "perfect"
    else:
        return "abundant"
    
def numbers(x, y):
    for k in range(x, y + 1):
        print(f"Số {k} là {define_number(k)}.")

x = int(input("Nhap x = "))
y = int(input("Nhap y = "))

numbers(x, y)