import allure
from playwright.sync_api import Page
from core.base import BasePage
from data.test_data import products
from data import DOMAIN, TITLE


class ShopPage(BasePage):
    # Локаторы
    ALL_PRODUCTS_TITLE = "h2.bb-font-h2"
    ADD_TO_CART_BUTTON = '[data-itemkey="21467343-E056-BE09-9A53-DBB50EE53C78"]'
    SEARCH_SECTION = "(//*[@class='form-group'])[1]"
    SEARCH_FIELD = 'input[name="search"][type="text"]'
    SEARCH_BUTTON = '[class="append search-btn"]'
    BROWSE_BY_SECTION = "(//*[@class='form-group'])[2]"
    COLLECTIONS_SECTION = "(//*[@class='form-group'])[3]"
    PRICE_SECTION = "(//*[@class='form-group'])[4]"
    SORT_BY_DROPDOWN = '[title="Sort Products"]'
    PRICE_MIN_FIELD = 'input[class*="min-price"]'
    PRICE_MAX_FIELD = 'input[class*="max-price"]'
    PRODUCT_CARD = '[class="store-products"]'  # Локатор для всей карточки товара
    PRODUCT_TITLE = 'div[data-product-id="13799318"] h5'  # Внутри карточки товара
    PRODUCT_PRICE = "#store-products-13799318 .py-3 span span"
    PRODUCT_SECTION = '[class="store-products"]'
    FEATURED_CHECKBOX = "#related-13799318-FFFFFFFF-FFFF-FFFF-FFFF-FFFFFFFFFFFF"
    ON_SALE_CHECKBOX = "#onSale-13799318"
    IN_STOCK_CHECKBOX = "#inStock-13799318"
    METALLIC_CHECKBOX = "#related-13799318-49555A5D-B5C5-90FD-A8F2-79C8F13293F1"
    WITH_MAGSAFE_CHECKBOX = "#related-13799318-63964004-E7A2-3A5F-3DDA-D599D4021CB9"
    SILICONE_CHECKBOX = "#related-13799318-73C7904F-E977-A380-9778-D53C11483404"
    IFRAME_SELECTOR = '[src="/shop/product/untitled-product-2?productQuickView=1"]'  # Модальное окно после нажатия Add to Cart
    MODAL_ADD_TO_CART_BUTTON = ".btn btn-primary bb-store-add-product ml-0"  # Кнопка Add to Cart в модальном окне

    def __init__(self, page: Page):
        super().__init__(page)
        self.url = f"{DOMAIN}/shop"
        self.title = f"SHOP | {TITLE}"

    @allure.step('Открыть страницу "Shop"')
    def open_shop_page(self):
        self.page.goto(self.url, timeout=10000)

    @allure.step('Проверка видимости заголовка "All Products"')
    def assert_all_products_title_visible(self):
        """Проверяет, что заголовок 'All Products' виден."""
        all_products_title = self.page.locator(self.ALL_PRODUCTS_TITLE)
        all_products_title.wait_for(state="visible", timeout=10000)
        assert all_products_title.is_visible(), "Заголовок 'All Products' не отображается"

    @allure.step('Поиск продукта с названием: {query}')
    def search_product(self, query):
        """Выполняет поиск продукта по ключевому слову."""
        search_input = self.page.locator(self.SEARCH_FIELD)
        search_input.fill(query)

        search_button = self.page.locator(self.SEARCH_BUTTON)
        search_button.wait_for(state="visible", timeout=5000)
        search_button.click()

    @allure.step('Установить минимальную цену: {min_price} и максимальную цену: {max_price}')
    def filter_by_price(self, min_price, max_price):
        """Фильтрует товары по цене."""
        min_price_input = self.page.locator(self.PRICE_MIN_FIELD)
        max_price_input = self.page.locator(self.PRICE_MAX_FIELD)

        min_price_input.fill(str(min_price))
        max_price_input.fill(str(max_price))

        # Предположим, что есть кнопка "Применить" фильтр
        apply_button = self.page.locator(self.SEARCH_BUTTON)
        apply_button.click()

    @allure.step('Проверка отображения продукта: {product}')
    def assert_product_visible(self, product):
        """Проверяет, что найден продукт с указанным названием и ценой внутри карточки товара."""

        product_cards = self.page.locator(self.PRODUCT_CARD)
        product_count = product_cards.count()

        found = False
        for i in range(product_count):
            card = product_cards.nth(i)
            card_text = card.inner_text().strip()

            if product["title"] in card_text and product["price"] in card_text:
                found = True
                break

        assert found, (
            f'Продукт с названием "{product["title"]}" и ценой "{product["price"]}" '
            f'не найден на странице.'
        )

    @allure.step('Отметить фильтр: {filter_name}')
    def apply_checkbox_filter(self, filter_name):
        """Устанавливает фильтр через чекбокс."""
        filters = {
            "featured": self.FEATURED_CHECKBOX,
            "on_sale": self.ON_SALE_CHECKBOX,
            "in_stock": self.IN_STOCK_CHECKBOX,
            "metallic": self.METALLIC_CHECKBOX,
            "magsafe": self.WITH_MAGSAFE_CHECKBOX,
            "silicone": self.SILICONE_CHECKBOX
        }

        checkbox_selector = filters.get(filter_name.lower())
        if checkbox_selector:
            checkbox = self.page.locator(checkbox_selector)
            checkbox.check()
        else:
            raise ValueError(f"Фильтр '{filter_name}' не найден")
