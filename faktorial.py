#Program Menghitung Faktorial

def faktorial(n):
    if 0<=n<2 :
        return 1
    elif n<0 :
        return "Tidak ada"
    else :
        return n*faktorial(n-1)

n = int(input("Masukkan angka : "))
print("Faktorial dari", n, "adalah", faktorial(n))



