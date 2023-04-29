# Bu benim dosyam
# Bu ikinci yorumum

"""
Dokümantasyon yorum satırı
"""

# Bu benim
# Çok Satırlı
# Yorumum

"""
Değişken Tanımlama
1. DEĞİŞKENİN ADI VERİLİR
2. DEĞİŞKENİN TİPİ (SAYI, YAZI ..VB.)
3. DEĞİŞKENİN DEĞERİ
"""

# TİPLER
# sayısal, mantıksal, karakter

# SAYI TİPLER

# TAM SAYI
# Küsüratı bulunmayan sayılardır -5,-4,-3,-2,-1,0, 1,2,3,4,5
# degisken_adi: tip =  deger

sayi1 = 1
sayi2: int = 2  # Tercih edilen profesyonel yöntem

print(sayi1)
print(sayi2)

# Küsüratlı Sayılar
# Float

sayi3 = 12.2
sayi4: float = 56.23
sayi1 = 19.2
print(sayi3)
print(sayi4)
print(sayi1)

# Karakter Tipler (Stringler)
# A,B,C,D  Merhaba

a_harfi = 'A'
b_harfi: str = 'B'  # String

print(a_harfi)
print(b_harfi)

ad: str = "Mehmet Nuri"
latin_olmayan: str = "алфавит"  # UTF-8
print(ad)
print(latin_olmayan)

# Tip öğrenme
# type() => içerisine gönderilen değerin tipini verir

print(type(1))
print(type(1.2))
print(type("A"))
print(type(latin_olmayan))

# # Mantıksal Veri Tipi (Boolean -> bool ) True False
# True => EVET , Doğru
# False => Hayır , Yanlış

arabasi_varmi = True  # Bu kişinin arabası var anlamına gelir
ucagi_varmi: bool = False  # Bu kişinin uçağı yoktur

print(arabasi_varmi)
print(ucagi_varmi)
print(type(arabasi_varmi))

# Operatörler

### '=' değer atama operatörümüzdür.
a = 25
d = 12.3
c = "Ali"
b = False

# Aritmetiksel Operatörler

"""
Toplama     => +
Çıkarma     => -
Çarpma      => *
Bölme       => /
Mod         => %
Tam Bölme   =>  //
Arttırma    => +=
Azaltma     => -=
"""

# + operatörü değerler sayısal ise toplar, karakter ise birleştirir
sayi1: int = 15
sayi2: int = 25
ad: str = "Mehmet Nuri"
soyad: str = "ÖZTÜRK"

print(sayi1 + sayi2)
print(ad + soyad)

# Toplam
toplam: int = sayi1 + sayi2
print(toplam)

# Çıkarma
fark: int = sayi1 - sayi2
print(fark)

# Çarpma
carpim: int = sayi1 * sayi2
print(carpim)

# Bölme
bolum: float = sayi1 / sayi2
print(bolum)

# Tam bölme
tam_bolum: int = sayi1 // sayi2
print(tam_bolum)

# Mod Alma
kalan: int = sayi1 % sayi2
print(kalan)

# Arttırma
sayi1 += 5  # sayi1 =  sayi1 +5
print(sayi1)

# Azaltma
sayi1 -= 5  # sayi1 = sayi1 -5
print(sayi1)

# Çarp ve Eşitle
sayi1 *= 2
print(sayi1)

# Böl ve eşitle
sayi1 /= 2
print(sayi1)

# Mod Al ve Eşitle
sayi1 %= 2
print(sayi1)

# Tam böl ve eşitle
sayi1 //= 2
print(sayi1)

# İPUCU
"""
Bir değişkenin ramdeki adresine ulaşmak için id() metodu kullanılır
"""
print(id(sayi1))

# ÖZEL NOTLAR

# TEK SATIRDA BİRDEN FAZLA DEĞİŞKEN TANIMLAMA

x = y = z = 12
print(x)
print(y)
print(z)

print(id(x))
print(id(y))
print(id(z))

i, j, k = 12, 36, 56
print(i)
print(j)
print(k)

print(id(i))
print(id(j))
print(id(k))

# Karşılaştırma Operatörleri
"""
Eşitlik kontrolleri daima bool değer döndürür

Eşitlik Kontrolü            ==
Eşit değil kontrolü         !=
Büyüklük kontrolü           >
Küçüklük kontrolü           <
Büyük veya eşit kontrolü    >=
Küçük veya eşit kontrolü    <=

"""
a = 2
b = 3

print(a > b)
print(a < b)
print(a == b)
print(a != b)
print(a <= b)
print(a >= b)

# ve veya  and or

# OR iki durumdan biri doğru ise doğru gelir
kucuk_veya_esit = a < b or a == b
print(kucuk_veya_esit)

buyuk_veya_esit = a > b or a == b
print(buyuk_veya_esit)

# AND(ve)
#  İki koşuldan ikiside doğru ise doğru döner

sonuc = a > 12 and a > 15
print(sonuc)

sonuc2 = a > 0 and a > 1
print(sonuc2)
