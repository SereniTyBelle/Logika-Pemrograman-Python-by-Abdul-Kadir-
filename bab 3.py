#Nomor 17
diskon=0.1
total_pemb=float(input("Masukkan total pembelian: "))
print("Besar diskon: 10%")
total_disk= total_pemb * diskon
total_penj= total_pemb - total_disk
print('Total yang dibayarkan: %.2f' %(total_penj))

#Nomor 18
badu=int(input('Masukkan umur Badu: '))
x=badu
x-=2
print('Umur Badu adalah ', badu)
print('Umur Sita adalah ', x)
print('Jumlah umur mereka adalah ', badu + x)

#Nomor 15
a=int(input("Masukkan angka: "))
print(f'{a:*>10}')
