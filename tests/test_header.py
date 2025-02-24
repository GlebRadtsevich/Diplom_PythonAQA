import allure

from pages.components.header import Header


@allure.epic("Тесты для Header")
class TestHeader:

    @allure.title("Test: Проверка отображения хедера")
    def test_header_is_visible(self, page):
        header = Header(page)
        header.assert_header_visible()

    @allure.title("Test: Проверка отображения логотипа в хедере")
    def test_logo_is_visible(self, page):
        header = Header(page)
        header.assert_logo_visible()

    @allure.title("Test: Проверка наличия ссылки Shop в хедере")
    def test_shop_link(self, page):
        header = Header(page)
        header.assert_shop_link()

    @allure.title("Test: Проверка наличия ссылки Contact в хедере")
    def test_contact_link(self, page):
        header = Header(page)
        header.assert_contact_link()

    @allure.title("Test: Проверка наличия ссылки About в хедере")
    def test_about_link(self, page):
        header = Header(page)
        header.assert_about_link()

    @allure.title("Test: Проверка наличия ссылки FAQ в хедере")
    def test_faq_link(self, page):
        header = Header(page)
        header.assert_faq_link()

    @allure.title("Test: Проверка отображения иконки корзины")
    def test_cart_icon_is_visible(self, page):
        header = Header(page)
        header.assert_cart_icon()

    @allure.title("Test: Проверка закрытия sidebar корзины")
    def test_cart_sidebar(self, page):
        header = Header(page)
        header.assert_cart_icon()
        header.open_cart_sidebar()
        header.close_cart_sidebar()

