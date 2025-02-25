import allure
from pages.faq_page import FAQPage


@allure.epic("Тесты для страницы FAQ")
class TestFAQPage:

    @allure.title("Test: Проверка всех видимых разделов на странице FAQ")
    def test_all_sections_visible(self, page):
        faq_page = FAQPage(page)
        faq_page.open_faq_page()
        faq_page.assert_faq_banner_visible()
        faq_page.assert_general_section_visible()
