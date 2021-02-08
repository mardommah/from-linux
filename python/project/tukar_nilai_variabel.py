#Menukarkan Nilai Variabel

#Menukarkan Nilai variabel A ke B dan sebaliknya

#Masukkan Nilai A
a = int(input('Masukkan Nilai A:'))

#Masukkan Nilai B
b = int(input('Masukkan Nilai B:'))

print('Nilai Sebelum Ditukar:')
print(f'Nilai A = {a}')
print(f'Nilai B = {b}')

#Tukarkan Nilai
c = a  #c adalah variabel bantu
a = b
b = c

#menampilkan hasil pertukaran nilai
print('Nilai Setelah Ditukar:')
print(f'Nilai A = {a}')
print(f'Nilai B = {b}')
