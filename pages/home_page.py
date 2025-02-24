import allure
from playwright.sync_api import Page

from core.base import BasePage
from data import DOMAIN, TITLE


class HomePage(BasePage):
    BANNER = '[class="overflow-content bb-banner-padding content-v-center"]'
    BANNER_TITLE = '#bb-section-D323FA94-CE32-5DC6-E626-7D075193B984 > div > div > div.aspect-ratio-inner > div:nth-child(2) > div > div > div > div > div > h2'
    BANNER_NAME = "Make Cases Great Again"
    FEATURED_SECTION = "#bb-section-512921E5-B3EE-81BE-E747-F1A82516138D"
    FEATURED_SECTION_TITLE = '//*[@class="bb-font-h2"]'
    RECENT_REVIEWS = '[class="bb-section bb-section-layout-2 bb-color-0"]'
    RECENT_REVIEWS_TITLE = '[class=" bb-font-h3"]'
    RECENT_REVIEWS_NAME = "RECENT REVIEWS"
    REVIEWS = ".col-12.col-md-6"
    SEARCH_AND_FILTER_BUTTON = '[class="form-control bb-border-color filter-btn"]'
    SEE_OUR_PRICING_BUTTON = '[class="btn  btn-primary"]'
    SEARCH_INPUT = 'body > div.products-filter-panel.show > div.panel.bb-color-0 > div.p-4 > div.panel-filter > div > div:nth-child(1) > div > input'
    APPLY_BUTTON = '[class="btn btn-primary apply-filter"]'


    def __init__(self, page: Page):
        super().__init__(page)
        self.url = f"{DOMAIN}/"
        self.title = TITLE

    @allure.step('Open "Home" page')
    def open_home_page(self):
        self.page.goto(self.url, timeout=10000)

    @allure.step('Assert "Home" page is opened')
    def assert_home_page_is_opened(self):
        assert self.page.locator(self.BANNER).is_visible(), "Banner not visible!"
        assert self.page.locator(
            self.BANNER_TITLE).inner_text() == self.BANNER_NAME, \
                f"Expected banner text '{self.BANNER_NAME}', but got different text."

    @allure.step('Assert that "Recent Reviews" block is displayed with correct text')
    def assert_recent_reviews_displayed(self):
        # Проверяем, что блок Recent Reviews видим на странице
        reviews_block = self.page.locator(self.RECENT_REVIEWS)
        assert reviews_block.is_visible(), "Блок 'Recent Reviews' не отображается"

        # Проверяем, что в блоке отображается надпись "RECENT REVIEWS"
        reviews_title = self.page.locator(self.RECENT_REVIEWS_TITLE)
        reviews_title.wait_for(timeout=10000)
        actual_text = reviews_title.inner_text().strip()
        assert actual_text == self.RECENT_REVIEWS_NAME, \
            f"Ожидаемый текст '{self.RECENT_REVIEWS_NAME}', но получен '{actual_text}'"

    @allure.step('Click on "See our pricing" button')
    def click_see_our_pricing(self):
        pricing_button = self.page.locator(self.SEE_OUR_PRICING_BUTTON)
        pricing_button.wait_for(state="visible", timeout=10000)  # Ждем появления кнопки
        pricing_button.click()

    @allure.step('Проверка открытия страницы "Shop" после нажатия кнопки "See our pricing"')
    def assert_see_our_pricing(self):
        self.page.wait_for_load_state("networkidle")
        current_url = self.page.url
        assert "shop" in current_url, f"Shop page did not open as expected. Current URL: {current_url}"

    @allure.step('Search and filter products with query: {query}')
    def search_and_filter(self, query):
        # Нажимаем на кнопку "Search and Filter"
        search_and_filter_btn = self.page.locator(self.SEARCH_AND_FILTER_BUTTON)
        search_and_filter_btn.wait_for(state="visible", timeout=10000)
        search_and_filter_btn.click()

        # Явное ожидание поля поиска
        search_input = self.page.locator(self.SEARCH_INPUT)
        search_input.wait_for(state="attached", timeout=10000)  # Ждем, пока элемент появится в DOM
        search_input.wait_for(state="visible", timeout=10000)  # Ждем, пока элемент станет видимым

        # Вводим текст в поле поиска
        search_input.fill(query)

        # Нажимаем кнопку "Apply"
        filter_button = self.page.locator(self.APPLY_BUTTON)
        filter_button.wait_for(state="visible", timeout=10000)
        filter_button.click()

        # Дожидаемся появления результатов поиска
        self.page.wait_for_selector(".search-results", timeout=10000)