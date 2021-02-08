import numpy as np

a = np.floor(np.random.randn(1,6)*10) #nilai random dikali 10

print(a)
print('nilai max dari a = ',a.max())

#menentukan posisi nilai tertinggi
#jika ada nilai sama maka yang pertama diambil yang di jadikan nilai max
print('posisi max dari a =',a.argmax())

#mengurutkan dari posisi terendah

print('posisi min dari a=', a.min())

#mencari posisi nilai terendah
#jika ada nilai sama maka yang pertama diambil yang di jadikan nilai min
print('posisi nilai min dari a =', a.argmin())

#mengurutkan berdasar nilai terendah ke tinggi
print('mengurutkan nilai a: ')
print(np.sort(a))

#mengurutkan berdasarkan argument dan urutannya dari terendah ke tinggi
print(np.argsort(a))




