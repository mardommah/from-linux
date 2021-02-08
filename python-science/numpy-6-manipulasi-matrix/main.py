#transpose
#vector baris
#reshape

import numpy as np

a = np.array((
            [1,2,3],
            [4,5,6]
            ))

#a shape berfungsi menampilkan ukuran matriks

print('matriks a ukuran: ', a.shape)
print(a)

#transpose matrix adalah mengubah baris menjadi kolom
print('transpose matrix dari a:')
print(a.transpose())
#atau
# print(np.transpose(a))

#menggunakan getter setter
# print(a.T) #T adalah transpose




#flatten / vector baris -> menampilkan vector dalam sebaris
print('flatten matrix a:')
print(a.ravel())
#atau
# print(np.ravel(a))
print('matrix a dengan ukuran: ', a.shape)


#reshape vector baris
print('reshape vector baris:')
print(a.reshape(3,2))

print('matrix a dengan ukuran: ',a.shape)


#perbedaan transpose dan reshape vector adalah:
# transpose akan mengurutkan matriks dengan cara kolom diurutkan dalam bentuk baris dan ukurannya tetap
# sedangkan reshape mengurutkan dalam bentuk kolom, dan bisa diatur jumlah yang akan ingin di reshape
# reshape(jumlah_baris,jumlah_kolom)


#resize berfungsi mengubah matrix
#resize matrix
print("resize matrix a:")
print(a.resize(3,2))

print('matrix a dengan ukuran: ', a.shape)