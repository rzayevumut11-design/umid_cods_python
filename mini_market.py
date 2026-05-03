import json
import time
from datetime import datetime

# ---------- Fayl funksiyaları ----------

def load_json(file):
    try:
        with open(file, "r") as f:
            return json.load(f)
    except:
        return []

def save_json(file, data):
    with open(file, "w") as f:
        json.dump(data, f, indent=4)

# ---------- Login sistemi ----------

def login():
    users = load_json("users.json")

    username = input("Username: ")

    for user in users:
        if user["username"] == username:

            # cooldown yoxla
            if user["lock_until"] and time.time() < user["lock_until"]:
                print("10 saniyə gözlə!")
                return None

            for i in range(3):
                password = input("Password: ")

                if password == user["password"]:
                    print("Giriş uğurlu")
                    user["failed_attempts"] = 0
                    user["lock_until"] = None
                    save_json("users.json", users)
                    return user
                else:
                    print("Səhv şifrə")

            # 3 dəfə səhv
            user["lock_until"] = time.time() + 10
            save_json("users.json", users)
            print("3 səhv! 10 saniyə bloklandın")

    print("User tapılmadı")
    return None

# ---------- Məhsullar ----------

def show_products(user):
    products = load_json("products.json")

    for category in products:
        print("\n", category)
        for item in products[category]:
            print(item["id"], item["name"], "-", item["price"], "AZN")

    pid = int(input("Məhsul ID: "))
    qty = int(input("Miqdar: "))

    action = input("B (səbət) / F (favorit): ").lower()

    for category in products:
        for item in products[category]:
            if item["id"] == pid:

                if action == "b":
                    add_to_basket(user, category, item, qty)
                elif action == "f":
                    add_to_favorites(user, category, item)

# ---------- Səbət ----------

def add_to_basket(user, category, item, qty):
    file = f"basket_{user['username']}.json"
    basket = load_json(file)

    basket.append({
        "category": category,
        "product": item["name"],
        "unit": item["price"],
        "qty": qty,
        "line_total": item["price"] * qty
    })

    save_json(file, basket)
    print("Səbətə əlavə olundu")

# ---------- Checkout ----------

def checkout(user):
    file = f"basket_{user['username']}.json"
    basket = load_json(file)

    total = 0
    for item in basket:
        total += item["line_total"]

    print("Ümumi məbləğ:", total)

    if total > user["balance"]:
        print("Balans kifayət deyil")
        return

    user["balance"] -= total

    users = load_json("users.json")
    for u in users:
        if u["username"] == user["username"]:
            u["balance"] = user["balance"]

    save_json("users.json", users)

    # alış tarixçəsi
    purchases_file = f"purchases_{user['username']}.json"
    purchases = load_json(purchases_file)

    purchases.append({
        "time": str(datetime.now()),
        "total": total
    })

    save_json(purchases_file, purchases)

    save_json(file, [])  # səbəti təmizlə

    print("Checkout uğurlu")

# ---------- Favorit ----------

def add_to_favorites(user, category, item):
    file = f"favorites_{user['username']}.json"
    fav = load_json(file)

    fav.append(item)

    save_json(file, fav)
    print("Favoritə əlavə edildi")

# ---------- Əsas menyu ----------

def menu(user):
    while True:
        print("\n1) Məhsullar")
        print("2) Checkout")
        print("3) Balans")
        print("0) Çıxış")

        choice = input("Seçim: ")

        if choice == "1":
            show_products(user)

        elif choice == "2":
            checkout(user)

        elif choice == "3":
            print("Balans:", user["balance"])

        elif choice == "0":
            break

# ---------- Main ----------

user = login()

if user:
    menu(user)