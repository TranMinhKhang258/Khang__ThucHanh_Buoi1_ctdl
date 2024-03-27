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

    def RutGon(self):
        if self.Head is None:
            print("Da thuc rong")
            return

        current1 = self.Head
        while True:
            current2 = current1.KeTiep
            while current2 != self.Head:
                if current2.SoMu == current1.SoMu:
                    current1.HeSo += current2.HeSo
                    temp = current2.KeTiep
                    current1.KeTiep = temp
                    del current2
                    current2 = temp
                else:
                    current2 = current2.KeTiep
            current1 = current1.KeTiep
            if current1 == self.Head:
                break

        current = self.Head
        previous = None
        while True:
            if current.HeSo == 0:
                if previous is None:
                    temp = current.KeTiep
                    if temp == current: 
                        self.Head = None
                        return
                    else:
                        while temp.KeTiep != self.Head:
                            temp = temp.KeTiep
                        self.Head = current.KeTiep
                        temp.KeTiep = self.Head
                        del current
                        current = self.Head
                else:
                    previous.KeTiep = current.KeTiep
                    temp = current.KeTiep
                    del current
                    current = temp
            else:
                previous = current
                current = current.KeTiep
            if current == self.Head:
                break

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
dathuc.Them(-4, 3)
dathuc.Them(2, 1)

print("Da thuc truoc khi rut gon:")
dathuc.InDaThuc() 

dathuc.RutGon()

print("Da thuc sau khi rut gon:")
dathuc.InDaThuc() 
