import numpy as np

#membuat vector 
a = np.array([1,2,3,4,5])
b = np.array([1.5, 2.5, 5,6,7])

#membuat vector dengan range
# c = np.range(batas_bawah batas_atas step)
c = np.arange(1,10,1)

#membuat liniear space (linspace)
# Menampilkan 4 angka dalam range yang sama
d = np.linspace(1,10,4)

#array multidimensi / matrix

e = np.array([ (1,2,3) , (4,5,6) ])

#menampilkan nilai

#matrix kosong
#f = np.zeros((jumlah_kolom,jumlah_baris))
f = np.zeros((5,5))


#matrix dengan nilai satu 
g = np.ones((5,5))

#matrix identitas, yaitu matriks yang memiliki nilai yang sama dalam satu garis diagonal
h1 = np.identity(5)
h2 = np.eye(5)

#menambah semua nilai matrix +1
# print(e + 1)

print(h1)