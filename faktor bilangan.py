#Program Menentukan Faktor Bilangan

n = int(input("Masukkan angka : "))

faktor = []
for i in range (1, n+1) :
    if n % i == 0 :
        faktor.append(i)

print("Faktor dari ", n, "adalah ", faktor)