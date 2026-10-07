# Git Flow в проекте «СпортТовары»

## Схема ветвления

```
main ─────────●───────────────●──────────────●───────
              │               │              │
              │           hotfix/*      release/*
              │               │              │
develop ──●───┴───●───────●───┴──●───────●───┴───●───
          │       │       │      │       │       │
       feature/ feature/ feature/ ...   feature/ ...
       low-stock total-v1 search-advanced
```

## Основные ветки

| Ветка | Назначение | Кто пушит | Стабильность |
|-------|-----------|-----------|--------------|
| `main` | Стабильная версия продукта. Только проверенный код | Тимлид через PR | Всегда рабочая |
| `develop` | Интеграция новых функций | Разработчики | Может быть нестабильной |
| `feature/<название>` | Разработка отдельной функции | Один разработчик | Черновик |
| `hotfix/<название>` | Срочное исправление ошибки в main | Дежурный | Минимальные правки |

## Правила работы

1. **Никогда не коммитим напрямую в `main`** — только через слияние из `develop` или `hotfix`.
2. **Feature-ветки создаются от `develop`** и вливаются обратно в `develop`.
3. **Hotfix-ветки создаются от `main`** и вливаются в `main` + `develop`.
4. **Имя ветки:** `feature/<краткое-название>` в kebab-case (например, `feature/low-stock`).
5. **После слияния feature-ветка удаляется** — `git branch -d feature/...`.

## Команды

```bash
# Создать feature-ветку
git checkout develop
git checkout -b feature/low-stock

# После работы — слияние
git checkout develop
git merge feature/low-stock
git branch -d feature/low-stock
git push
```

## Схема для нашего спринта

- `feature/low-stock` — US-1, товары с низким остатком
- `feature/total-v1` / `feature/total-v2` — демонстрация конфликта
- `feature/search-advanced` — US-2, расширенный поиск
- `hotfix/cart-total` — исправление ошибки в main