import pytest
from pages.components.footer import Footer

@pytest.fixture
def footer(page):
    return Footer(page)

def test_footer(footer: Footer):
    footer.assert_footer_visible()
    footer.assert_logo_visible()
    footer.assert_address()
    footer.assert_email()
    footer.assert_message()