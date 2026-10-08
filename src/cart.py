"""Модуль работы с корзиной покупателя."""


def add_to_cart(cart, products, product_id, size, quantity):
    """Добавляет товар в корзину. Возвращает (успех, сообщение)."""
    product = next((p for p in products if p.get("id") == product_id), None)
    if product is None:
        return False, f"Товар с ID={product_id} не найден"

    item = {
        "id": product["id"],
        "name": product["name"],
        "brand": product.get("brand", ""),
        "price": product["price"],
        "size": size,
        "quantity": quantity,
    }
    cart.append(item)
    return True, f"Добавлено: {product['name']} (размер {size}, {quantity} шт.)"


def remove_from_cart(cart, product_id, size):
    """Удаляет товар из корзины по ID и размеру."""
    for i, item in enumerate(cart):
        if item["id"] == product_id and item["size"] == size:
            cart.pop(i)
            return True, "Удалено"
    return False, "Не найдено"


def update_quantity(cart, products, product_id, size, new_qty):
    """Изменяет количество товара в корзине."""
    for item in cart:
        if item["id"] == product_id and item["size"] == size:
            item["quantity"] = new_qty
            return True, "Обновлено"
    return False, "Не найдено"


def cart_total(cart):
    """Считает итоговую сумму корзины с учётом количества."""
    return sum(item["price"] * item["quantity"] for item in cart)
