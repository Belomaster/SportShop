"""Модуль сохранения и загрузки данных."""
import json


def load_products(filename="data/products.json"):
    """Загружает список товаров из JSON."""
    try:
        with open(filename, "r", encoding="utf-8") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def save_products(products, filename="data/products.json"):
    """Сохраняет товары в JSON."""
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(products, f, ensure_ascii=False, indent=2)
