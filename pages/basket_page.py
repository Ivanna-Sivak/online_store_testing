from .base_page import BasePage
from pages.locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_basket_page(self):
        self.should_be_no_goods_in_basket()
        self.should_be_empty_basket_text()

    def should_be_no_goods_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.PROCEED_TO_CHECKOUT_BUTTON), "There are goods in a basket"

    def should_be_empty_basket_text(self):
        empty_basket_element = self.browser.find_element(*BasketPageLocators.EMPTY_BASKET_TEXT)
        assert empty_basket_element.text == "Your basket is empty. Continue shopping",\
            "There is no text 'Your basket is empty'"
