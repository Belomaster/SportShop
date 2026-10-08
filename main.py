"""Точка входа приложения SportShop."""
from src.storage import load_products, save_products
from src.catalog import get_low_stock, search_advanced, count_by_category, avg_price
from src.cart import add_to_cart, cart_total
from src.orders import create_order, print_order, save_orders, load_orders
from src.analytics import total_revenue, best_selling_product, average_order_total


def main():
    products = load_products("data/products.json")
    cart = []

    while True:
        print("\n=== SportShop ===")
        print("1. Показать все товары")
        print("2. Товары с низким остатком")
        print("3. Поиск")
        print("4. Аналитика по категориям")
        print("5. Средняя цена")
        print("6. Добавить в корзину")
        print("7. Показать корзину / сумму")
        print("8. Оформить заказ")
        print("9. Аналитика по заказам")
        print("0. Выход")
        choice = input("Выбор: ").strip()

        if choice == "1":
            for p in products:
                print(p)
        elif choice == "2":
            for p in get_low_stock(products):
                print(p)
        elif choice == "3":
            q = input("Запрос: ").strip()
            for p in search_advanced(products, q):
                print(p)
        elif choice == "4":
            print(count_by_category(products))
        elif choice == "5":
            print(f"Средняя цена: {avg_price(products):.2f}")
        elif choice == "6":
            try:
                pid = int(input("ID товара: "))
                size = input("Размер: ").strip()
                qty = int(input("Количество: "))
                ok, msg = add_to_cart(cart, products, pid, size, qty)
                print(msg)
            except ValueError:
                print("Ошибка ввода")
        elif choice == "7":
            for item in cart:
                print(item)
            print(f"Сумма: {cart_total(cart)}")
        elif choice == "8":
            client = input("Имя клиента: ").strip()
            order = create_order(cart, client)
            if order:
                print_order(order)
                orders = load_orders("data/orders.json")
                orders.append(order)
                save_orders(orders, "data/orders.json")
                cart.clear()
            else:
                print("Корзина пуста")
        elif choice == "9":
            orders = load_orders("data/orders.json")
            print(f"Выручка: {total_revenue(orders)}")
            print(f"Средний чек: {average_order_total(orders):.2f}")
            top = best_selling_product(orders)
            print(f"Топ товар: {top}")
        elif choice == "0":
            break


if __name__ == "__main__":
    main()
