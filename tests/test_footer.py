import allure
import pytest
from pages.components.footer import Footer

@pytest.fixture
def footer(page):
    return Footer(page)

@allure.epic("Тесты для Footer")
@pytest.mark.ui
class TestFooter:

    @allure.title("Test: Проверка отображения футера")
    def test_footer(self, footer: Footer):
        footer.assert_footer_visible()
        footer.assert_logo_visible()
        footer.assert_address()
        footer.assert_email()
        footer.assert_message()