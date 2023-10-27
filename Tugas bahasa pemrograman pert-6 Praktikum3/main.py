# Mengimpor modul math untuk nilai konstanta pi
import math

# Meminta pengguna untuk memasukkan jari-jari lingkaran
jari_jari = float(input("Masukkan jari-jari lingkaran: "))

# Menghitung luas lingkaran (A = π * r^2)
luas = math.pi * jari_jari**2

# Menghitung keliling lingkaran (K = 2 * π * r)
keliling = 2 * math.pi * jari_jari

# Menampilkan hasil
print(f"Luas lingkaran: {luas}")
print(f"Keliling lingkaran: {keliling}") 