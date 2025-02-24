import allure
from playwright.sync_api import Page
from core.base import BasePage
from data import DOMAIN, TITLE


class FAQPage(BasePage):
    # Локаторы
    FAQ_BANNER = "#bb-section-202C54B3-F4CB-4348-968F-494DF1F9DFB1"
    GENERAL_SECTION = "#bb-section-D1AA47D0-DF12-4378-BD62-9D298F2C88E2"

    def __init__(self, page: Page):
        super().__init__(page)
        self.url = f"{DOMAIN}/faq"
        self.title = f"FAQ | {TITLE}"

    @allure.step('Открытие страницы FAQ')
    def open_faq_page(self):
        """Открыть страницу FAQ."""
        self.page.goto(self.url, timeout=10000)

    @allure.step('Проверка видимости баннера FAQ')
    def assert_faq_banner_visible(self):
        """Проверить, что баннер FAQ виден на странице."""
        faq_banner = self.page.locator(self.FAQ_BANNER)
        faq_banner.wait_for(state="visible", timeout=10000)
        assert faq_banner.is_visible(), "FAQ баннер не отображается"

    @allure.step('Проверка видимости раздела General')
    def assert_general_section_visible(self):
        """Проверить, что раздел General виден на странице."""
        general_section = self.page.locator(self.GENERAL_SECTION)
        general_section.wait_for(state="visible", timeout=10000)
        assert general_section.is_visible(), "Раздел General не отображается"
