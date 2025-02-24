import allure
import pytest
from pages.home_page import HomePage
from data.test_data import products


@allure.epic("Тесты для Home Page")
@pytest.mark.functional
class TestHomePage:

    @allure.title("Test: Проверка открытия главной страницы")
    def test_open_home_page(self, page):
        home_page = HomePage(page)
        home_page.open_home_page()
        home_page.assert_home_page_is_opened()

    @allure.title("Test: Проверка отображения блока Recent Reviews")
    def test_recent_reviews_displayed(self, page):
        home_page = HomePage(page)
        home_page.open_home_page()
        home_page.assert_recent_reviews_displayed()

    @allure.title("Test: Проверка перехода на страницу Shop через кнопку 'See our pricing'")
    def test_see_our_pricing_redirects_to_shop(self, page):
        home_page = HomePage(page)
        home_page.open_home_page()
        home_page.click_see_our_pricing()
        home_page.assert_see_our_pricing()

    @allure.title("Test: Поиск продукта по части названия и проверка результатов")
    @pytest.mark.parametrize("product", products[:2])
    def test_search_and_filter_product(self, page, product):
        home_page = HomePage(page)
        home_page.open_home_page()
        query = product["title"][:5]
        home_page.search_and_filter(query)
        search_result_title = page.locator(f'text="{product["title"]}"')
        search_result_title.wait_for(state="visible", timeout=5000)
        assert search_result_title.is_visible(), f'Product title "{product["title"]}" not found in search results'
        search_result_price = page.locator(f'text="{product["price"]}"')
        search_result_price.wait_for(state="visible", timeout=5000)
        assert search_result_price.is_visible(), f'Product price "{product["price"]}" not found in search results'
        search_result_link = page.locator(f'a[href*="{product["path"]}"]')
        search_result_link.wait_for(state="visible", timeout=5000)
        assert search_result_link.is_visible(), (f'Product link containing "{product["path"]}"'
                                                 f' not found in search results')

    @allure.title("Test: Проверка отображения хедера и футера на главной странице")
    def test_header_and_footer_visible(self, page):
        home_page = HomePage(page)
        home_page.open_home_page()
        home_page.header.assert_header_visible()
        home_page.header.assert_logo_visible()
        home_page.footer.assert_footer_visible()