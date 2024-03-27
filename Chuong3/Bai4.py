class Node:
    def __init__(self, heso, somu):
        self.HeSo = heso
        self.SoMu = somu
        self.KeTiep = None

class DaThuc:
    def __init__(self):
        self.Head = None
    
    def Them(self, heso, somu):
        new_node = Node(heso, somu)
        if self.Head is None:
            self.Head = new_node
        else:
            current = self.Head
            previous = None
            while current is not None and current.SoMu > somu:
                previous = current
                current = current.KeTiep
            
            if current is not None and current.SoMu == somu:
                current.HeSo += heso
            else:
                # Thêm node vào danh sách
                if previous is None:
                    new_node.KeTiep = self.Head
                    self.Head = new_node
                else:
                    new_node.KeTiep = current
                    previous.KeTiep = new_node

    def DoiDau(self):
        current = self.Head
        while current is not None:
            current.HeSo = -current.HeSo  
            current = current.KeTiep

    def InDaThuc(self):
        current = self.Head
        while current is not None:
            print(f"{current.HeSo}x^{current.SoMu}", end=" ")
            if current.KeTiep is not None:
                print("+", end=" ")
            current = current.KeTiep
        print()

dathuc = DaThuc()
dathuc.Them(3, 2)
dathuc.Them(-4, 3)
dathuc.Them(2, 1)

print("Da thuc truoc khi doi dau:")
dathuc.InDaThuc() 

dathuc.DoiDau()

print("Da thuc sau khi doi dau:")
dathuc.InDaThuc() 
