from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

url = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_button_exists(browser):
    browser.get(url)

    try:
        btn_add_to_basket = browser.find_element(By.CLASS_NAME, "btn-add-to-basket")
        assert btn_add_to_basket.is_displayed(), "Кнопка найдена, но не видима на экране"
    except NoSuchElementException:
        assert False, "Кнопка не найдена на странице"