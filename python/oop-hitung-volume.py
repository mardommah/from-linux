class Kotak(object):
    def __init__(self, p, l, t):
        self.panjang = p
        self.lebar = l
        self.tinggi = t
    
    def hitungVolume(self):
        return self.panjang * self.lebar * self.tinggi

kotak1 = Kotak(2,3,4)

print("Volume kotak adalah: ", kotak1.hitungVolume(), "cm")