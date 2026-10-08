# Отчёт об интеграции модулей

## Какие модули были выделены

Монолитный `shop.py` разбит на 5 модулей в папке `src/`:

| Модуль | Назначение | Функции |
|--------|-----------|---------|
| `catalog.py` | Каталог товаров | `get_low_stock`, `search_advanced`, `count_by_category`, `avg_price` |
| `cart.py` | Корзина покупателя | `add_to_cart`, `remove_from_cart`, `update_quantity`, `cart_total` |
| `orders.py` | Заказы | `create_order`, `print_order`, `save_orders`, `load_orders` |
| `analytics.py` | Аналитика по заказам | `total_revenue`, `best_selling_product`, `average_order_total` |
| `storage.py` | Сохранение и загрузка | `load_products`, `save_products` |

Точка входа — `main.py` в корне проекта.

## Какие импорты используются

В `main.py`:

```python
from src.storage import load_products, save_products
from src.catalog import get_low_stock, search_advanced, count_by_category, avg_price
from src.cart import add_to_cart, cart_total
from src.orders import create_order, print_order, save_orders, load_orders
from src.analytics import total_revenue, best_selling_product, average_order_total