import allure
from pages.checkout_page import CheckoutPage
from pages.shop_page import ShopPage


@allure.epic("Тест формы оплаты")
class TestCheckout:

    @allure.title("Test: Форма оплаты с заполнение данных из DB")
    def test_place_order(self, page, customers_db):
        shop_page = ShopPage(page)
        shop_page.open_shop_page()
        shop_page.select_metallic_filter()
        shop_page.click_on_first_product()
        shop_page.add_to_cart()
        shop_page.checkout()
        checkout_page = CheckoutPage(page, customers_db)
        checkout_page.assert_checkout_page_is_opened()
        checkout_page.wait_for_checkout_page_to_load()
        checkout_page.fill_checkout_form()
        checkout_page.click_continue()
        checkout_page.click_continue()
        checkout_page.submit_order()
        checkout_page.assert_order_successful()
        checkout_page.continue_shopping()
