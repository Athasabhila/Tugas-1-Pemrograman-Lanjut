def print_squares(n):
    for i in range(n):
        print(i**2)

n = int(input("Masukkan nilai n: "))
print_squares(n)


n = int(input("Masukkan nilai n (1-20): "))
if 1 <= n <= 20:
    print("Nilai i^2 untuk i < n:")
    print_squares(n)
else:
    print("Masukkan tidak valid. Harap masukkan nilai antara 1 dan 20.")

