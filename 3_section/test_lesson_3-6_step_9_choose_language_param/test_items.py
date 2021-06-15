import time

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_add_btn(browser, config):
    browser.get(config['url'])
    try:
        btn = WebDriverWait(browser, 5).\
            until(EC.presence_of_element_located((By.XPATH, "//form[@id='add_to_basket_form']//button")))
        exist = True
    except TimeoutException:
        exist = False
    assert exist, f'Button <ADD TO BASKET> is not present'



