import allure
from playwright.sync_api import Page
from core.base import BasePage
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
    PRODUCT_CARD = '[class="store-products"]'
    PRODUCT_NAME = '.bb-font-h3'
    PRODUCT_PRICE = '.bb-product-final-price'
    FIRST_PRODUCT = '//*[@id="store-products-13799318"]//a'
    FEATURED_CHECKBOX = "#related-13799318-FFFFFFFF-FFFF-FFFF-FFFF-FFFFFFFFFFFF"
    ON_SALE_CHECKBOX = "#onSale-13799318"
    IN_STOCK_CHECKBOX = "#inStock-13799318"
    METALLIC_CHECKBOX = "#related-13799318-49555A5D-B5C5-90FD-A8F2-79C8F13293F1"
    WITH_MAGSAFE_CHECKBOX = "#related-13799318-63964004-E7A2-3A5F-3DDA-D599D4021CB9"
    SILICONE_CHECKBOX = "#related-13799318-73C7904F-E977-A380-9778-D53C11483404"
    IFRAME_SELECTOR = '[src="/shop/product/untitled-product-2?productQuickView=1"]'
    MODAL_ADD_TO_CART_BUTTON = ".btn btn-primary bb-store-add-product ml-0"
    QUANTITY_SELECTOR = '[name="bb-product-qty"]'

    def __init__(self, page: Page):
        super().__init__(page)
        self.url = f"{DOMAIN}/shop"
        self.title = f"SHOP | {TITLE}"

    @allure.step('Открыть страницу "Shop"')
    def open_shop_page(self):
        self.page.goto(self.url, timeout=10000)

    @allure.step('Проверка видимости заголовка "All Products"')
    def assert_all_products_title_visible(self):
        all_products_title = self.page.locator(self.ALL_PRODUCTS_TITLE)
        all_products_title.wait_for(state="visible", timeout=10000)
        assert all_products_title.is_visible(), "Заголовок 'All Products' не отображается"

    @allure.step('Поиск продукта с названием: {query}')
    def search_product(self, query):
        search_input = self.page.locator(self.SEARCH_FIELD)
        search_input.fill(query)
        search_button = self.page.locator(self.SEARCH_BUTTON)
        search_button.wait_for(state="visible", timeout=5000)
        search_button.click()

    @allure.step('Установить минимальную цену: {min_price} и максимальную цену: {max_price}')
    def filter_by_price(self, min_price, max_price):
        min_price_input = self.page.locator(self.PRICE_MIN_FIELD)
        max_price_input = self.page.locator(self.PRICE_MAX_FIELD)
        min_price_input.fill(str(min_price))
        max_price_input.fill(str(max_price))
        apply_button = self.page.locator(self.SEARCH_BUTTON)
        apply_button.click()

    @allure.step('Проверка отображения продукта: {product}')
    def assert_product_visible(self, product):
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

    @allure.step('Открытие страницы Shop')
    def open_shop_page(self):
        self.page.goto(self.url, timeout=10000)

    @allure.step('Проверка, что страница Shop открыта')
    def assert_shop_page_is_opened(self):
        assert self.page.locator(self.METALLIC_CHECKBOX).is_visible(), "Фильтр Metallic не отображается на странице!"

    @allure.step('Выбор фильтра Metallic')
    def select_metallic_filter(self):
        metallic_checkbox = self.page.locator(self.METALLIC_CHECKBOX)
        metallic_checkbox.click()

    @allure.step('Click on the first product')
    def click_on_first_product(self):
        first_product = self.page.locator("//*[@id='store-products-13799318']//a").nth(0)
        first_product.click()

    @allure.step('Проверка, что страница продукта открыта')
    def assert_product_page_is_opened(self, expected_path):
        current_url = self.page.url
        assert expected_path in current_url, (f"Ожидаемый путь '{DOMAIN}/{expected_path}',"
                                              f" но текущий путь: {current_url}")

    @allure.step('Проверка названия продукта')
    def assert_product_name(self, expected_title):
        product_name = self.page.locator(self.PRODUCT_NAME).inner_text().strip()
        assert product_name == expected_title, (f"Ожидаемое название: '{expected_title}',"
                                                f" но получено: '{product_name}'")

    @allure.step('Проверка цены продукта')
    def assert_product_price(self, expected_price):
        product_price = self.page.locator(self.PRODUCT_PRICE).inner_text().strip()
        assert product_price == expected_price, (f"Ожидаемая цена: '{expected_price}',"
                                                 f" но получена: '{product_price}'")

    # Логика для работы с количеством товара и ценой
    @allure.step('Установка начального количества товара')
    def set_initial_quantity(self, quantity: int):
        quantity_input = self.page.locator(self.QUANTITY_SELECTOR)
        # Ждём, пока элемент станет доступным и видимым
        # Подождем, пока элемент будет видимым
        quantity_input.wait_for(state="visible", timeout=10000)  # Увеличиваем время ожидания до 10 секунд

        try:
            # Пробуем фокусировать элемент и заполнять его значением
            quantity_input.focus()
            quantity_input.fill(str(quantity))
            self.page.locator('body').click()# Вводим начальное количество товара
        except TimeoutError:
            print("Ошибка: элемент не найден или не видим в течение времени ожидания.")
            raise

    @allure.step('Проверка начального значения счётчика товара')
    def assert_initial_quantity(self, expected_quantity: int):
        quantity_locator = self.page.locator(self.QUANTITY_SELECTOR)  # Получаем локатор для поля ввода
        quantity_locator.wait_for(timeout=10000)  # Ждем, пока элемент станет доступным для взаимодействия

        quantity = quantity_locator.input_value()  # Получаем значение из поля
        assert int(quantity) == expected_quantity, (f"Ожидалось количество {expected_quantity},"
                                                    f" но найдено {quantity}")

    @allure.step('Проверка изменения цены')
    def assert_price_changes(self, expected_price: float):
        price = self.page.locator(self.PRODUCT_PRICE).inner_text().strip().replace('$', '')
        assert float(price) == expected_price, (f"Ожидаемая цена {expected_price},"
                                                f" но найдена {price}")
