from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_URL = (By.CSS_SELECTOR, "#login_link")
    LOGIN_INPUT = (By.CSS_SELECTOR, "#login_form")
    LOGIN_REGISTRATION = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators():
    BUTTON_ADD = (By.CSS_SELECTOR, ".btn-add-to-basket")
    NAME_BOOK = (By.CSS_SELECTOR, ".product_main h1")
    PRICE_BOOK = (By.CSS_SELECTOR, "p.price_color")
    NAME_BOOK_IN_MESSAGE = (By.CSS_SELECTOR, "#messages>div:nth-child(1) strong")
    PRICE_BOOK_IN_MESSAGE = (By.CSS_SELECTOR, "#messages>div:nth-child(3) strong")
