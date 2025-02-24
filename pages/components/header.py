import allure
from playwright.sync_api import Page

from data import DOMAIN


class Header:
    HEADER_CONTAINER = '#bb-header'
    LOGO = '#bb-header-spacing .bb-site-logo img'
    SHOP_LINK = '[href="/shop"]'
    CONTACT_LINK = '[href="/contact"]'
    ABOUT_LINK = '[href="/about"]'
    FAQ_LINK = '[href="/faq"]'
    CART_ICON = '[aria-label="Open Cart"]'
    CART_SIDEBAR = '[class="bb-cart-dialog bb-color-0 pb-5 px-3 px-md-0"]'
    CLOSE_CART_BUTTON = 'aria-label="Close Sidebar"'
    CART_ITEM_TITLE = 'class="mb-1 d-block bb-cart-product-name"'


    def __init__(self, page: Page, url=f"{DOMAIN}/"):
        self.page = page
        self.url = url
        self.open_page()  # Открытие страницы с ожиданием загрузки

    @allure.step("Открытие страницы и ожидание полной загрузки")
    def open_page(self):
        self.page.goto(self.url, timeout=30000, wait_until="networkidle")
        self.wait_for_page_load()

    @allure.step("Ожидание полной загрузки страницы")
    def wait_for_page_load(self):
        self.page.wait_for_load_state("networkidle")

    @allure.step("Проверка отображения хедера")
    def assert_header_visible(self):
        assert self.page.locator(self.HEADER_CONTAINER).is_visible(), "Header не отображается"

    @allure.step("Проверка отображения логотипа")
    def assert_logo_visible(self):
        assert self.page.locator(self.LOGO).is_visible(), "Логотип не отображается"

    @allure.step("Проверка наличия ссылки Shop в header")
    def assert_shop_link(self):
        shop_link = self.page.locator(self.SHOP_LINK)
        assert shop_link.count() > 0, "Ссылка Shop не найдена в header"

    @allure.step("Проверка наличия ссылки Contact в header")
    def assert_contact_link(self):
        contact_link = self.page.locator(self.CONTACT_LINK)
        assert contact_link.count() > 0, "Ссылка Contact не найдена в header"

    @allure.step("Проверка наличия ссылки About в header")
    def assert_about_link(self):
        about_link = self.page.locator(self.ABOUT_LINK)
        assert about_link.count() > 0, "Ссылка About не найдена в header"

    @allure.step("Проверка наличия ссылки FAQ в header")
    def assert_faq_link(self):
        faq_link = self.page.locator(self.FAQ_LINK)
        assert faq_link.count() > 0, "Ссылка FAQ не найдена в header"

    @allure.step("Проверка отображения иконки корзины")
    def assert_cart_icon(self):
        cart_icon = self.page.locator(self.CART_ICON)
        assert cart_icon.is_visible(), "Иконка корзины не отображается"

    @allure.step("Открытие sidebar корзины через проверку видимости")
    def open_cart_sidebar(self):
        cart_icon = self.page.locator(self.CART_ICON)
        cart_icon.wait_for(state="visible", timeout=10000)
        cart_icon.click()
        cart_sidebar = self.page.locator(self.CART_SIDEBAR)
        cart_sidebar.wait_for(state="visible", timeout=15000)
        assert cart_sidebar.is_visible(), "Sidebar корзины не открылся"

    @allure.step("Закрытие sidebar корзины через проверку видимости")
    def close_cart_sidebar(self):
        cart_icon = self.page.locator(self.CART_ICON)
        cart_icon.wait_for(state="visible", timeout=10000)
        cart_icon.click(force=True)

    @allure.step("Проверка наличия товара в корзине: {product_title}")
    def assert_product_in_cart(self, product_title):
        cart_item = self.page.locator(f"{self.CART_ITEM_TITLE} >> text={product_title}")
        cart_item.wait_for(state="visible", timeout=10000)
        assert cart_item.is_visible(), f"Товар '{product_title}' не найден в корзине"