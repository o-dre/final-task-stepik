from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_login_page(self):
        self.should_be_message_is_empty_basket()
        self.should_be_is_empty_basket()

    def should_be_message_is_empty_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.EMPATY_BASKET), "Products in the shopping cart"

    def should_be_is_empty_basket(self):
        assert self.is_element_present(*BasketPageLocators.EMPATY_BASKET_MESSAGE), "Basket in not empty"
