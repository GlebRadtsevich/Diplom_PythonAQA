import os
import pytest
from playwright.sync_api import sync_playwright
# from data import CustomerDB


@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as playwright:
        headless = os.getenv("HEADLESS", "false").lower() == "true"
        browser = playwright.chromium.launch(headless=headless, args=[
            "--no-sandbox",
            "--disable-dev-shm-usage",
            "--disable-gpu"
        ])
        yield browser
        browser.close()

@pytest.fixture(scope="function")
def page(browser):
    context = browser.new_context()
    page = context.new_page()
    page.set_default_timeout(5000)
    yield page
    context.close()

# @pytest.fixture(autouse=True, scope="function")
# def customer_db():
#     customer_db = CustomerDB()
#     customer_data = customer_db.get_customer_from_db()
#     yield customer_data
#     customer_db.close()
