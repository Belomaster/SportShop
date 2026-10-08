"""Модуль аналитики по заказам."""


def total_revenue(orders):
    """Общая выручка по всем заказам."""
    return sum(o.get("total", 0) for o in orders)


def best_selling_product(orders):
    """Самый продаваемый товар (по количеству)."""
    counts = {}
    for order in orders:
        for item in order.get("items", []):
            name = item.get("name", "?")
            counts[name] = counts.get(name, 0) + item.get("quantity", 0)
    if not counts:
        return None
    return max(counts.items(), key=lambda x: x[1])


def average_order_total(orders):
    """Средняя сумма заказа."""
    if not orders:
        return 0
    return sum(o.get("total", 0) for o in orders) / len(orders)
