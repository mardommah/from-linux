
def ubahNilai(p):
    p *= 100
    print("Nilai didalam p")
    print(p)
    return


def main():
    
    a = 5
    
    print("Sebelum pemanggilan fungsi")
    print(a, "\n")

    #memanggil fungsi ubahNilai()
    #dengan a sebagai parameter aktualnya
    print ("nilai pada function ubahNilai")
    ubahNilai(a)

    print("\nNilai di dalam a")
    print(a)

main()    
