from .base_page import BasePage
from .locators import BasketPageLockators


class BasketPage(BasePage):
    def basket_empty(self):
        assert self.is_not_element_present(*BasketPageLockators.GET_PURCHASE), "В корзине есть товары"

    def basket_empty_text(self):
        assert self.browser.find_element(*BasketPageLockators.EMPTY_BASKET_TEXT) is not None, "text is not presented"
