# file: operator_aritmatika.py

# Ambil input untuk mengisi nilai
a = int(input("Inputkan nilai a: "))
b = int(input("Inputkan nilai b: "))

# Menggunakan operator penjumlahan
c = a + b
print("Hasil {} + {} = {}".format(a, b, c))

# Operator Pengurangan
c = a - b
print("Hasil {} - {} = {}".format(a, b, c))

# Operator Perkalian
c = a * b
print("Hasil {} * {} = {}".format(a, b, c))

# Operator Pembagian
if b != 0:
    c = a / b
    print("Hasil {} / {} = {}".format(a, b, c))
else:
    print("Error: Pembagian dengan nol")

# Operator Sisa Bagi
c = a % b
print("Hasil {} % {} = {}".format(a, b, c))

# Operator Pangkat
c = a ** b
print("Hasil {} ** {} = {}".format(a, b, c))

