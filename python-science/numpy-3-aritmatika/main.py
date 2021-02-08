import numpy as np

#list dari python
a = [1,2,3,4,5]
b = [6,7,8,9,10]

#array dari numpy
anp = np.array([1,2,3,4,5])
bnp = np.array([6,7,8,9,10])

#elemenwise operation (masing-masing array akan saling menjumlahkan, mengurangi dsb) hanya pada numpy
#semua operasi matematika dasar dalam numpy adalah ELEMENTWISE operation
#perkalian numpy dan perkalian matriks berbeda


#penjumlahan
# hasil = a+b 
hasil2 = anp + bnp

#pengurangan
#pada list python tidak bisa dikurangi antar list
# hasil3 = a-b

#sedangkan pada numpy bisa
hasil4 = anp - bnp

#perkalian
#ini tidak bisa jg 
# hasil5 = a * b

hasil6 = anp * bnp

#pembagian
#Ini tidak bisa
# hasil7 = a / b

hasil8 = anp / bnp

#kuadrat

hasil9 = anp**2 

#Modulus

hasil10 = anp % bnp

#matriks
#multidimensi array numpy

c = np.array(([1,2,3],[4,5,6]))
d = np.array(([7,8,9],[-1,-2,-3]))

#penjumlahan matriks
hasil11 = c + d
hasil12 = c * d

#penjumlahan dilakukan sesuai dengan urutan matriks
# Misal:
# 1 2 3      dan     7 8 9
# 4 5 6              -1 -2 -3
#

#akan dikalikan berurutan dengan contoh 1 x 7, 2 x 8 , 3 x 9  dst
print(hasil11)
print(hasil12)