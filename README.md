# СпортТовары — система управления магазином

## Описание

Учебный проект — консольное приложение для управления магазином спортивных
товаров. Позволяет вести каталог, искать товары, работать с корзиной,
оформлять заказы и просматривать аналитику по продажам.

## Требования

- Python 3.10+
- Git
- SQLite не используется — данные хранятся в JSON (`data/products.json`, `data/orders.json`)

## Установка

```bash
git clone git@github.com:Belomaster/SportShop.git
cd SportShop
```

## Запуск

```bash
python3.12 main.py
```

## Тестирование

```bash
python3.12 -m unittest discover -s tests -v
```

Ожидаемый результат: `Ran 23 tests ... OK`.

## Сборка

```bash
python3.12 build.py
```

Скрипт проверит версию Python, наличие данных и запустит тесты.

## Структура проекта

```
SportShop/
├── src/
│   ├── __init__.py
│   ├── catalog.py        # работа с каталогом товаров
│   ├── cart.py           # корзина покупателя
│   ├── orders.py         # заказы
│   ├── analytics.py      # аналитика по заказам
│   └── storage.py        # сохранение/загрузка JSON
├── tests/
│   ├── __init__.py
│   ├── test_shop.py          # модульные тесты
│   └── test_integration.py   # интеграционные тесты
├── docs/                 # документация проекта
├── data/
│   └── products.json     # данные о товарах
├── main.py               # точка входа
├── build.py              # скрипт сборки
└── README.md
```

## Использование

После запуска `main.py` откроется консольное меню:

```
=== SportShop ===
1. Показать все товары
2. Товары с низким остатком
3. Поиск
4. Аналитика по категориям
5. Средняя цена
6. Добавить в корзину
7. Показать корзину / сумму
8. Оформить заказ
9. Аналитика по заказам
0. Выход
```

Пример сеанса:

```
Выбор: 3
Запрос: nike
{'id': 1, 'name': 'Мяч Nike', 'brand': 'Nike', 'category': 'Игры', 'price': 1500, 'quantity': 5}
```

## Документация

- [API Reference](docs/17_API_Reference.md)
- [User Guide](docs/18_User_Guide.md)
- [Developer Guide](docs/19_Developer_Guide.md)
- [Final Test Report](docs/20_Final_Test_Report.md)
- [Presentation](docs/21_Presentation.md)

## Авторы

- Belomaster — разработка, тестирование, документация (учебный проект, 2026)

## Лицензия

Учебный проект. Свободное использование в образовательных целях.