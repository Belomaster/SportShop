"""Модуль работы с каталогом товаров."""


def get_low_stock(products, threshold=3):
    """Возвращает товары с количеством <= threshold, отсортированные по возрастанию."""
    if not products:
        return []
    low = [p for p in products if p.get("quantity", 0) <= threshold]
    return sorted(low, key=lambda p: p["quantity"])


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


def count_by_category(products):
    """Возвращает словарь {категория: количество} для товаров с количеством > 0."""
    counts = {}
    for p in products:
        if p.get("quantity", 0) > 0:
            cat = p.get("category", "Без категории")
            counts[cat] = counts.get(cat, 0) + 1
    return dict(sorted(counts.items(), key=lambda x: x[1], reverse=True))


def avg_price(products):
    """Средняя цена товаров."""
    if not products:
        return 0
    return sum(p["price"] for p in products) / len(products)
