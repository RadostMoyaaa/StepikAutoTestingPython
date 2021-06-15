from selenium import webdriver
import pytest
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--language', default='ru')


@pytest.fixture(scope="function")
def browser(request):  # Фикстура драйвера
    user_language = request.config.getoption("--language")
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    manager = ChromeDriverManager(version='latest')  # Инициализируем менеджер загрузки драйвера chrome
    browser = webdriver.Chrome(executable_path=manager.install(), options=options)
    yield browser
    browser.close()

