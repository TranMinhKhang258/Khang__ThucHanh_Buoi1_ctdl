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
                if previous is None:
                    new_node.KeTiep = self.Head
                    self.Head = new_node
                else:
                    new_node.KeTiep = current
                    previous.KeTiep = new_node

    def RutGon(self):
        if self.Head is None:
            return
        
        current = self.Head
        previous = None
        somu_set = set() 
        
        while current is not None:
            if current.SoMu in somu_set:
                previous.HeSo += current.HeSo
                previous.KeTiep = current.KeTiep
                current = current.KeTiep
            else:
                somu_set.add(current.SoMu)
                previous = current
                current = current.KeTiep
        
        current = self.Head
        previous = None
        while current is not None:
            if current.HeSo == 0:
                if previous is None:
                    self.Head = current.KeTiep
                    current = self.Head
                else:
                    previous.KeTiep = current.KeTiep
                    current = previous.KeTiep
            else:
                previous = current
                current = current.KeTiep

    def Cong(self, dathuc2):
        result = DaThuc() 
        
        current = self.Head
        while current is not None:
            result.Them(current.HeSo, current.SoMu)
            current = current.KeTiep
        
        current = dathuc2.Head
        while current is not None:
            result.Them(current.HeSo, current.SoMu)
            current = current.KeTiep
        
        result.RutGon()
        
        return result

    def InDaThuc(self):
        current = self.Head
        while current is not None:
            print(f"{current.HeSo}x^{current.SoMu}", end=" ")
            if current.KeTiep is not None:
                print("+", end=" ")
            current = current.KeTiep
        print()

dathuc1 = DaThuc()
dathuc1.Them(3, 2)
dathuc1.Them(4, 3)
dathuc1.Them(2, 1)

dathuc2 = DaThuc()
dathuc2.Them(2, 2)
dathuc2.Them(5, 4)

print("Da thuc 1:")
dathuc1.InDaThuc()  
print("Da thuc 2:")
dathuc2.InDaThuc()  

dathuc3 = dathuc1.Cong(dathuc2)
print("Da thuc 1 + Da thuc 2:")
dathuc3.InDaThuc()  
