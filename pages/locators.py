from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    EMAIL_ADDRESS_FIELD_LOGIN = (By.ID, "id_login-username")
    EMAIL_ADDRESS_FIELD_REGISTER = (By.ID, "id_registration-email")
    PASSWORD_FIELD_REGISTER = (By.ID, "id_registration-password1")
    PASSWORD_FIELD_REGISTER_CONFIRM = (By.ID, "id_registration-password2")
    REGISTER_BUTTON = (By.CSS_SELECTOR, "[name = 'registration_submit']")


class ProductPageLocators():
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    SEARCH_FIELD = (By.CSS_SELECTOR, "[type=search]")
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    HAS_BEEN_ADDED_TO_BASKET = (By.CSS_SELECTOR, "#messages div:first-child .alertinner strong")


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasketPageLocators():
    BASKET_LINK = (By.CSS_SELECTOR, ".basket-mini span a")
    PROCEED_TO_CHECKOUT_BUTTON = (By.PARTIAL_LINK_TEXT, "checkout/")
    EMPTY_BASKET_TEXT = (By.CSS_SELECTOR, "#content_inner p")



