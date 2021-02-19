import pytest
from selenium import webdriver
import time
import math
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Фикстура для setup и teardown
@pytest.fixture
def browser():
	print('Start browser...')
	browser = webdriver.Chrome()
	browser.implicitly_wait(5)
	yield browser
	print('Quit browser...')
	browser.quit()

# Параметризация 
@pytest.mark.parametrize('number', [str(x) for x in range(236895, 236906) if x not in (236900, 236901, 236902)])
def test_answer(browser, number):
	
	answer = math.log(int(time.time()))
	# Открываем бразуер
	link = f'https://stepik.org/lesson/{number}/step/1'
	browser.get(link)
	
	# Ищем поле, отправляем данные
	textarea = WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.TAG_NAME, 'textarea')))
	textarea.send_keys(str(answer))

	# Ищем кнопку, кликаем
	button = WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.CLASS_NAME, 'submit-submission')))
	button.click()

	# Ищем поле с сообщением
	message = browser.find_element_by_css_selector('pre.smart-hints__hint').text
	
	assert message == 'Correct!', f'Message is not correct message {message}, link {link}'
	
