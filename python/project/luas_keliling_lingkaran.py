import math

#menampilkan informasi program
print('Luas dan keliling lingkaran\n')

#input nilai jari-jari
r = float(input('Masukkan nilai jari-jari: '))

#menghitung luas lingkaran
L = math.pi * (r ** 2)

#menghitung keliling lingkaran
K = 2 * math.pi * r

#menampilkan hasil luas
print(f'Luas Lingkaran Adalah: {L}')

#menampilkan hasil keliling
print(f'Keliling lingkaran adalah: {K}')
