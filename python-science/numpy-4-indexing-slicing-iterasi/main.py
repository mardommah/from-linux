import numpy as np

a = np.arange(10)**2

print(a)

#mengambil nilai

print('elemen ke 1 dari a adalah', a[0])
print('elemen ke 7 dari a adalah', a[6])
print('elemen paling belakang adalah', a[-1])

#slicing

#elemen ke 6 tidak akan dimasukkan
print('elemen ke 1 sampai 5', a[0:5])
print('elemen ke 4 sampai akhir', a[3:])
print('elemen dari awal sampai 5', a[:5])


#iterasi

# for i in a:
#     print('nilai elemen ke', i)

for i in a:
    for j in range(0,11):
        print('nilai elemen ke', j ,'adalah', i)
        break

