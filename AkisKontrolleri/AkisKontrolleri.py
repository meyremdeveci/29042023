##################### AKIŞ KONTROL : IF ELIF ELSE ########################################
# Program akışında bir sonuc,durum ve değere göre program akışı
# devam edecek ise if elif else deyimleri kullanılır.
# Karar yapıların if ve else 1 kez tanımlanır.
# alternatif bütün durumlar elif keyword'ü tekrar tekrar
# yazılarak kullanılablir
"""
a: int = 10
b: int = 20

if a > b:
    print("a sayısı b sayısından büyüktür.")
elif a == b:
    print("a sayısı ve b sayısı birbirine eşittir.")
else:
    print("a sayısı b sayısından küçüktür.")
"""
"""
Eşitlik                 =>  ==
Eşit değil              =>  !=
Büyüklük                =>  >
Küçüklük                =>  <
Büyük Eşit              =>  >=
Küçük Eşit              =>  <=
Not Değil               =>  !

"""
"""
gun_sayisi: int = int(input("Lütfen adını öğrenmek istediğiniz günün numarasını girin: "))

if gun_sayisi == 1:
    print("Pazartesi")
elif gun_sayisi == 2:
    print("Salı")
elif gun_sayisi == 3:
    print("Çarşamba")
elif gun_sayisi == 4:
    print("Perşembe")
elif gun_sayisi == 5:
    print("Cuma")
elif gun_sayisi == 6:
    print("Cumartesi")
elif gun_sayisi == 7:
    print("Pazar")
else:
    print("Yanlış bir değer girdiniz !!")
"""

# Ödev :
#  Kullanıcıdan 1-7 arası sayı alın.
# Bu alınan sayıyı islami gün isimlerine göre ekrana yazın
#  Örn: 1. gün  Yevmu’l-İs̠neyn
#  Pazar: Yevmu’l-Eḥad
# Pazartesi: Yevmu’l-İs̠neyn
# Salı: Yevmu’s̠-S̠ülās̠ā’
# Link: https://tr.wikipedia.org/wiki/Hicr%C3%AE_takvim


# Ödev :
#  Kullanıcıdan 1-12 arası sayı alın.
# Alınan sayıya göre ayları islami isimlerini yazdırın
# Link: https://tr.wikipedia.org/wiki/Hicr%C3%AE_takvim


# VE VEYA ( and ve or)


"""
gun_sayisi: int = int(input("Lütfen adını öğrenmek istediğiniz günün numarasını girin: "))

if gun_sayisi > 7 or gun_sayisi < 1:
    print("Hatalı gün sayısı")
elif gun_sayisi == 1:
    print("Pazartesi")
elif gun_sayisi == 2:
    print("Salı")
elif gun_sayisi == 3:
    print("Çarşamba")
elif gun_sayisi == 4:
    print("Perşembe")
elif gun_sayisi == 5:
    print("Cuma")
elif gun_sayisi == 6:
    print("Cumartesi")
elif gun_sayisi == 7:
    print("Pazar")
"""

# Kullanıcıdan 1 sayı alın tek mi çift mi olduğunu ekrana yazın
"""
sayi :int =  int(input("Lütfen tipi kontrol edilecek olan sayıyı giriniz: "))

if sayi % 2 == 0:
    print("Bu bir çift sayıdır")
else:
    print("Bu bir tek sayıdır")
    
"""
# SORU: Klavyeden girilen değer: 100'den büyükse karesini,
# küçükse küpünü ekrana yazdıran prog. ( ** üs almak için kullanılır) sayi ** 3
"""
sayi: int = int(input("Lütfen bir sayı giriniz: "))

if sayi > 100:
    print(sayi ** 2)
elif sayi < 100:
    print(sayi ** 3)
else:
    print("Sayı 100'e eşittir.")
"""
# Kullanıcıdan alınan sayının aralığını belirleyiniz
#  0-10  11-20

"""
sayi: int = int(input("Lütfen bir sayı giriniz: "))

if 0 < sayi and sayi < 11:
    print("Sayı 0-10 aralığındadır")
elif 10 < sayi and sayi < 21:
    print("Sayı 10-20 aralığındadır")
elif 20 < sayi and sayi < 31:
    print("Sayı 20-30 aralığındadır")
elif 30 < sayi and sayi < 41:
    print("Sayi 30-40 aralığındadır")
"""

