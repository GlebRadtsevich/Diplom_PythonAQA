import allure
from playwright.sync_api import Page


class CheckoutPage:
    EMAIL_FIELD = "#checkout-email"
    FIRST_NAME_FIELD = "#checkout-firstName"
    LAST_NAME_FIELD = "#checkout-lastName"
    ADDRESS_FIELD = "#checkout-addressLine1"
    CITY_FIELD = "#checkout-city"
    COUNTRY_SELECTOR = "#checkout-country"
    STATE_SELECTOR = '[name="state"]'
    PHONE_FIELD = "#checkout-phone"
    CONTINUE_BUTTON = '[class="hp-btn hp-btn-primary checkout-continue"]'
    SUBMIT_BUTTON = '(//*[@id="offline-payment-btn"])[1]'
    THANK_YOU_CARD = '(//*[@class="thank-you-subheader"])[1]'
    CONTINUE_SHOPPING_BUTTON = ".hp-btn-primary"

    def __init__(self, page: Page, customer_data=None):
        self.page = page
        self.url = "https://checkout-msxk87fv.websiteserver4.com/_storeManager.checkout"
        self.title = "AllInOne - Secure Checkout"
        self.customer_data = customer_data

    @allure.step("Открытие страницы Checkout")
    def open_checkout_page(self):
        self.page.goto(self.url, timeout=15000)

    @allure.step("Проверка заголовка страницы Checkout")
    def assert_checkout_page_is_opened(self):
        assert self.page.title() == self.title, f"Ожидался заголовок '{self.title}', но получен '{self.page.title()}'"

    @allure.step("Заполнение формы с данными покупателя")
    def fill_checkout_form(self):
        assert self.customer_data, "Нет данных покупателя для заполнения формы"
        self.page.locator(self.EMAIL_FIELD).fill(self.customer_data["email"])
        self.page.locator(
            self.FIRST_NAME_FIELD).fill(
            self.customer_data["first_name"])
        self.page.locator(
            self.LAST_NAME_FIELD).fill(
            self.customer_data["last_name"])
        self.page.locator(
            self.ADDRESS_FIELD).fill(
            self.customer_data["address"])
        self.page.locator(self.CITY_FIELD).fill(self.customer_data["city"])
        self.page.locator(self.PHONE_FIELD).fill(self.customer_data["phone"])
        self.select_country()
        self.select_state()

    @allure.step("Выбор элемента из выпадающего списка")
    def select_dropdown_option(self, selector: str, value: str):
        dropdown = self.page.locator(selector)
        if dropdown.is_visible() and dropdown.is_enabled():
            dropdown.click()
            dropdown.select_option(label=value)
        else:
            raise Exception(f"Dropdown for state '{value}' is not visible or enabled.")

    @allure.step("Переход к следующему шагу")
    def click_continue(self):
        self.page.locator(self.CONTINUE_BUTTON).click()
        self.page.wait_for_load_state("networkidle")

    @allure.step("Подтверждение заказа")
    def submit_order(self):
        self.page.locator(self.SUBMIT_BUTTON).click()
        self.page.wait_for_load_state("networkidle")

    @allure.step("Проверка успешного оформления заказа")
    def assert_order_successful(self):
        assert self.page.locator(
            self.THANK_YOU_CARD).is_visible(), "Подтверждение заказа не найдено"

    @allure.step("Возвращение в магазин")
    def continue_shopping(self):
        self.page.locator(self.CONTINUE_SHOPPING_BUTTON).click()

    @allure.step("Ожидание полной загрузки страницы Checkout")
    def wait_for_checkout_page_to_load(self):
        self.page.wait_for_load_state("networkidle", timeout=15000)

    @allure.step("Выбор страны")
    def select_country(self):
        country_value = self.customer_data["country"]
        dropdown = self.page.locator(self.COUNTRY_SELECTOR)
        dropdown.click()
        self.page.wait_for_function(f"() => document.querySelectorAll('{self.COUNTRY_SELECTOR} option').length > 1",timeout=15000)
        options = dropdown.locator("option").all_inner_texts()
        print("Available country options:", options)
        if country_value in options:
            dropdown.select_option(label=country_value)
        else:
            raise Exception(f"Country '{country_value}' not found in dropdown options.")

    @allure.step("Выбор штата")
    def select_state(self):
        state_value = self.customer_data["state"]
        dropdown = self.page.locator(self.STATE_SELECTOR)
        self.page.wait_for_function(f"() => document.querySelectorAll('{self.STATE_SELECTOR} option').length > 1",timeout=15000)
        options_values = dropdown.locator("option").evaluate_all("elements => elements.map(el => el.value)")
        if state_value in options_values:
            dropdown.select_option(value=state_value)
        else:
            raise Exception(f"State '{state_value}' is not available in the dropdown options. Available values: {options_values}")
