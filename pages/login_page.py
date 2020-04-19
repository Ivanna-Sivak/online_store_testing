from pages.base_page import BasePage
from pages.locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self, browser):
        assert "login" in browser.current_url, "It's not a login url"
        assert self.is_element_present(*LoginPageLocators.EMAIL_ADDRESS_FIELD_LOGIN)

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.EMAIL_ADDRESS_FIELD_LOGIN), "Login form is not present"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.EMAIL_ADDRESS_FIELD_REGISTER), \
            "Registration form is not present"
