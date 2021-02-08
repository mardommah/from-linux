import numpy as np

a = np.array([1,2,3,4])
b = [1,2,3,4]

print(a)
print(b)

a = a + 1 #ini akan menambah satu angka ke semua komponen
# a = b + 1 #ini akan error harus di tulis dalam bentuk array jg

b = b + [1] #menambah akan satu di bagian akhir

print(a)
print(b)