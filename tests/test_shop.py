"""
Модульные тесты для shop.py
Практическое занятие №8
"""
import unittest

from shop import (
    get_low_stock,
    search_advanced,
    total_sum,
    cart_total,
    add_to_cart,
    remove_from_cart,
    update_quantity,
)


# ---------- Задание 2: тесты каталога ----------

class TestGetLowStock(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(get_low_stock([]), [])

    def test_no_low_stock(self):
        products = [{'name': 'A', 'sizes': {40: 10}}]
        self.assertEqual(get_low_stock(products), [])

    def test_one_low_stock(self):
        products = [
            {'name': 'A', 'sizes': {40: 1}},
            {'name': 'B', 'sizes': {40: 10}},
        ]
        result = get_low_stock(products)
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]['name'], 'A')

    def test_threshold_custom(self):
        products = [{'name': 'A', 'sizes': {40: 3}}]
        self.assertEqual(len(get_low_stock(products, threshold=5)), 1)
        self.assertEqual(len(get_low_stock(products, threshold=2)), 0)


class TestSearchAdvanced(unittest.TestCase):

    def setUp(self):
        self.products = [
            {'id': 1, 'name': 'Кроссовки Nike', 'brand': 'Nike',
             'category': 'обувь', 'price': 8000, 'sizes': {40: 5, 41: 5}},
            {'id': 2, 'name': 'Мяч Adidas', 'brand': 'Adidas',
             'category': 'инвентарь', 'price': 2000, 'sizes': {5: 10}},
            {'id': 3, 'name': 'Кроссовки Adidas', 'brand': 'Adidas',
             'category': 'обувь', 'price': 6000, 'sizes': {42: 3}},
        ]

    def test_search_by_name(self):
        result = search_advanced(self.products, 'Nike')
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]['id'], 1)

    def test_search_by_category(self):
        result = search_advanced(self.products, '', category='обувь')
        self.assertEqual(len(result), 2)

    def test_search_by_price_range(self):
        result = search_advanced(self.products, '', min_price=3000, max_price=7000)
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]['id'], 3)

    def test_search_combined(self):
        result = search_advanced(self.products, 'Adidas', category='обувь', min_price=5000)
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]['id'], 3)

    def test_search_empty_result(self):
        result = search_advanced(self.products, 'Puma')
        self.assertEqual(result, [])


class TestTotalSum(unittest.TestCase):

    def test_empty_cart(self):
        self.assertEqual(total_sum([]), 0)

    def test_cart_with_items(self):
        products = [
            {'price': 1000, 'quantity': 2},
            {'price': 500, 'quantity': 3},
        ]
        self.assertEqual(total_sum(products), 3500)


# ---------- Задание 3: тесты с ожидаемыми ошибками ----------

class TestAddToCartErrors(unittest.TestCase):

    def test_invalid_size(self):
        products = [{'id': 1, 'name': 'A', 'price': 100, 'sizes': {40: 5}}]
        cart = []
        result, message = add_to_cart(cart, products, 1, 99, 1)
        self.assertFalse(result)
        self.assertIn('размер', message.lower())

    def test_unknown_product(self):
        products = [{'id': 1, 'name': 'A', 'price': 100, 'sizes': {40: 5}}]
        cart = []
        result, message = add_to_cart(cart, products, 999, 40, 1)
        self.assertFalse(result)

    def test_division_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            _ = 1 / 0


# ---------- Задание 5: тесты корзины ----------

class TestCart(unittest.TestCase):

    def setUp(self):
        self.products = [
            {'id': 1, 'name': 'Кроссовки', 'price': 8000, 'sizes': {40: 10, 41: 5}},
            {'id': 2, 'name': 'Мяч', 'price': 2000, 'sizes': {5: 20}},
        ]
        self.cart = []

    def test_add_to_cart_success(self):
        result, _ = add_to_cart(self.cart, self.products, 1, 40, 1)
        self.assertTrue(result)
        self.assertEqual(len(self.cart), 1)
        self.assertEqual(self.cart[0]['quantity'], 1)

    def test_add_to_cart_twice_increases_quantity(self):
        add_to_cart(self.cart, self.products, 1, 40, 2)
        add_to_cart(self.cart, self.products, 1, 40, 3)
        self.assertEqual(len(self.cart), 1)
        self.assertEqual(self.cart[0]['quantity'], 5)

    def test_remove_from_cart(self):
        add_to_cart(self.cart, self.products, 1, 40, 1)
        self.assertTrue(remove_from_cart(self.cart, 1, 40))
        self.assertEqual(len(self.cart), 0)
        self.assertFalse(remove_from_cart(self.cart, 1, 40))

    def test_update_quantity(self):
        add_to_cart(self.cart, self.products, 1, 40, 1)
        self.assertTrue(update_quantity(self.cart, 1, 40, 7))
        self.assertEqual(self.cart[0]['quantity'], 7)

    def test_cart_total(self):
        add_to_cart(self.cart, self.products, 1, 40, 2)  # 16000
        add_to_cart(self.cart, self.products, 2, 5, 3)   # 6000
        self.assertEqual(cart_total(self.cart), 22000)

    def test_cart_total_empty(self):
        self.assertEqual(cart_total(self.cart), 0)


if __name__ == '__main__':
    unittest.main() 