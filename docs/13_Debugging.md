# Отладка в VS Code — Практическое занятие №8

## Что отлаживали
Функция `get_low_stock(products, threshold=3)` в `shop.py`.

## Где была точка останова
Строка с `return sorted(low, key=lambda p: p["quantity"])` в функции `get_low_stock`.
Также дополнительно ставилась точка останова на входе в функцию (строка с `def`).

## Ход отладки
1. Запуск: Run → Start Debugging (F5), конфигурация "Python File".
2. Запущен файл `tests/test_shop.py` — он вызвал `get_low_stock`.
3. Программа остановилась на точке останова.
4. В панели Variables проверены значения:
   - `products` — список словарей вида `{'name': 'A', 'sizes': {40: 1}}`;
   - `low` — список товаров, прошедших фильтр (у них есть `sizes`);
   - у элементов `low` **отсутствует** ключ `quantity`.
5. При выполнении `key=lambda p: p["quantity"]` возник `KeyError: 'quantity'`.
6. Step Over (F10) подтвердил, что ошибка именно в лямбде сортировки.
7. Step Into (F11) использовался для захода внутрь вложенных проверок размеров.

## Значения переменных (пример)
| Переменная | Значение |
|---|---|
| `products` | `[{'name': 'A', 'sizes': {40: 1}}, {'name': 'B', 'sizes': {40: 10}}]` |
| `threshold` | 3 |
| `low` | `[{'name': 'A', 'sizes': {40: 1}}]` |
| `p` (в лямбде) | `{'name': 'A', 'sizes': {40: 1}}` — ключа `quantity` нет |

## Найденная ошибка
В `get_low_stock` сортировка шла по несуществующему ключу `quantity`.
У товаров в тестах есть только `sizes` (словарь размер → остаток).

**Было:**
```python
low = [p for p in products if p.get("quantity", 0) <= threshold]
return sorted(low, key=lambda p: p["quantity"])

**Стало:**
```python
low = []
for p in products:
    sizes = p.get("sizes")
    if sizes:
        min_qty = min(sizes.values())
        if min_qty <= threshold:
            low.append((p, min_qty))
    else:
        qty = p.get("quantity", 0)
        if qty <= threshold:
            low.append((p, qty))

low.sort(key=lambda pair: pair[1])
return [p for p, _ in low]