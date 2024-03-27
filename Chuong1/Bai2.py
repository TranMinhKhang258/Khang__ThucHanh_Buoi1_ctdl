def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def neper(n):
    e = 0
    for k in range(0, n + 1):
        e += 1 / factorial(k)
    return e

n = int(input("Nhập số nguyên n (n ≥ 0): "))
print("Số e được tính là:", neper(n))