# Klavyeden girilen 4 sayıdan tek ve çift olanları ayrı
# ayrı toplayarak ekrana yazdırınız..
"""
tek_toplam = 0
cift_toplam = 0

s1: int = int(input("Birinci sayı"))

if s1 % 2 == 0:
    cift_toplam += s1
else:
    tek_toplam += s1

s2: int = int(input("İkinci sayı"))

if s2 % 2 == 0:
    cift_toplam += s2
else:
    tek_toplam += s2

s3: int = int(input("Üçüncü sayı"))

if s3 % 2 == 0:
    cift_toplam += s3
else:
    tek_toplam += s3

s4: int = int(input("Dördüncü sayı"))

if s4 % 2 == 0:
    cift_toplam += s4
else:
    tek_toplam += s4

print(f"Tek Sayıların Toplamı : {tek_toplam}")
print(f"Çift Sayıların Toplamı: {cift_toplam}")
"""
"""
ÖDEV:  Kullanıcıdan vize final not girilmesi istensin
not aralığı 0 ile 100 arasında olmalıdır.
# vize ve finalin ortalaması alınsın. Vizenin  %40 ı Finalin %60 (vize*0.4)+(final*0.6)
# 0-44 : Kaldınız
# 45-69: Geçtiniz
# 70-84: İyi
# 85-100: Pekiyi
"""

# Kullanıcıdan isim,yaş,maaşve çocuk sayısı alalım

"""
    Eğer kullanıcının yaşı 45'in altındaysa;
        çocuk sayısına bakılacak ve çocuk sayısı 3^ten az ise çocuk başına 250₺,
         değilse çocuk başına 200₺ maaşa eklenecek
    Eğer kullanıcının yaşı 45 ve üzerinde ise:
        çocuk başına para verilmeyecek direk 500₺ maaşa eklenecek.
    Ekrana "Nesrin Yılmaz Maaşınız: 4000₺" yazılacak.
"""

"""
isim: str = input("İsim: ")
yas: int = int(input("Yaş: "))
maas: float = float(input("Maaş: "))
cocuk_sayisi: int = int(input("Çocuk Sayısı: "))

if yas < 45 and yas > 18:

    if cocuk_sayisi < 3 and cocuk_sayisi >= 0:
        maas += cocuk_sayisi * 250
    else:
        maas += cocuk_sayisi * 200
elif yas >= 45:
    maas += 500

else:
    print("Belirlenen yaş aralığına sahip değilsiniz !")

print(f"İsim: {isim}, Yaş: {yas}, Maaş:{maas}, Çocuk Sayısı:{cocuk_sayisi}")
"""

# Kullanıcı Gİriş Paneli Tasarlayınız.

"""
    Kullanıcıadı/Email ve şifre ile giriş sağlanacak
        Giriş Başarılı ise ekrana "Giriş Başarılı" yazsın
        Değilse
            Kullanıcıya kayıt olmak ister misiniz?
                Hayır ise PEKİ!!!
                Evet Kullanıcıadı, ad, soyad,email,şifre ve şifre tekrarı alarak kayıt yapalım.
                    şifre ve şifretekrarın aynı olması
"""
"""
kullanici_adi: str = "mehmetnuri"
email: str = "info@mehmetnuri.net"
sifre: str = "123456"

print("-----------------------------------GİRİŞ PANELİ-----------------------------------")

username_or_email: str = input("Lütfen kullanıcı adınızı veya e-posta adresiniz giriniz: ")
pasword: str = input("Lütfen şifrenizi giriniz: ")

if (kullanici_adi == username_or_email or email == username_or_email) and (pasword == sifre):
    print("Giriş başarılı !")
else:
    cevap: str = input("Kayıt olmak ister misiniz?(E/H)").upper()  # Bütün harfleri büyük harfe çevir

    if cevap == "H":
        print("Teşekkürler")
    elif cevap == "E":
        ad: str = input("Adınız: ")
        soyad: str = input("Soyadınız: ")
        email: str = input("E-Posta: ")
        password: str = input("Şifreniz: ")
        password_again: str = input("Şifreniz(Tekrar): ")

        if password == password_again:
            print("Hoş geldiniz!")
            print(f"Ad: {ad} Soyad: {soyad}, Email:{email} Şifre: {password}")
        else:
            print("Şifreleriniz birbiriyle uyuşmuyor")
    else:
        print("Hatalı bir seçim yaptınız")
"""
"""
# Girilen 3 sayıyı büyüklük olarak karşılaştıran python uygulamasını yapınız.

a: int = int(input("Birinci sayı: "))
b: int = int(input("İkinci sayı: "))
c: int = int(input("Üçüncü sayı: "))

if a > b and a > c:
    print(f"En büyük sayı a sayısıdır ve değeri: {a}")
elif b > a and b > c:
    print(f"En büyük sayı b sayısıdır ve değeri: {b}")
else:
    print(f"En büyük sayı c sayısıdır ve değeri: {c}")
"""
# ÖZEl YÖNTEMLER

dogru: bool = True
yanlis: bool = False

if dogru:  # if ve elif değer True ise içerisine alır
    print("Doğru")
else:
    print("Yanlış")

if not dogru:  # if ve elif değer True ise içerisine alır
    print("Doğru")
else:
    print("Yanlış")

if not yanlis:
    print("Doğru")
else:
    print("Yanlış")
