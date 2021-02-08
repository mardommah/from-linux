import numpy as np

a = np.array([(2,3),(1,2)])
y = np.array([23,14])

#ditanyakan X = ....?

# print(a)

#penyelesaian
a_inv = np.linalg.inv(a)
x1 = np.dot(a_inv, y)
#hasil
print(x1)


# Cara Lain

x2 = np.linalg.solve(a,y)

print(x2)

