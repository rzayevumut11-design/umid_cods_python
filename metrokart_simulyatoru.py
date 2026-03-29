# ======= PIN HISSESI =======
PIN = "6988"
cehd = 0

while cehd < 3:
    pin = input("PİN daxil et: ")

    if pin == PIN:
        print("Düzgün PİN")
        break

    else:
        cehd += 1
        print("Yanliş PİN")
        
if cehd == 3:
    print("Kart bloklandi")
    exit()
    
# ======= BASLANGIC DEYISENLER =======
balans = 0
borc = 0
gedis_sayi = 0
limit = 100
rejim = "normal"

#statistika
umumi_odenis = 0
umumi_endirim = 0
umumi_artirilan = 0

#son emeliyyatlar
emeliyyatlar = []

# ======= ESAS MENYU =======
while True:
    print("\n----- MENU -----")
    print("1. Balansi goster")
    print("2. Balansi artir")
    print("3. Gedis et")
    print("4. Son emeliyyatlar")
    print("5. Statistika")
    print("6. Parametrler")
    print("0. Çixiş")

    secim = input("Seçim et: ")

    # ======= 1. BALANS =======
    if secim == "1":
        print("Balans:", balans)
        print("Borc:", borc)

    # ======= 2. BALANS ARTIR =======
    elif secim == "2":
        mebleg = float(input("Mebleg daxil et: "))

        if mebleg <= 0:
            print("Yanlis mebleg")
        elif mebleg > limit:
            print("Limit asildi")
        else:
            # borc evvel silinir
            if borc > 0:
                if mebleg >= borc:
                    mebleg -= borc
                    borc = 0
                else:
                    borc -= mebleg
                    mebleg = 0

            balans += mebleg
            umumi_artirilan += mebleg

            emeliyyatlar.append(f"Artirildi: +{mebleg} AZN | Balans: {balans}")
            print("Balans artirildi")  
# ======= 3. GEDIS =======
    elif secim == "3":

        # qiymet rejime gore
        if rejim =="telebe":
            qiymet = 0.20
            endirim = 0
        elif rejim =="pensiya":
            qiymet = 0.15
            endirim = 0
        else:
            gedis_sayi += 1

            if gedis_sayi == 1:
                qiymet = 0.40
                endirim = 0
            elif gedis_sayi <= 4:
                qiymet = 0.36
                endirim = 0.04
            else:
                qiymet = 0.30
                endirim = 0.10
        
        # balans yoxlanisi
        if balans >= qiymet:
            balans -= qiymet
            umumi_odenis += qiymet
            umumi_endirim += endirim

            emeliyyatlar.append(f"Gedis: -{qiymet} AZN | Balans: {balans}")
            print("Kecid edildi")

        elif 0.30 <= balans < 0.40:
            print("Tecili kecid edildi") 
            borc += 0.10
            balans = 0

            emeliyyatlar.append("Tecili kecid (borc +0.10)")
        else: 
            print("Balans kifayet deyil")
            if rejim == "normal":
                gedis_sayi -= 1
    # ======= 4. SON EMELIYYATLAR =======
    elif secim == "4":
        n = int(input("Nece emeliyyat gormek isteyirsen: "))
        print("\n--- SON EMELIYYATLAR ---")

        for emel in emeliyyatlar[-n:]:
            print(emel)

    # ======= 5. STATISTIKA =======
    elif secim == "5":
        print("\n--- STATISTIKA ---")
        print("Gedis sayi:", gedis_sayi)
        print("Umumi odenis:", umumi_odenis)
        print("Umumi endirim:", umumi_endirim)
        print("Artirilan mebleg:", umumi_artirilan)

    # ======= 6. PARAMETRLER =======
    elif secim =="6":
        print("\n1. Limit deyis")
        print("2. Rejim sec")

        sec = input("Secim: ")

        if sec =="1":
            limit = float(input("Yeni limit: "))
            print("Limit deyisdi")

        elif sec == "2":
            print("1. Normal")
            print("2. Telebe")
            print("3. Pensiyaci")

            r = input ("Sec: ") 

            if r == "1":
                rejim = "normal"
            elif r == "2":
                rejim = "telebe"
            elif r == "3":
                rejim = "pensiya"

            print("Rejim", rejim)

    # ======= 0. CIXIS =======
    elif secim == "0":
        print("Proqram bitdi")
        break

    else:
        print("Yanlis secim")