def gcd_recursive(m, n):
    if n == 0:
        return m
    else:
        return gcd_recursive(n, m % n)
    
def gcd(m, n):
    while n != 0:
        m, n = n, m % n
    return m

m = int(input("Nhap m = "))
n = int(input("Nhap n = "))

k1 = gcd_recursive(m, n)
k2 = gcd(m, n)
print(f"GCD của {m} và {n} bang de quy là: ", k1)
print(f"GCD của {m} và {n} là: ", k2)