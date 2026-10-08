import json
from datetime import datetime

PRODUCTS_FILE = "products.json"


def load_products(filename=PRODUCTS_FILE):
    """Загружает список товаров из JSON-файла."""
    try:
        with open(filename, "r", encoding="utf-8") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def save_products(products, filename=PRODUCTS_FILE):
    """Сохраняет список товаров в JSON-файл."""
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(products, f, ensure_ascii=False, indent=2)


# ---------- US-1. Товары с низким остатком ----------

def get_low_stock(products, threshold=3):
    """
    Возвращает список товаров с низким остатком (<= threshold),
    отсортированный по возрастанию остатка.

    Поддерживает два формата товара:
      • {'name': ..., 'sizes': {40: 1, 41: 5}} — остатки по размерам;
      • {'name': ..., 'quantity': 2}            — общий остаток.
    """
    if not products:
        return []

    low = []
    for p in products:
        sizes = p.get("sizes")
        if sizes:
            # Есть словарь размеров — берём минимальный остаток
            min_qty = min(sizes.values())
            if min_qty <= threshold:
                low.append((p, min_qty))
        else:
            # Иначе — общее поле quantity
            qty = p.get("quantity", 0)
            if qty <= threshold:
                low.append((p, qty))

    # Сортируем по возрастанию остатка и возвращаем сами товары
    low.sort(key=lambda pair: pair[1])
    return [p for p, _ in low]


def highlight_low_stock(products, threshold=3):
    """Выводит список товаров с низким остатком в консоль."""
    low = get_low_stock(products, threshold)
    if not low:
        print("Нет товаров с низким остатком")
        return
    print(f"{'Название':<20}{'Бренд':<15}{'Кол-во':>8}")
    for p in low:
        qty = min(p["sizes"].values()) if p.get("sizes") else p.get("quantity", 0)
        print(f"{p['name']:<20}{p.get('brand', '-'):<15}{qty:>8}")


# ---------- US-2. Поиск по названию и бренду ----------

def search_advanced(products, query, category=None, min_price=None, max_price=None):
    """Расширенный поиск по названию/бренду с фильтрами по категории и цене."""
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


# ---------- US-3. Аналитика по категориям ----------

def count_by_category(products):
    """Возвращает словарь {категория: количество} для товаров с количеством > 0."""
    counts = {}
    for p in products:
        if p.get("quantity", 0) > 0:
            cat = p.get("category", "Без категории")
            counts[cat] = counts.get(cat, 0) + 1
    return dict(sorted(counts.items(), key=lambda x: x[1], reverse=True))


# ---------- US-6. Добавление нового товара ----------

def add_product(products, name, brand, category, price, quantity):
    """Добавляет новый товар с проверкой на дубликат."""
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


# ---------- US-7. Удаление товара ----------

def remove_product(products, product_id):
    """Удаляет товар по ID с подтверждением."""
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


# ---------- US-4. Сумма заказа (v2) ----------

def total_sum(products):
    """Считает сумму заказа с учётом количества."""
    return sum(p['price'] * p['quantity'] for p in products)


# ---------- Корзина покупателя ----------

def cart_total(cart):
    """Считает итоговую сумму корзины с учётом количества каждой позиции."""
    return sum(item['price'] * item['quantity'] for item in cart)


# ---------- Корзина (занятие №8) ----------

def add_to_cart(cart, products, product_id, size, quantity=1):
    """
    Добавляет товар в корзину.
    cart: список словарей {'id', 'name', 'size', 'price', 'quantity'}
    products: список товаров с ключами 'id', 'name', 'price', 'sizes' (dict {размер: кол-во})
    Возвращает (True, 'сообщение') или (False, 'сообщение об ошибке').
    """
    product = next((p for p in products if p.get('id') == product_id), None)
    if product is None:
        return False, 'товар не найден'

    sizes = product.get('sizes', {})
    if size not in sizes:
        return False, f'размер {size} не найден'

    if sizes[size] < quantity:
        return False, 'недостаточно товара на складе'

    # Если позиция уже в корзине — увеличиваем количество
    for item in cart:
        if item['id'] == product_id and item['size'] == size:
            item['quantity'] += quantity
            sizes[size] -= quantity
            return True, 'количество увеличено'

    cart.append({
        'id': product_id,
        'name': product['name'],
        'size': size,
        'price': product['price'],
        'quantity': quantity,
    })
    sizes[size] -= quantity
    return True, 'добавлено'


def remove_from_cart(cart, product_id, size):
    """Удаляет позицию из корзины. Возвращает True/False."""
    for i, item in enumerate(cart):
        if item['id'] == product_id and item['size'] == size:
            cart.pop(i)
            return True
    return False


def update_quantity(cart, product_id, size, new_quantity):
    """Меняет количество позиции. Если new_quantity <= 0 — удаляет."""
    if new_quantity <= 0:
        return remove_from_cart(cart, product_id, size)
    for item in cart:
        if item['id'] == product_id and item['size'] == size:
            item['quantity'] = new_quantity
            return True
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