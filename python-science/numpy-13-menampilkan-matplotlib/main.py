import numpy as np
import matplotlib.pyplot as plt

#1. persamaan garis
#y = 2x + 3


x = np.arange(1,11,1)
y = 2*x + 3

# print(x)
# print(y)

#plot persamaan garis x terhadap y

plt.figure(1)
plt.plot(x,y)


#2. Lingkaran

jari2 = 5

sudut = np.linspace(0,2*np.pi,100)
x2 = jari2*np.cos(sudut)
y2 = jari2*np.sin(sudut)

plt.figure(2)
plt.plot(x2,y2)
plt.show()

