from selenium.webdriver.common.by import By


class MainPageLocators():
    pass

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
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages>div:nth-child(1)")


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    #LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")

class BasketPageLocators():
    BASKET_LINK = (By.CSS_SELECTOR, "a.btn.btn-default")
    EMPATY_BASKET_MESSAGE =(By.CSS_SELECTOR, "#content_inner p")
    EMPATY_BASKET =(By.CSS_SELECTOR, ".basket-items")