import numpy as np

#jika sebuah array dikalikan langsung akan menggunakan operasi elementwise (dikali atau dijumlah langsung)
#contoh:

a = np.array([1,2,3])
b = np.array([4,5,6])

matrixa = np.zeros((2,3))
matrixb = np.ones((2,3))

# print(a+b)

#jika ingin ditambah di belakang nya atau di sambung caranya :
#stacking matrix

#hstack = menyusun secara horizontal
#vstack = menyusun secara vertikal

c = np.hstack((a,b))
d = np.vstack((a,b))

matrixc = np.hstack((matrixa,matrixb))
matrixd = np.vstack((matrixa,matrixb))

print(c)
print(d)

print(matrixc)
print(matrixd)
