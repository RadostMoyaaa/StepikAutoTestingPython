import pytest
from selenium import webdriver


link = "http://selenium1py.pythonanywhere.com/"

@pytest.fixture
def browser():
    print('\n I am starting browser for test')
    return webdriver.Chrome()

class TestMainPage1:
    # Вызываем фикстуру в тесте, передав её как параметр
    def test_guest_should_see_login_linK(self, browser):
        browser.get(link)
        browser.find_element_by_css_selector("#login_link")


    def test_guest_should_see_basket_link_on_the_main_page(self, browser):
        browser.get(link)
        browser.find_element_by_css_selector(".basket-mini .btn-group > a")



