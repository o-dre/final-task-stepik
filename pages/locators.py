from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_URL = (By.CSS_SELECTOR, "#login_link")
    LOGIN_INPUT = (By.CSS_SELECTOR, "#login_form")
    LOGIN_REGISTRATION = (By.CSS_SELECTOR, "#register_form")
