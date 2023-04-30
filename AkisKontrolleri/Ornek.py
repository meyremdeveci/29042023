vize: int = int(input("Vize Notunuz: "))
final: int = int(input("Final Notunuz: "))

sonuc: float = float((vize * 0.4) + (final * 0.6))

print(f"Ortalama : {sonuc}")

if sonuc > 84.9:
    print("AA")
elif 74.9 < sonuc < 85:
    print("BA")
elif 59.9 < sonuc < 75:
    print("CB")
elif 49.9 < sonuc < 60:
    print("CC")
else:
    print("FF")
