def cetak_kuadrat_ganjil(n):
    for i in range(1, n + 1):
        if i % 2 != 0:  
            print(i ** 2)

while True:
    try:
        nilai = int(input("Masukkan nilai : "))
        if nilai == "selesai":
            break
        cetak_kuadrat_ganjil(nilai)
    except ValueError:
        print("Masukkan bilangan bulat atau 'selesai' untuk mengakhiri.")
