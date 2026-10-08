"""Интеграционный тест полного цикла: каталог → корзина → заказ → JSON."""
import os
import unittest

from src.catalog import get_low_stock, search_advanced
from src.cart import add_to_cart, cart_total
from src.orders import create_order, save_orders, load_orders
from src.storage import load_products


class TestIntegration(unittest.TestCase):

    def setUp(self):
        self.products = load_products("data/products.json")
        self.cart = []
        self.orders_file = "data/test_orders.json"

    def tearDown(self):
        if os.path.exists(self.orders_file):
            os.remove(self.orders_file)

    def test_full_cycle(self):
        # 1. Загрузка товаров
        self.assertGreater(len(self.products), 0)

        # 2. Добавление в корзину
        result, msg = add_to_cart(self.cart, self.products, 1, "M", 2)
        self.assertTrue(result, msg)
        self.assertEqual(len(self.cart), 1)

        # 3. Создание заказа
        order = create_order(self.cart, "Тестовый клиент", self.products)
        self.assertIsNotNone(order)
        self.assertGreater(order["total"], 0)

        # 4. Сохранение в JSON
        save_orders([order], self.orders_file)

        # 5. Загрузка из JSON
        loaded = load_orders(self.orders_file)
        self.assertEqual(len(loaded), 1)

        # 6. Проверка суммы
        self.assertEqual(loaded[0]["total"], order["total"])

    def test_catalog_and_cart(self):
        """Каталог + корзина: ищем товар, добавляем, считаем сумму."""
        found = search_advanced(self.products, "nike")
        self.assertEqual(len(found), 1)

        add_to_cart(self.cart, self.products, found[0]["id"], "L", 3)
        self.assertEqual(cart_total(self.cart), found[0]["price"] * 3)

    def test_low_stock(self):
        """Проверка функции get_low_stock из модуля catalog."""
        low = get_low_stock(self.products, threshold=3)
        self.assertGreaterEqual(len(low), 1)
        for p in low:
            self.assertLessEqual(p["quantity"], 3)


if __name__ == "__main__":
    unittest.main()
