#tujuan dari kode ini adalah untuk membuktikan bahwa python adalah pass by reference bukan pass by value
#artinya nilai yang di edit dan kemudian disimpan tidak mengubah alamat memori 


def ubahNilai(p):
    print("\nDi dalam fungsi")
    print("p lama", p)
    print("Id p lama", id(p))

    p *= 100 # membuat obyek p baru

    print("\np baru", p) #p baru
    print("ID p baru", id(p))
    return

def main():
    a = 5
    print("sebelum pemanggilan fungsi")
    print("a = ", a)
    print("ID a = ", id(a))

    #memanggil fungsi ubahNilai()
    #dengan a sebagai parameter aktualnya
    ubahNilai(a)

    print("\nSetelah pemanggilan fungsi")
    print("a = ", a)
    print("id = ", id(a))

main()
