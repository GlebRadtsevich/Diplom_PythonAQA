import allure
from playwright.sync_api import Page

from core.base import BasePage
from data import DOMAIN, TITLE


class HomePage(BasePage):
    BANNER = '[class="overflow-content bb-banner-padding content-v-center"]'
    BANNER_TITLE = '#bb-section-D323FA94-CE32-5DC6-E626-7D075193B984 .aspect-ratio-inner h2'
    BANNER_NAME = "Make Cases Great Again"
    FEATURED_SECTION = "#bb-section-512921E5-B3EE-81BE-E747-F1A82516138D"
    FEATURED_SECTION_TITLE = '//*[@class="bb-font-h2"]'
    RECENT_REVIEWS = '[class="bb-section bb-section-layout-2 bb-color-0"]'
    RECENT_REVIEWS_TITLE = '[class=" bb-font-h3"]'
    RECENT_REVIEWS_NAME = "RECENT REVIEWS"
    REVIEWS = ".col-12.col-md-6"
    SEARCH_AND_FILTER_BUTTON = '[class="form-control bb-border-color filter-btn"]'
    SEE_OUR_PRICING_BUTTON = '[class="btn  btn-primary"]'
    SEARCH_INPUT = '(//input[@name="search"])[2]'
    APPLY_BUTTON = '[class="btn btn-primary apply-filter"]'

    def __init__(self, page: Page):
        super().__init__(page)
        self.url = f"{DOMAIN}/"
        self.title = TITLE

    @allure.step('Открытие страницы "Home"')
    def open_home_page(self):
        self.page.goto(self.url, timeout=10000)

    @allure.step('Проверка, что страница "Home" открыта')
    def assert_home_page_is_opened(self):
        assert self.page.locator(
            self.BANNER).is_visible(), "Banner not visible!"
        assert self.page.locator(
            self.BANNER_TITLE).inner_text() == self.BANNER_NAME, f"Ожидался текст '{self.BANNER_NAME}'."

    @allure.step('Проверка отображения блока "Recent Reviews" с правильным текстом')
    def assert_recent_reviews_displayed(self):
        reviews_block = self.page.locator(self.RECENT_REVIEWS)
        assert reviews_block.is_visible(), "Блок 'Recent Reviews' не отображается"
        reviews_title = self.page.locator(self.RECENT_REVIEWS_TITLE)
        reviews_title.wait_for(timeout=10000)
        actual_text = reviews_title.inner_text().strip()
        assert actual_text == self.RECENT_REVIEWS_NAME, f"Ожидаемый текст '{
            self.RECENT_REVIEWS_NAME}', но получен '{actual_text}'"

    @allure.step('Клик по кнопке "See our pricing"')
    def click_see_our_pricing(self):
        pricing_button = self.page.locator(self.SEE_OUR_PRICING_BUTTON)
        pricing_button.wait_for(
            state="visible",
            timeout=10000)  # Ждем появления кнопки
        pricing_button.click()

    @allure.step('Проверка открытия страницы "Shop" после нажатия кнопки "See our pricing"')
    def assert_see_our_pricing(self):
        self.page.wait_for_load_state("networkidle")
        current_url = self.page.url
        assert "shop" in current_url, f"Shop page did not open as expected. Current URL: {current_url}"

    @allure.step('Поиск и фильтрация товаров по запросу: {query}')
    def search_and_filter(self, query):
        search_and_filter_btn = self.page.locator(
            self.SEARCH_AND_FILTER_BUTTON)
        search_and_filter_btn.wait_for(state="visible", timeout=10000)
        search_and_filter_btn.click()
        search_input = self.page.locator(self.SEARCH_INPUT)
        search_input.wait_for(state="attached", timeout=10000)
        search_input.wait_for(state="visible", timeout=10000)
        search_input.fill(query)
        filter_button = self.page.locator(self.APPLY_BUTTON)
        filter_button.wait_for(state="visible", timeout=10000)
        filter_button.click()
        self.page.wait_for_selector(".search-results", timeout=10000)
