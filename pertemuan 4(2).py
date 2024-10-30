#Soal 2: Nilai Ujian

nilai = int(input ("masukan nilai anda/n="))
if nilai >= 75:
    print('Kamu dinyatakan lulus')
elif nilai < 75:
    print('Kamu dinyatakan tidak lulus')

if nilai >= 90:
    print('dengan predikat A')
elif nilai >= 75:
    print('dengan predikat B')
elif nilai >= 65:
    print('dengan predikat C')
elif nilai < 65:
    print('dengan predikat D')
