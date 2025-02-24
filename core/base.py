from playwright.sync_api import Page, Locator
from pages.components.header import Header
from pages.components.footer import Footer

class BasePage:

    def __init__(self, page: Page):
        self.page: Page = page
        self.header = Header(page)
        self.footer = Footer(page)

    def wait_for_element(self, selector):
        element = self.page.locator(selector)
        element.wait_for(state="visible", timeout=10000)
        return element

    def wait_for_elements(self, selector):
        elements = self.page.locator(selector)
        elements.wait_for(state="attached", timeout=10000)
        return elements

    def click(self, selector: str):
        self.page.click(selector)

    def fill(self, selector: str, text: str):
        self.page.fill(selector, text)

    def is_visible(self, selector: str, timeout: int = 5000) -> bool:
        element = self.page.locator(selector)
        try:
            element.wait_for(state="visible", timeout=timeout)
            return True
        except Exception as e:
            error_message = str(e)
            if "Timeout" in error_message:
                raise TimeoutError(f"Элемент с селектором '{selector}' не стал видимым за {timeout} мс.")
            else:
                raise RuntimeError(f"Ошибка Playwright при проверке видимости элемента '{selector}': {error_message}")

    def get_text(self, selector: str) -> str:
        return self.page.inner_text(selector)

    def hover(self, selector: str):
        self.page.hover(selector)

    def scroll_to(self, selector: str):
        element = self.page.locator(selector)
        element.scroll_into_view_if_needed()

    def get_locator(self, selector: str) -> Locator:
        return self.page.locator(selector)
