"""Скрипт локальной сборки проекта SportShop."""
import os
import subprocess
import sys


def check_python_version():
    """Проверка версии Python."""
    if sys.version_info < (3, 10):
        print("Ошибка: требуется Python 3.10+")
        sys.exit(1)
    print(f"Python {sys.version_info.major}.{sys.version_info.minor} — OK")


def check_data():
    """Проверка наличия файла данных."""
    if not os.path.exists("data/products.json"):
        print("Ошибка: не найден data/products.json")
        sys.exit(1)
    print("data/products.json — OK")


def run_tests():
    """Запуск всех тестов."""
    result = subprocess.run(
        [sys.executable, "-m", "unittest", "discover", "-s", "tests", "-v"],
        capture_output=True, text=True,
    )
    print(result.stdout)
    if result.stderr:
        print(result.stderr)
    if result.returncode != 0:
        print("Ошибка: тесты не прошли!")
        sys.exit(1)
    print("Тесты — OK")


def run_app():
    """Запуск приложения."""
    subprocess.run([sys.executable, "main.py"])


if __name__ == "__main__":
    print("=== Сборка SportShop ===")
    check_python_version()
    check_data()
    run_tests()
    print("\nСборка успешна!")
    answer = input("Запустить приложение? (y/n): ").strip().lower()
    if answer == "y":
        run_app()
