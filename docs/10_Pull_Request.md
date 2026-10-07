# PR: feature/search-advanced → develop

**Автор:** Belomaster
**Дата:** 07.10.2026
**Ревьюер:** <ФИО преподавателя>

## Что сделано

- Реализована функция `search_advanced(products, query, category=None, min_price=None, max_price=None)`.
- Поиск работает по частичному совпадению названия и бренда (регистр не важен).
- Поддерживается фильтрация по категории, минимальной и максимальной цене.
- Добавлен docstring с описанием функции.

## Изменённые файлы

- `shop.py` — функция `search_advanced`.

## Как проверить

1. Открыть `shop.py` в редакторе.
2. Убедиться, что функция `search_advanced` определена.
3. Запустить тестовый сценарий:

```python
products = [
    {"name": "Мяч Nike", "brand": "Nike", "category": "Игры", "price": 1500, "quantity": 5},
    {"name": "Гантель", "brand": "Fit", "category": "Фитнес", "price": 800, "quantity": 2},
]
print(search_advanced(products, "nike"))                    # 1 товар
print(search_advanced(products, "", category="Фитнес"))     # 1 товар
print(search_advanced(products, "", min_price=1000))        # 1 товар