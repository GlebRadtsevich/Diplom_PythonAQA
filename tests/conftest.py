import os
import pytest
from playwright.sync_api import sync_playwright
# from data import CustomerDB


# Фикстура для запуска браузера Playwright
@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as playwright:
        # Определяем режим запуска (headless или нет)
        headless = os.getenv("HEADLESS", "false").lower() == "true"

        # Запускаем браузер Chromium с заданными параметрами
        browser = playwright.chromium.launch(headless=headless, args=[
            "--no-sandbox",
            "--disable-dev-shm-usage",
            "--disable-gpu"
        ])

        yield browser  # Передаем браузер в тесты
        browser.close()


# Фикстура для создания новой страницы в браузере для каждого теста
@pytest.fixture(scope="function")
def page(browser):
    context = browser.new_context()  # Создаем новый контекст для изоляции данных между тестами
    page = context.new_page()  # Открываем новую вкладку
    page.set_default_timeout(5000)  # Устанавливаем таймаут по умолчанию (5 секунд)

    yield page  # Передаем объект страницы в тесты

    context.close()  # Закрываем контекст после выполнения теста


# # Фикстура для работы с базой данных клиентов
# @pytest.fixture(autouse=True, scope="function")
# def customer_db():
#     customer_db = CustomerDB()  # Подключаемся к базе данных
#     customer_data = customer_db.get_customer_from_db()  # Получаем данные клиента
#
#     yield customer_data  # Передаем данные в тесты
#
#     customer_db.close()  # Закрываем соединение с базой данных
