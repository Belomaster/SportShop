* 255c12c US-0: описан hotfix cart-total в docs/11_Hotfix.md
* 9e0b591 hotfix: исправлена функция cart_total (учёт количества)
* 9b9fcce main: добавлена функция cart_total (с ошибкой — без учёта количества)
* 85de149 US-2: создан docs/10_Pull_Request.md для PR
* 5ab62a4 US-0: описано разрешение конфликта в docs/09_Conflict_Resolution.md
* c851caf US-0: описано разрешение конфликта в docs/09_Conflict_Resolution.md
* d8e7755 US-0: добавлен .gitignore (исключены __pycache__, *.pyc, products.json и др.)
*   646e10f Разрешён конфликт в total_sum
|\  
| * 4efc37b US-4: добавлена функция total_sum (с учётом количества)
* | 4f8d89d US-4: добавлена функция total_sum (без учёта количества)
|/  
* a0bcca2 US-1: улучшена функция get_low_stock (docstring, защита от пустого списка)
* dba3086 US-0: добавлена схема Git Flow в docs/08_Git_Flow.md
* 381bfba US-0: добавлена ретроспектива спринта
* b0bd06b US-0: добавлены заметки Daily Standup
* 73f1078 US-1,US-2,US-3,US-7: реализованы функции работы с товарами
* 5107d89 US-0: создана Kanban-доска с WIP-лимитом
* 6d228da US-0: сформирован Sprint Backlog №1
* 4687ebe US-0: добавлен Product Backlog (10 User Story)


## Анализ графа истории

### Сколько веток было создано?

Создано **6 веток** (не считая постоянных `main` и `develop`):

1. `feature/low-stock` — реализация функции `get_low_stock` (US-1).
2. `feature/total-v1` — версия `total_sum` без учёта количества (для конфликта).
3. `feature/total-v2` — версия `total_sum` с учётом количества.
4. `feature/search-advanced` — реализация `search_advanced` (US-2).
5. `hotfix/cart-total` — исправление `cart_total`.

Постоянные ветки: `main` и `develop`.

### Какие слияния произошли?

| # | Что сливали | Куда | Тип |
|---|-------------|------|-----|
| 1 | `feature/low-stock` | `develop` | Fast-forward |
| 2 | `feature/total-v1` | `develop` | Fast-forward |
| 3 | `feature/total-v2` | `develop` | ⚠️ С конфликтом |
| 4 | `feature/search-advanced` | `develop` | Fast-forward |
| 5 | `develop` | `main` | Fast-forward (синхронизация перед hotfix) |
| 6 | `hotfix/cart-total` | `main` | Fast-forward |
| 7 | `hotfix/cart-total` | `develop` | Fast-forward |

### Был ли конфликт и как он разрешён?

**Да**, конфликт возник при слиянии `feature/total-v2` в `develop` — обе ветки (`total-v1` и `total-v2`) изменяли функцию `total_sum` в одном и том же месте `shop.py`.

**Причина:** разные версии одной функции в одном участке файла.

**Разрешение:** вручную выбран вариант из `total-v2` (с учётом количества), маркеры конфликта удалены, слияние завершено коммитом `646e10f` «Разрешён конфликт в total_sum».

Подробнее — в `docs/09_Conflict_Resolution.md`.

### Вывод

История проекта демонстрирует полный цикл Git Flow:

- Разработка велась в feature-ветках и сливалась в `develop`.
- Один конфликт был намеренно создан и разрешён вручную.
- Hotfix от `main` исправил критическую ошибку и попал в обе ветки.
- Все коммиты имеют осмысленные сообщения с ID задач (US-1, US-2, US-4, US-7).