#perkalian matrix
#dalam matrix perkalian adalah kolom dikali baris

import numpy as np

a = np.array(([1,2],
            [4,5]))
        
# b = np.ones([2,2])
b = np.array(([6,7],
            [8,9]))

print("matrix a:")
print(a)

print('matrix b:')
print(b)

#perkalian matrix

#cara 1 menggunakan dot
c1 = np.dot(a,b)

#menggunakan oop
c2 = a.dot(b)  #menempelkan object b ke object a

print('matrix c1')
print(c1)

print('matrix c2')
print(c2)

