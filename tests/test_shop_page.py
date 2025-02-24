import allure
import pytest
from pages.shop_page import ShopPage
from data.test_data import products


@allure.epic("Shop Page Tests")
@pytest.mark.ui
class TestShopPage:

    @allure.title("Test: Открытие страницы Shop и проверка заголовка")
    def test_open_shop_page_and_check_title(self, page):
        shop_page = ShopPage(page)
        shop_page.open_shop_page()
        shop_page.assert_all_products_title_visible()

    @allure.title("Test: Поиск продуктов из test_data через карточки товара")
    @pytest.mark.parametrize("product", products)
    def test_search_products(self, page, product):
        shop_page = ShopPage(page)
        shop_page.open_shop_page()
        query = product.get("title", "")[:5]
        shop_page.search_product(query)
        shop_page.assert_product_visible(product)

    @allure.title("Test: Фильтрация товаров по цене")
    def test_filter_products_by_price(self, page):
        shop_page = ShopPage(page)
        shop_page.open_shop_page()
        shop_page.filter_by_price(20, 26)
        filtered_results = page.locator('[class="store-products"]')
        assert filtered_results.count() > 0, "Не найдено товаров в указанном диапазоне цен"

    @allure.title("Test: Применение чекбокса 'Featured'")
    def test_apply_featured_filter(self, page):
        shop_page = ShopPage(page)
        shop_page.open_shop_page()
        shop_page.apply_checkbox_filter("featured")
        featured_results = page.locator('[class="store-products"]')
        assert featured_results.count() > 0, "Не найдено отмеченных как 'Featured' товаров"

    @allure.title("Test: Применение чекбокса 'On Sale'")
    def test_apply_onsale_filter(self, page):
        shop_page = ShopPage(page)
        shop_page.open_shop_page()
        shop_page.apply_checkbox_filter("on_sale")
        on_sale_results = page.locator('[class="store-products"]')
        assert on_sale_results.count() > 0, "Не найдено отмеченных как 'On_sale' товаров"

    @allure.title("Test: Применение чекбокса 'In Stock'")
    def test_apply_instock_filter(self, page):
        shop_page = ShopPage(page)
        shop_page.open_shop_page()
        shop_page.apply_checkbox_filter("in_stock")
        in_stock_results = page.locator('[class="store-products"]')
        assert in_stock_results.count() > 0, "Не найдено отмеченных как 'in_stock' товаров"

    @allure.title("Test: Применение чекбокса 'Metallic'")
    def test_apply_metallic_filter(self, page):
        shop_page = ShopPage(page)
        shop_page.open_shop_page()
        shop_page.apply_checkbox_filter("metallic")
        metallic_results = page.locator('[class="store-products"]')
        assert metallic_results.count() > 0, "Не найдено отмеченных как 'Metallic' товаров"

    @allure.title("Test: Применение чекбокса 'Silicone'")
    def test_apply_silicone_filter(self, page):
        shop_page = ShopPage(page)
        shop_page.open_shop_page()
        shop_page.apply_checkbox_filter("silicone")
        silicone_results = page.locator('[class="store-products"]')
        assert silicone_results.count() > 0, "Не найдено отмеченных как 'Silicone' товаров"

    @allure.title("Test: Применение чекбокса 'MagSafe'")
    def test_apply_magsafe_filter(self, page):
        shop_page = ShopPage(page)
        shop_page.open_shop_page()
        shop_page.apply_checkbox_filter("magsafe")
        magsafe_results = page.locator('[class="store-products"]')
        assert magsafe_results.count() > 0, "Не найдено отмеченных как 'MagSafe' товаров"

