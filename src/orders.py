"""Модуль работы с заказами."""
import json
from datetime import datetime


def create_order(cart, client_name, products=None):
    """Создаёт заказ из содержимого корзины."""
    if not cart:
        return None
    total = sum(item["price"] * item["quantity"] for item in cart)
    order = {
        "client": client_name,
        "items": [dict(item) for item in cart],
        "total": total,
        "created_at": datetime.now().isoformat(timespec="seconds"),
    }
    return order


def print_order(order):
    """Печатает заказ в консоль."""
    if not order:
        print("Заказ пуст")
        return
    print(f"\nЗаказ для {order['client']} от {order['created_at']}")
    for item in order["items"]:
        print(f"  {item['name']} (размер {item['size']}) x {item['quantity']} = {item['price'] * item['quantity']}")
    print(f"Итого: {order['total']}")


def save_orders(orders, filename="orders.json"):
    """Сохраняет список заказов в JSON."""
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(orders, f, ensure_ascii=False, indent=2)


def load_orders(filename="orders.json"):
    """Загружает список заказов из JSON."""
    try:
        with open(filename, "r", encoding="utf-8") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []
