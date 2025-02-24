import allure
from playwright.sync_api import Page
from data import DOMAIN

class Footer:
    FOOTER = ".bb-section.bb-section-layout-4.bb-color-1"
    LOGO = "//footer//div[contains(@class, 'bb-site-logo')]//img"
    ADDRESS = ".d-flex.py-1:first-of-type"
    EMAIL = ".d-flex.py-1:last-of-type"
    MESSAGE = "footer .col-12.col-sm-6.py-2 > div"
    address_text = "888 Griffiths Way, Mainland ML 12345"
    email_text = "radtsevich70@gmail.com"
    message_text = ("This site is created for testing purposes "
                    "and can be used only by the site owner")

    def __init__(self, page: Page, url=f"{DOMAIN}/"):
        self.page = page
        self.url = url
        self.open_page()

    @allure.step("Открытие страницы и ожидание полной загрузки")
    def open_page(self):
        self.page.goto(self.url, timeout=30000, wait_until="networkidle")
        self.wait_for_page_load()

    @allure.step("Ожидание полной загрузки страницы")
    def wait_for_page_load(self):
        self.page.wait_for_load_state("networkidle")

    @allure.step("Проверка отображения футера")
    def assert_footer_visible(self):
        assert self.page.locator(self.FOOTER).is_visible(), "Footer не отображается"

    @allure.step("Проверка отображения логотипа в футере")
    def assert_logo_visible(self):
        logo_locator = self.page.locator(self.LOGO)
        logo_locator.wait_for(state="visible", timeout=10000)  # Ждем появления логотипа
        assert logo_locator.is_visible(), "Логотип не отображается"

    @allure.step("Проверка отображения адреса в футере")
    def assert_address(self):
        address = self.page.locator(self.ADDRESS)
        address_text = address.inner_text()
        assert address_text == self.address_text, f"Ожидался текст адреса '{self.address_text}', но найден '{address_text}'"

    @allure.step("Проверка отображения email в футере")
    def assert_email(self):
        email = self.page.locator(self.EMAIL)
        email_text = email.inner_text()
        assert email_text == self.email_text, f"Ожидался текст email '{self.email_text}', но найден '{email_text}'"

    @allure.step("Проверка отображения сообщения в футере")
    def assert_message(self):
        message = self.page.locator(self.MESSAGE)
        message_text = message.inner_text()
        assert message_text == self.message_text, f"Ожидался текст сообщения '{self.message_text}', но найден '{message_text}'"
