class BieuThuc:
    def __init__(self, bieu_thuc):
        self.bieu_thuc = bieu_thuc

    def GiaTri(self):
        def thuc_hien_phep_toan(operand_stack, operator_stack):
            operand2 = operand_stack.pop()
            operand1 = operand_stack.pop()
            operator = operator_stack.pop()
            if operator == '+':
                operand_stack.append(operand1 + operand2)
            elif operator == '-':
                operand_stack.append(operand1 - operand2)
            elif operator == '*':
                operand_stack.append(operand1 * operand2)
            elif operator == '/':
                operand_stack.append(operand1 / operand2)

        def uu_tien(toan_tu):
            if toan_tu in ['+', '-']:
                return 1
            if toan_tu in ['*', '/']:
                return 2
            return 0

        toan_hang_stack = []
        toan_tu_stack = []

        i = 0
        while i < len(self.bieu_thuc):
            if self.bieu_thuc[i].isdigit():
                operand = 0
                while i < len(self.bieu_thuc) and self.bieu_thuc[i].isdigit():
                    operand = operand * 10 + int(self.bieu_thuc[i])
                    i += 1
                toan_hang_stack.append(operand)
                continue
            elif self.bieu_thuc[i] in ['+', '-', '*', '/']:
                while (toan_tu_stack and
                       uu_tien(self.bieu_thuc[i]) <= uu_tien(toan_tu_stack[-1])):
                    thuc_hien_phep_toan(toan_hang_stack, toan_tu_stack)
                toan_tu_stack.append(self.bieu_thuc[i])
            i += 1

        while toan_tu_stack:
            thuc_hien_phep_toan(toan_hang_stack, toan_tu_stack)

        return toan_hang_stack.pop()

bieu_thuc = "3 + 4 * 2 - 8 / 2"
bt = BieuThuc(bieu_thuc)
print("Giá trị của biểu thức '{}' là: {}".format(bieu_thuc, bt.GiaTri()))
