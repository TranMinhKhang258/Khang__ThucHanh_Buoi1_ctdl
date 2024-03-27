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
            new_node.KeTiep = new_node  
        else:
            current = self.Head
            while current.KeTiep != self.Head:
                current = current.KeTiep
            current.KeTiep = new_node
            new_node.KeTiep = self.Head

    def InDaThuc(self):
        if self.Head is None:
            print("Da thuc rong")
            return
        current = self.Head
        while True:
            print(f"{current.HeSo}x^{current.SoMu}", end=" ")
            current = current.KeTiep
            if current != self.Head:
                print("+", end=" ")
            else:
                break
        print()

dathuc = DaThuc()
dathuc.Them(3, 2)
dathuc.Them(4, 3)
dathuc.Them(2, 1)

print("Da thuc sau khi them:")
dathuc.InDaThuc()  
