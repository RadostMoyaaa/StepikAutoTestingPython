import pytest
from selenium import webdriver

# Встроенная функция добавления опции по выбору браузера через опции командной строки
def pytest_addoption(parser):
	parser.addoption('--browser_name', action='store', default='None', 
		help='Choose browser --browser_name:browser, browser - chrome or firefox')
	# --browser_name - имя опции
	# default - значение по умолчанию
	# help - опция помощи по команде

@pytest.fixture(scope="function")
def browser(request):
	# считываем значение опции browser_name с помощью встроенной фикстуры request
	browser_name = request.config.getoption("browser_name")
	if browser_name == "chrome":  # по опции Chrome
		print('Starting chrome...')
		browser = webdriver.Chrome()
	elif browser_name == "firefox": # по опции Firefox
		print('Starting Firefox...')
		browser = webdriver.Firefox()
	else:  # По умолчанию вызываем ошибку, поясняем ввод опции
		raise pytest.UsageError("--browser_name should be chrome or firefox")
	yield browser
	print('Quit...')
	browser.quit()
