import allure
import pytest
from pages.contact_page import ContactPage


@allure.epic("Контактная страница Tests")
@pytest.mark.ui
class TestContactPage:

    @allure.title("Test: Открытие страницы 'Contact Us'")
    def test_open_contact_page(self, page):
        """Тест на открытие страницы 'Contact Us'."""
        contact_page = ContactPage(page)
        contact_page.open()
        contact_page.wait_for_page_to_load()
        contact_page.assert_page_is_displayed()

    @allure.title("Test: Проверка наличия элементов на странице 'Contact Us'")
    def test_contact_page_ui_elements(self, page):
        """Тест на проверку наличия элементов на странице 'Contact Us'."""
        contact_page = ContactPage(page)
        contact_page.open()
        contact_page.wait_for_page_to_load()
        contact_page.assert_contact_page_ui()

    @allure.title("Test: Проверка поля 'First Name'")
    def test_first_name_field(self, page):
        """Тест на проверку видимости поля 'First Name' на странице 'Contact Us'."""
        contact_page = ContactPage(page)
        contact_page.open()
        contact_page.wait_for_page_to_load()
        contact_page.assert_element_is_visible(contact_page.FIRST_NAME_FIELD)

    @allure.title("Test: Проверка поля 'Last Name'")
    def test_last_name_field(self, page):
        """Тест на проверку видимости поля 'Last Name' на странице 'Contact Us'."""
        contact_page = ContactPage(page)
        contact_page.open()
        contact_page.wait_for_page_to_load()
        contact_page.assert_element_is_visible(contact_page.LAST_NAME_FIELD)

    @allure.title("Test: Проверка поля 'Email'")
    def test_email_field(self, page):
        """Тест на проверку видимости поля 'Email' на странице 'Contact Us'."""
        contact_page = ContactPage(page)
        contact_page.open()
        contact_page.wait_for_page_to_load()
        contact_page.assert_element_is_visible(contact_page.EMAIL_FIELD)

    @allure.title("Test: Проверка поля 'Message'")
    def test_message_field(self, page):
        """Тест на проверку видимости поля 'Message' на странице 'Contact Us'."""
        contact_page = ContactPage(page)
        contact_page.open()
        contact_page.wait_for_page_to_load()
        contact_page.assert_element_is_visible(contact_page.MESSAGE_FIELD)

    @allure.title("Test: Проверка кнопки отправки на странице 'Contact Us'")
    def test_submit_button(self, page):
        """Тест на проверку видимости кнопки отправки формы на странице 'Contact Us'."""
        contact_page = ContactPage(page)
        contact_page.open()
        contact_page.wait_for_page_to_load()
        contact_page.assert_element_is_visible(contact_page.SUBMIT_BUTTON)
