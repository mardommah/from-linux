#invers dan determinan



import numpy as np

a = np.array([(1,-1),(1,1)])

print(a)

#invers matrix

#inv = invers
#linalg = fungsi linear algebra / aljabar linear
a_inv = np.linalg.inv(a)
print(a_inv)

#untuk membuntikan bahwa invers nya benar kalikan dengan nilai awal nya jika mengembalikan nilai satuan maka benar

print(np.dot(a,a_inv))




#determinan

det_a = np.linalg.det(a)
det_a_inv = np.linalg.det(a_inv)
print(det_a)
print(det_a_inv)


#fungsi invers dan determinan untuk menyelesaikan persamaan linear