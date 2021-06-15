from selenium import webdriver
import pytest
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--language', default='ru')


@pytest.fixture(scope='function')
def config(request):
    language = request.config.getoption("--language")
    url = 'http://selenium1py.pythonanywhere.com/{}/catalogue/coders-at-work_207/'.format(language)
    return {'url': url}


@pytest.fixture(scope="function")
def browser(request):  # Фикстура драйвера
    manager = ChromeDriverManager(version='latest')  # Инициализируем менеджер загрузки драйвера chrome
    browser = webdriver.Chrome(executable_path=manager.install())
    yield browser
    browser.close()

