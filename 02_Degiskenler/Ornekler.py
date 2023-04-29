a: int = 5
b: int = 6
c: int = 7

a = b
c = 95
b = c

print(a)
print(b)
print(c)

# Kullanıcıdan bilgi almak
# Önemli NOT: input ile alınan değerlerin tamamı str

# ad = input("Adınız: ")
# print(ad)

# Tip Dönüşümleri

"""
p: float = 12.23
s = int(p)

print(p)
print(s)

l = float(s)
print(l)

n = "12"
m = "12.56"
print(int(n))
print(float(m))

h = "True"
print(bool(h))

ad = input("Adınız: ")
print(ad)
yas = int(input("Yaşınız: "))
print(yas)

print(type(ad))
print(type(yas))
"""
"""
Kullanıcıdan Ad Soyad maas yas dogum yeri iş yeri adı 
bilgilerini alıp farklı değişkenlerde ve veritiplerine uygun bir şekilde
alıp ekrana yazın.
"""

print("""
[H]=========HARMAN========[-][o][x]
|                                   |
| Programa Hoşgeldiniz!             |
| Sürüm 0.8                         |
| Devam etmek için herhangi         |
| bir düğmeye basın.                |
|                                   |
|=================================|
""")



ad: str = input("Adınız: ")
soyad: str = input("Soyadınız: ")
maas: float = float(input("Maaşınız: "))
yas: int = int(input("Yaşınız: "))
dogum_yeri: str = input("Doğum Yeriniz: ")
is_yeri_adi: str = input("İş Yeri Adınız: ")

print(ad)
print(soyad)
print(maas)
print(yas)
print(dogum_yeri)
print(is_yeri_adi)

# print özel yöntemler

print(ad, soyad, maas, yas, dogum_yeri, is_yeri_adi)

print("ad: ", ad)
print("soyad: ", soyad)
print("maas: ", maas)
print("yas: ", yas)
print("dogum_yeri: ", dogum_yeri)
print("is_yeri_adi: ", is_yeri_adi)


print("Ad: {} Soyad: {} Maaş:  {} Yaş: {} Doğum Yeri: {} İş Yeri Adı: {}".format(ad,soyad,maas,yas,dogum_yeri,is_yeri_adi))

print("Ad: {0} Soyad: {1} Maaş:  {2} Yaş: {3} Doğum Yeri: {4} İş Yeri Adı: {5}".format(ad,soyad,maas,yas,dogum_yeri,is_yeri_adi))

print(f"Ad: {ad} Soyad: {soyad} Maaş:  {maas} Yaş: {yas} Doğum Yeri: {dogum_yeri} İş Yeri Adı: {is_yeri_adi}")

print(f"""
Ad: {ad} Soyad: {soyad} Maaş:  {maas} 
Yaş: {yas} Doğum Yeri: {dogum_yeri} İş Yeri Adı: {is_yeri_adi}
""")




