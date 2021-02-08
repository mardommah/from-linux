#untuk dua dimensi!!!

import numpy as np

#(2,2) artinya matriks 2 x 2

#rand(baris,kolom)
a = np.floor(np.random.rand(2,3)*10) #matriks 2x3


print(a)

print('nilai max dari a = ', a.max())
print('posisi max dari a = ', a.argmax())
print('nilai min dari a =', a.min())
print('posisi min dari a = ', a.argmin())

print("mengurutkan nilai dari a: ")
print(np.sort(a))
print(np.argsort(a))