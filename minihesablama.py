ad = input("Ad:")

yas = int(input("Yaş:"))

ceki = float(input("Çəki:"))

boy = float(input("Boy:"))

saatliq_maas = int(input("Saatlıq_maaş:"))

islediyi_saat_sayi = int(input("İşlədiyin saat sayı:"))

hazirki_il = 2026

dogum_ili = hazirki_il - yas

bmi = ceki / (boy * boy)

maas = saatliq_maas * islediyi_saat_sayi

print("=" * 30)

print("HESABLAMA NƏTİCƏLƏRİ")

print("=" * 30)

print("Ad:", ad)

print("Doğum ili:", dogum_ili)

print("BMI:", bmi)

print("Maaş:", maas)
