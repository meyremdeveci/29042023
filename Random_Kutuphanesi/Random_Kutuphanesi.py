# import random as rd # rastgele sayılar üreten bir kütüphane
# import random  Random kütüphanesinin tamamını import et

from random import random, randint, uniform, randrange

print(random())  # 0-1 arasında rastgele bir sayı veriyor
print(randint(0, 100))  # 0-100 arasında rastgele tam sayı üret
print(uniform(0, 100))  # 0-100 arasında rastgele float sayı üret
print(randrange(0, 101))  # 0-100 arasında rastgele tam sayı üretir başlangıç ve bitiş sayıları dahil edilmez
print(randrange(1, 100, 3))  # 0-100 arasında rastgele tam sayı üretir. 3 e bölümünden kalanı 1 olanları verir
