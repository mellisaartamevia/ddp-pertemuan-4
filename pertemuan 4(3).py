#Soal 3: Cek Usia dan Status

usia = int(input('Masukan usia anda/n= '))


if usia >= 18:
    print('Kamu sudah dewasa')
elif usia >= 13 and usia < 17:
    print("kamu saat ini sedang memasuki masa remaja")
elif usia < 18:
    print('kamu masih anak anak')
