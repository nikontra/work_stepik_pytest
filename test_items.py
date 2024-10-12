import time

from selenium.webdriver.common.by import By


LINK = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'

def test_page_contains_an_add_to_cart_button(browser):
    browser.get(LINK)
    time.sleep(5)
    basket = browser.find_element(By.CSS_SELECTOR, 'button.btn.btn-add-to-basket')
    assert basket.is_displayed() is True
