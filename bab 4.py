#Bab 4

#huruf.py
#kar = input("Masukkan karakter = ")
#huruf = (kar >= "A" and kar <= "Z") or \
#    (kar >= "a" and kar <= 'z')
#hasil = 'huruf' if huruf \
#    else 'bukan huruf'
#print (kar, 'merupakan', hasil)

#nomor 10
kar = input ("Masukkan karakter = ")
vokal = (kar == ('A' or "I" or 'U' or 'E' or 'O')) or \
    (kar == ('a' or 'i' or 'u' or 'e' or 'o'))
hasil = "merupakan huruf vokal" if vokal \
    else 'bukan huruf vokal'
print (kar, hasil)