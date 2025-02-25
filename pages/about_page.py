import allure
from playwright.sync_api import Page
from core.base import BasePage
from data import DOMAIN, TITLE


class AboutPage(BasePage):
    ABOUT_US_BANNER = "#bb-section-60F4A7BE-4C8D-470A-8374-C7E269E614CB"
    CONTACT_US = '[class="btn  btn-primary"]'
    SHOP_NOW = '[class="btn  btn-secondary"]'
    WELCOME_SECTION = '//*[@id="bb-section-60F4A7BE-4C8D-470A-8374-C7E269E614CB"]'
    WHY_US_SECTION = "#bb-section-71D5E765-AB5D-450C-B1F2-00C8EA490010"

    def __init__(self, page: Page):
        super().__init__(page)
        self.url = f"{DOMAIN}/about"
        self.title = f"ABOUT | {TITLE}"

    @allure.step('Open "About Us" page')
    def open_about_page(self):
        self.page.goto(self.url, timeout=10000)

    @allure.step('Assert "About Us" banner is visible')
    def assert_about_us_banner(self):
        assert self.page.locator(
            self.ABOUT_US_BANNER).is_visible(), "Banner 'About Us' is not visible"

    @allure.step('Click on "Contact Us" button')
    def click_contact_us(self):
        contact_button = self.page.locator(self.CONTACT_US)
        contact_button.wait_for(state="visible", timeout=5000)
        contact_button.click()

    @allure.step('Click on "Shop Now" button')
    def click_shop_now(self):
        shop_button = self.page.locator(self.SHOP_NOW)
        shop_button.wait_for(state="visible", timeout=5000)
        shop_button.click()

    @allure.step('Assert "Welcome" section is visible')
    def assert_welcome_section(self):
        assert self.page.locator(
            self.WELCOME_SECTION).is_visible(), "Welcome section is not visible"

    @allure.step('Assert "Why Us" section is visible')
    def assert_why_us_section(self):
        assert self.page.locator(self.WHY_US_SECTION)
