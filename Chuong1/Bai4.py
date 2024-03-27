class Pascal:
    def calculate_factorial(num):
        if num == 0:
            return 1
        factorial = 1
        for i in range(1, num + 1):
            factorial *= i
        return factorial
    def pascal(n):
        for line in range(1, n + 2):
            C = 1
            for i in range(1, line + 1):
                print(C, end=" ")
                C = C * (line - i) // i
            print()
n = int(input("Nhập n: "))
print("tam giác Pascal ứng với bậc", n, "là:")
Pascal.pascal(n)