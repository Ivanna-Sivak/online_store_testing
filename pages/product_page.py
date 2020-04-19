from .base_page import BasePage
from pages.locators import ProductPageLocators


class ProductPage(BasePage):
    def should_be_product_page(self):
        self.should_be_add_to_basket_button()
        self.should_be_search_field()
        self.should_be_login_link()

    def should_be_add_to_basket_button(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET_BUTTON), "Add to basket button is not present"

    def should_be_search_field(self):
        assert self.is_element_present(*ProductPageLocators.SEARCH_FIELD), "Search field is not present"

    def should_be_login_link(self):
        assert self.is_element_present(*ProductPageLocators.LOGIN_LINK), "Login link is not present"

    def add_to_basket(self):
        button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        button.click()

    def find_text_has_been_added_to_basket(self,):
        element = self.browser.find_element(*ProductPageLocators.HAS_BEEN_ADDED_TO_BASKET)
        element_txt = element.text
        assert element_txt == "Coders at Work", "Text has_been_added_to_basket is not found"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.HAS_BEEN_ADDED_TO_BASKET), \
            "Success message is presented, but should not be"

    def success_message_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.HAS_BEEN_ADDED_TO_BASKET), \
            "Success message didn't disappear after adding to basket"

