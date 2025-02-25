import allure
from playwright.sync_api import Page
from data import DOMAIN, TITLE


class ContactPage:
    CONTACT_US_BANNER = "#bb-section-D323FE37-F93E-D1BB-E7C9-A1A9C4F745CA"
    CONTACT_US_SECTION = "#bb-section-D323FE38-B2DF-9D49-BB86-C714ED5E5325"
    FIND_US_SECTION = "#bb-section-D323FE39-C02B-4D75-AE07-00B87B95E4BB"
    FIRST_NAME_FIELD = '//*[@name="First Name"]'
    LAST_NAME_FIELD = '//*[@name="Last Name"]'
    EMAIL_FIELD = '//*[@name="Email"]'
    MESSAGE_FIELD = '//*[@name="Message"]'
    SUBMIT_BUTTON = 'button[type="submit"].btn.btn-primary'

    def __init__(self, page: Page):
        self.page = page
        self.url = f"{DOMAIN}/contact"
        self.title = f"Contact | {TITLE}"

    @allure.step("Открытие страницы CONTACT")
    def open(self):
        self.page.goto(self.url, timeout=10000)

    @allure.step('Ожидание полной загрузки страницы')
    def wait_for_page_to_load(self):
        """Ожидает, пока страница полностью загрузится."""
        self.page.wait_for_load_state("load")
        self.page.wait_for_selector(self.CONTACT_US_BANNER)

    @allure.step('Проверка, что страница "CONTACT" открыта')
    def assert_page_is_displayed(self):
        assert self.page.title() == self.title, f"Ожидаемый title: {
            self.title}, но найден {
            self.page.title()}"
        assert self.page.url == self.url, f"Ожидаемый URL: {
            self.url}, но найден {
            self.page.url}"
        self.assert_element_is_visible(self.CONTACT_US_BANNER)
        self.assert_banner_title("Contact Us ")

    @allure.step('Проверка наличия элементов на странице "CONTACT"')
    def assert_contact_page_ui(self):
        self.assert_page_is_displayed()
        self.assert_element_is_visible(self.CONTACT_US_SECTION)
        self.assert_element_is_visible(self.FIND_US_SECTION)
        self.assert_element_is_visible(self.FIRST_NAME_FIELD)
        self.assert_element_is_visible(self.LAST_NAME_FIELD)
        self.assert_element_is_visible(self.EMAIL_FIELD)
        self.assert_element_is_visible(self.SUBMIT_BUTTON)
        self.assert_element_is_visible(self.MESSAGE_FIELD)

    @allure.step('Проверка видимости элемента')
    def assert_element_is_visible(self, selector: str):
        element = self.page.locator(selector)
        assert element.is_visible(
        ), f"Элемент с селектором {selector} не виден на странице"

    @allure.step('Проверка заголовка баннера')
    def assert_banner_title(self, expected_title: str):
        banner_title = self.page.locator(
            self.CONTACT_US_BANNER).inner_text().strip()
        expected_title = expected_title.strip()
        assert banner_title == expected_title, f"Ожидаемый текст баннера: '{expected_title}', но найден: '{banner_title}'"
