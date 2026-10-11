# API Reference — проект «СпортТовары»

Описание всех публичных функций модулей `src/*.py`.

---

## Модуль `src.catalog`

### `get_low_stock(products, threshold=3)`

Возвращает список товаров с количеством ≤ `threshold`, отсортированный по возрастанию.

**Параметры:**
- `products` (list[dict]) — список товаров.
- `threshold` (int, по умолчанию 3) — порог количества.

**Возвращает:** `list[dict]` — товары с низким остатком.

**Пример:**
```python
from src.catalog import get_low_stock
low = get_low_stock(products, threshold=3)
for p in low:
    print(p["name"])
```

---

### `search_advanced(products, query, category=None, min_price=None, max_price=None)`

Расширенный поиск по названию/бренду с фильтрами.

**Параметры:**
- `products` (list[dict]) — список товаров.
- `query` (str) — поисковый запрос.
- `category` (str | None) — фильтр по категории.
- `min_price` (float | None) — минимальная цена.
- `max_price` (float | None) — максимальная цена.

**Возвращает:** `list[dict]` — подходящие товары.

---

### `count_by_category(products)`

Возвращает словарь `{категория: количество}` для товаров с `quantity > 0`, отсортированный по убыванию.

**Возвращает:** `dict[str, int]`.

---

### `avg_price(products)`

Средняя цена товаров.

**Возвращает:** `float` (0, если список пуст).

---

## Модуль `src.cart`

### `add_to_cart(cart, products, product_id, size, quantity)`

Добавляет товар в корзину.

**Возвращает:** `(bool, str)` — успех и сообщение.

---

### `remove_from_cart(cart, product_id, size)`

Удаляет товар по ID и размеру.

**Возвращает:** `(bool, str)`.

---

### `update_quantity(cart, products, product_id, size, new_qty)`

Изменяет количество товара в корзине.

**Возвращает:** `(bool, str)`.

---

### `cart_total(cart)`

Итоговая сумма корзины с учётом количества.

**Возвращает:** `float`.

---

## Модуль `src.orders`

### `create_order(cart, client_name, products=None)`

Создаёт заказ из содержимого корзины.

**Возвращает:** `dict | None` — заказ или None, если корзина пуста.

---

### `print_order(order)`

Печатает заказ в консоль.

---

### `save_orders(orders, filename="orders.json")`

Сохраняет список заказов в JSON.

---

### `load_orders(filename="orders.json")`

Загружает список заказов из JSON.

**Возвращает:** `list[dict]` (пустой список, если файла нет).

---

## Модуль `src.analytics`

### `total_revenue(orders)`

Общая выручка по всем заказам.

**Возвращает:** `float`.

---

### `best_selling_product(orders)`

Самый продаваемый товар по количеству.

**Возвращает:** `tuple[str, int] | None`.

---

### `average_order_total(orders)`

Средняя сумма заказа.

**Возвращает:** `float` (0, если заказов нет).

---

## Модуль `src.storage`

### `load_products(filename="data/products.json")`

Загружает список товаров из JSON.

**Возвращает:** `list[dict]`.

---

### `save_products(products, filename="data/products.json")`

Сохраняет товары в JSON.

---

## Возможные исключения

- `FileNotFoundError` — обрабатывается внутри `load_products` / `load_orders`.
- `json.JSONDecodeError` — обрабатывается, возвращается пустой список.
- `KeyError` — может возникнуть, если формат данных нарушен (см. `docs/15_Integration_Errors.md`). 