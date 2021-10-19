#Bab 6

#sentinel
cacah = 0
total = 0

data = int(input('Masukkan data. (-1 = selesai) : '))

while data != -1:
    cacah += 1 #Naikkan sebesar 1
    total += data #Tambahkan data ke total

    data = int (input('Masukkan data. (-1 = selesai) :'))

#Hitung rata-rata
rerata = total / cacah
print('Rata-rata = ', rerata)

#else while
bilangan = 1
while bilangan <= 5:
    print(bilangan)
    bilangan = bilangan + 1
else:
    print('***', bilangan,
        '-> pemberhenti perulangan')

#for
for bilangan in range (1, 6):
    print(bilangan)

print('-' * 15)

#for -1
for bilangan in range (5, 0, -1):
    print(bilangan)

#breakfor
for bilangan in range (1, 9):
    if bilangan == 5:
        break
    print(bilangan)
else:
    print(bilangan, '*** akhir for')

print('--- selesai')

#deret kuadrat
n = int(input())
for kuadrat in range (1, n + 1):
    print(kuadrat ** 2)
    kuadrat += 1

n = int(input())
for kuadrat in range (1, n + 1):
    print(kuadrat * kuadrat)

#deret bilangan

#nomor 11
s = 0
for j in range(1, 5):
    s = s + j
print(s)

#nomor 12
for b in range (1, 4):
    for k in range (1, 3):
        print(b * k, end='')
    print()

#nomor 13
a = 2
b = 100
while a <= b:
    if a % 8 == 0:
        print(a)
    a += 1

for x in range(2, 100 + 1):
    if x % 8 == 0:
        print(x)

#nomor 14
for y in range(2, 30 + 1):
    print(y * y)
    y += 1

#nomor 15; parallelogram
n = int(input('n = '))
for z in range (n, 0, -1):
    print(' ' * z, end='')
    print('*' * n)

n = int(input('n = '))
for z in range (0, n, 1):
    print(' ' * z, end='')
    print('*' * n)

#nomor 16 kotak berlubang dan pejal
'''n = int(input('n (antara 3 sampai 9) : '))
if n >= 3 or n <= 9:
    print('*' * n, " ", "*" * n)
    for j in range(0, n + 1):
        print()'''

