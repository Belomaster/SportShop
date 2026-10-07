import json
from datetime import datetime

PRODUCTS_FILE = "products.json"

def load_products(filename=PRODUCTS_FILE):
    try:
        with open(filename, "r", encoding="utf-8") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_products(products, filename=PRODUCTS_FILE):
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(products, f, ensure_ascii=False, indent=2)

# ---------- US-1 ----------
def get_low_stock(products, threshold=3):
    """Возвращает список товаров с количеством <= threshold, отсортированный по возрастанию."""
    low = [p for p in products if p.get("quantity", 0) <= threshold]
    return sorted(low, key=lambda p: p["quantity"])

def highlight_low_stock(products, threshold=3):
    low = get_low_stock(products, threshold)
    if not low:
        print("Нет товаров с низким остатком")
        return
    print(f"{'Название':<20}{'Бренд':<15}{'Кол-во':>8}")
    for p in low:
        print(f"{p['name']:<20}{p.get('brand', '-'):<15}{p['quantity']:>8}")

# ---------- US-2 ----------
def search_advanced(products, query, category=None, min_price=None, max_price=None):
    q = query.lower().strip()
    result = []
    for p in products:
        name = p.get("name", "").lower()
        brand = p.get("brand", "").lower()
        if q and q not in name and q not in brand:
            continue
        if category and p.get("category") != category:
            continue
        price = p.get("price", 0)
        if min_price is not None and price < min_price:
            continue
        if max_price is not None and price > max_price:
            continue
        result.append(p)
    return result

# ---------- US-3 ----------
def count_by_category(products):
    counts = {}
    for p in products:
        if p.get("quantity", 0) > 0:
            cat = p.get("category", "Без категории")
            counts[cat] = counts.get(cat, 0) + 1
    return dict(sorted(counts.items(), key=lambda x: x[1], reverse=True))

# ---------- US-6 ----------
def add_product(products, name, brand, category, price, quantity):
    if any(p["name"].lower() == name.lower() and p.get("brand", "").lower() == brand.lower()
           for p in products):
        print(f"Товар '{name}' от бренда '{brand}' уже существует.")
        return False
    if price <= 0 or quantity < 0:
        print("Ошибка: цена должна быть > 0, количество ≥ 0.")
        return False
    new_id = max((p.get("id", 0) for p in products), default=0) + 1
    products.append({
        "id": new_id,
        "name": name,
        "brand": brand,
        "category": category,
        "price": price,
        "quantity": quantity,
    })
    print(f"Товар '{name}' добавлен (ID={new_id}).")
    return True

# ---------- US-7 ----------
def remove_product(products, product_id):
    for i, p in enumerate(products):
        if p.get("id") == product_id:
            answer = input(f"Удалить '{p['name']}'? (y/n): ").strip().lower()
            if answer == "y":
                products.pop(i)
                print("Товар удалён.")
                return True
            print("Отмена.")
            return False
    print(f"Товар с ID={product_id} не найден.")
    return False

# ---------- Меню ----------
def main():
    products = load_products()
    while True:
        print("\n=== SportShop ===")
        print("1. Показать все товары")
        print("2. Товары с низким остатком")
        print("3. Поиск")
        print("4. Аналитика по категориям")
        print("5. Добавить товар")
        print("6. Удалить товар")
        print("0. Выход")
        choice = input("Выбор: ").strip()

        if choice == "1":
            for p in products:
                print(p)
        elif choice == "2":
            highlight_low_stock(products)
        elif choice == "3":
            q = input("Запрос: ").strip()
            res = search_advanced(products, q)
            print(f"Найдено: {len(res)}")
            for p in res:
                print(p)
        elif choice == "4":
            print(count_by_category(products))
        elif choice == "5":
            name = input("Название: ")
            brand = input("Бренд: ")
            category = input("Категория: ")
            price = float(input("Цена: "))
            qty = int(input("Количество: "))
            add_product(products, name, brand, category, price, qty)
            save_products(products)
        elif choice == "6":
            pid = int(input("ID товара: "))
            remove_product(products, pid)
            save_products(products)
        elif choice == "0":
            save_products(products)
            break

if __name__ == "__main__":
    main()