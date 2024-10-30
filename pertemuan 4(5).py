#Soal 5: Pembelian Diskon

# Meminta pengguna untuk memasukkan jumlah pembelian
jumlah_pembelian = float(input("Masukkan jumlah pembelian: "))

# Menghitung total harga dengan atau tanpa diskon
total_harga = jumlah_pembelian * 0.9 if jumlah_pembelian > 100 else jumlah_pembelian

# Menampilkan total harga
print(f"Total harga setelah diskon (jika ada): {total_harga}")
