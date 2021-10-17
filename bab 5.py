#bab 5
'''
import math

x1 = int(input ("x1 = "))
x2 = int(input ("x2 = "))
y1 = int(input ("y1 = "))
y2 = int(input ("y2 = "))

jarak = math.sqrt((x2 - x1) ** 2 + \
    (y2 - y1) ** 2)
print ("Jarak = %.2f" %jarak)
'''

'''
# Angsuran pinjaman model flat
import math


pokok = int(input("Pokok pinjaman       = ")) #pokok pinjaman
bungaPerTahun = float(input("Bunga per tahun (%)    = ")) #Bunga dalam setahun
tempoDalamBulan = int(input("Tempo bulan            = ")) #Lama kredit berapa bulan

# Perhitungan angsuran
angsuran = pokok * (1 / tempoDalamBulan +
    bungaPerTahun / 1200)

# Tampilkan hasil
print ("Angsuran per bulan = ", math.ceil(angsuran)) 
'''

'''
# Jarak lat Long
import math

radian = 0.017453277
rbumi = 6371

print ('Perhitungan jarak bumi')
print ('-' *22)

lintang1 = float(input("Lintang 1 = "))
lintang2 = float(input('Lintang 2 = '))
bujur1 = float(input('Bujur 1 = '))
bujur2 = float(input('Bujur 2 = '))

# Ubah ke radian
lintang1 *= radian
lintang2 *= radian

bujur1 *= radian
bujur2 *= radian

#Hitung jarak dua posisi
jarak = rbumi * math.acos((math.sin(lintang1) *
    math.sin(lintang2)) + (math.cos(lintang1) *
    math.cos(lintang2) * math.cos(bujur1-bujur2)))

#Tampilkan hasilnya
print ('Jarak dalam KM = ', jarak)
'''


#Penjualan dengan diskon jika >=200000
'''print('Penjualan Barang')
print('----------------')

beli = int(input('Harga beli = '))

diskon = 0
if beli >= 200000:
    diskon = 0.05 * beli

jumlah = beli - diskon
print('Total harga Rp', jumlah)'''

#nomor 11
'''nilai = int(input('Nilai = '))
if nilai>= 60:
    lulus = True
else: lulus = False
print(lulus)'''

#nomor 12
'''a = int(input('a = '))
if a > 3:
    print(a, 'lebih dari 3')
else:
    print(a, 'tidak lebih dari 3')'''

'''x = int(input('x = '))
if x == 0:
    print('nol')
else:
    print('bukan nol')'''

#nomor 13
'''a = int(input('a = '))
b = int(input('b = '))
c = int(input('c = '))

if a == b or b == c or a == c:
    print('Nilai ada yang bernilai sama')
else:
    print('a = ', a)
    print('b = ', b)
    print('c = ', c)'''

#nomor 14
'''print('Harga papan Arduino Uno')
print('-----------------------')
kuantitas = int(input('Masukkan kuantitas = '))
if kuantitas >100:
    print("Harga per Unit = 58.000")
    harga = kuantitas * 58000
    print('Total harga = Rp', harga)
elif kuantitas >= 41:
    print("Harga per Unit = 65.000")
    harga = kuantitas * 65000
    print('Total harga = Rp', harga)
elif kuantitas >= 21:
    print("Harga per Unit = 68.000")
    harga = kuantitas * 68000
    print('Total harga = Rp', harga)
elif kuantitas >= 13:
    print("Harga per Unit = 72.000")
    harga = kuantitas * 72000
    print('Total harga = Rp', harga)
elif kuantitas >= 6:
    print("Harga per Unit = 75.000")
    harga = kuantitas * 75000
    print('Total harga = Rp', harga)
else:
    print("Harga per Unit = 78.000")
    harga = kuantitas * 78000
    print('Total harga = Rp', harga)'''