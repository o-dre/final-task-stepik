import time


def test_find_add_to_card_btn(browser):
    browser.get('http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/')
    time.sleep(30)
    button = browser.find_element_by_css_selector('button.btn.btn-lg.btn-primary.btn-add-to-basket')
    assert button.is_displayed(), 'Кнопка добавления товара в корзину отсутствует'