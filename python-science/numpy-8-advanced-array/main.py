import numpy as np


#membuat matriks dengan tipe data tertentu
#bebas diubah baik ke dalam bentuk int, float atau bool
# a = np.array(([1,2,3],[3,4,5]), dtype=float)

# b = np.zeros((2,3), dtype=bool)

# print(a)
# print(b) false


#membuat array dengan menggunakan function

#bisa saja kita mengkuadratkan array dengan fungsi biasa tapi itu merepotkan
#contoh:

# b = np.array([0,1,2,3,4,5,6,7,8,9])

#dan langsung mengkuadratkannya

# print(b**2)


#tetapi ada cara yang lebih baik menggunakan function !!!!
# def nama_function(baris,kolom)
#x = vertical (baris) dan y = horizontal(kolom)

def kuadrat(baris,kolom):
    return kolom**2

def jumlah(baris,kolom):
    return (kolom + baris)

# b = np.fromfunction(fungsi, ukuran matriks, tipe)


b = np.fromfunction(kuadrat, (1,10), dtype=int)
c = np.fromfunction(jumlah, (4,4), dtype=float)


# print(kuadrat(1,5))
# print(b)
# print(c)





#membuat function dengan iterasi
iterable = (x*2 for x in range(6))

d = np.fromiter(iterable, dtype = int)
print(d)



#multi type array array isi campuran
#contoh campuran string dan integer

#S255 = dibaca string dengan max karakter 255
dtipe = [('nama','S255'), ('tinggi',int)]
#keterngan ('variabel1','tipe_data&maxberapa'),(variabel2, tipe_data2)

data = [('ucup',150),
        ('otong',160),
        ('mario',180)   
]

print(data)

e = np.array(data, dtype = dtipe)

print(e)
#pada hasil variabel e terdapat tulisan b'ucup' -> b berarti tipe data 'b' berarti byte
