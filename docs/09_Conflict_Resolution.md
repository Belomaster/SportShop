# Разрешение конфликта слияния

## Контекст

Конфликт возник при слиянии ветки `feature/total-v2` в `develop`,
после того как туда уже была влита `feature/total-v1`.

Обе ветки добавляли функцию `total_sum` в `shop.py`, но с разной логикой:

- **`feature/total-v1`** — сумма только по цене:
  ```python
  def total_sum(products):
      return sum(p['price'] for p in products)