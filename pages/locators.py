from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_INPUT = (By.CSS_SELECTOR, "button.login_submit")
    LOGIN_REGISTRATION = (By.CSS_SELECTOR, "button.registration_submit")
