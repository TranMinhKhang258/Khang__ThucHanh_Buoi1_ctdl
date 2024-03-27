def Fibonacci_recursive(n):
    if n == 1:
        return 0
    if n == 2 or n == 3:
        return 1
    else:
        return Fibonacci_recursive(n-1) + Fibonacci_recursive(n-2)
    
def Fibonacci(n):
    a = 0
    b = c = 1
    if n == 1:
        return 0
    if n == 2 or n == 3:
        return 1
    for _ in range(3, n+1):
        c = a + b
        a = b
        b = c
    return c

n = int(input("Nhap n = "))

print(f"So Fibonacci thu {n} bang de quy la ", Fibonacci_recursive(n))
print(f"So Fibonacci thu {n} la ", Fibonacci(n))