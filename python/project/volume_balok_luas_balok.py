#Menghitung volume dan Luas permukaan balok

#menghitung volume balok

#masukkan nilai panjang balok
p = int(input('Masukkan Panjang Balok(cm):'))

#masukkan nilai lebar balok
l = int(input('Masukkan Lebar Balok(cm):'))

#masukkan tinggi balok
t = int(input('Masukkan Tinggi Balok(cm):'))

#Hitung Volume Balok
V = p * l * t

print(f'Volume Balok sebesar {V} cm')

#menghitung Luas Permukaan Balok
LP = 2 * (p*l + p*t + l*t)

print(f'Luas Permukaan Balok Sebesar {LP} cm')
