from pages.base_page import BasePage
from pages.locators import LoginPageLocators


class LoginPage(BasePage):
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert self.is_element_present(*LoginPageLocators.EMAIL_ADDRESS_FIELD_LOGIN)

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.EMAIL_ADDRESS_FIELD_LOGIN), "Login form is not present"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.EMAIL_ADDRESS_FIELD_REGISTER), \
            "Registration form is not present"

    def register_new_user(self, email, password):
        email_adress_field = self.browser.find_element(*LoginPageLocators.EMAIL_ADDRESS_FIELD_REGISTER)
        email_adress_field.send_keys(email)
        password_field = self.browser.find_element(*LoginPageLocators.PASSWORD_FIELD_REGISTER)
        password_field.send_keys(password)
        password_field_confirm = self.browser.find_element(*LoginPageLocators.PASSWORD_FIELD_REGISTER_CONFIRM)
        password_field_confirm.send_keys(password)
        register_button = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)
        register_button.click()