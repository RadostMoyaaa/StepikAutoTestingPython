import time, math
from selenium import webdriver

link = "http://suninjuly.github.io/math.html"

try:
	# Запускаем драйвер Chrome, открываем страницу
	browser = webdriver.Chrome()
	browser.get(link)

	# Возьмем переменную x
	x = int(browser.find_element_by_id('input_value').text)
	
	# Подсчитаем пример ln(abs(12*sin(x)))
	answer = math.log(abs(12*math.sin(x)))
	
	# Возьмем поле ввода, введем данные
	inp = browser.find_element_by_css_selector('input[required]')
	inp.send_keys(str(answer))

	time.sleep(2)

	# Возьмем checkbox, отметимся
	checkb = browser.find_element_by_id('robotCheckbox')
	checkb.click()

	time.sleep(1)

	# Возьмем radiobutton, отметимся
	radiobut = browser.find_element_by_css_selector('[for="robotsRule"]')
	radiobut.click()

	time.sleep(1)

	# Найдем кнопку submit, нажмем
	btn = browser.find_element_by_css_selector('.btn.btn-default')

	btn.click()


finally:
	print('Done')
	browser.close()

