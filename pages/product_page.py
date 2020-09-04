from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def should_be_product_page(self):
        self.add_to_basket() #добавления в корзину
        self.should_be_book_price_be_equal() #сравнение цены на страницы c ценой в корзине
        self.should_be_book_name_be_equal() #название на странице и в корзине должно быть одинаковым
        self.should_not_be_success_message()
        self.is_disappeared()

    def add_to_basket(self):
        # реализуйте проверку на корректный url адрес
        assert self.is_element_present(*ProductPageLocators.BUTTON_ADD), "Button is not presented"
        button = self.browser.find_element(*ProductPageLocators.BUTTON_ADD)
        button.click()

    def should_be_book_price_be_equal(self):
        price_book = self.browser.find_element(*ProductPageLocators.PRICE_BOOK).text
        price_message = self.browser.find_element(*ProductPageLocators.PRICE_BOOK_IN_MESSAGE).text
        assert price_book == price_message, "Price is not same"

    def should_be_book_name_be_equal(self):
        name_book = self.browser.find_element(*ProductPageLocators.NAME_BOOK).text
        name_message = self.browser.find_element(*ProductPageLocators.NAME_BOOK_IN_MESSAGE).text
        assert name_book == name_message, "Name is not same"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_not_is_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"


