jumlah_barang = int(input("Masukkan jumlah barang: "))
total_harga = 0

for i in range(1, jumlah_barang + 1):
    harga = float(input(f"Masukkan harga barang ke-{i}: "))
    total_harga += harga

print(f"Total belanjaan: Rp. {total_harga:,.2f}")