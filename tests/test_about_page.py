import allure
import pytest
from pages.about_page import AboutPage


@allure.epic("Тесты для страницы About Us")
@pytest.mark.ui
class TestAboutPage:

    @allure.title("Test: Открытие страницы 'About Us'")
    def test_open_about_page(self, page):
        about_page = AboutPage(page)
        about_page.open_about_page()
        about_page.assert_about_us_banner()

    @allure.title("Test: Проверка видимости раздела 'Welcome'")
    def test_welcome_section_visible(self, page):
        about_page = AboutPage(page)
        about_page.open_about_page()
        about_page.assert_welcome_section()

    @allure.title("Test: Проверка видимости раздела 'Why Us'")
    def test_why_us_section_visible(self, page):
        about_page = AboutPage(page)
        about_page.open_about_page()
        about_page.assert_why_us_section()

    @allure.title("Test: Клик по кнопке 'Contact Us'")
    def test_click_contact_us_button(self, page):
        about_page = AboutPage(page)
        about_page.open_about_page()
        about_page.click_contact_us()
        assert "contact" in page.url, f"Ожидалось открытие контактной страницы, но текущий URL: {page.url}"

    @allure.title("Test: Клик по кнопке 'Shop Now'")
    def test_click_shop_now_button(self, page):
        about_page = AboutPage(page)
        about_page.open_about_page()
        about_page.click_shop_now()
        assert "shop" in page.url, f"Ожидалось открытие страницы магазина, но текущий URL: {page.url}"
