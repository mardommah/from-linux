import math

#Program konversi suhu dari fahrenheit ke celcius

#Masukkan nilai celcius
F = int(input('Masukkan Suhu Dalam Fahrenheit: '))

if F < 32 or F > 212: 
    print('Masukkan suhu dengan benar')
else:
    C = 5 * (F - 32) / 9

    #fungsi round adalah untuk membulatkan angka beberapa di belakang koma
    print(f'Suhu dalam Celcius adalah: {round(C,3)}')


