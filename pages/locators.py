from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    EMAIL_ADDRESS_FIELD_LOGIN = (By.ID, "id_login-username")
    EMAIL_ADDRESS_FIELD_REGISTER = (By.ID, "id_registration-email")
