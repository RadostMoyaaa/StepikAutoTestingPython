import time, math
from selenium import webdriver


link = 'http://suninjuly.github.io/get_attribute.html'

try:
	# Открываем браузер
	browser = webdriver.Chrome()
	browser.get(link)
	
	# Находим изображение, получаем значение атрибута valuex
	img = browser.find_element_by_id('treasure')
	valuex = int(img.get_attribute('valuex'))

	# Подсчитаем уравнение ln(abs(12*sin(x))
	answer = math.log(abs(12*math.sin(valuex)))

	# Ищем поле, вводим данные
	inp = browser.find_element_by_id('answer')
	inp.send_keys(str(answer))

	# Ищем checkbox, кликаем
	check_box = browser.find_element_by_id('robotCheckbox')
	check_box.click()

	# Ищем radiobutton, кликаем
	radio_btn = browser.find_element_by_id('robotsRule')
	radio_btn.click()

	# Ищем кнопку, кликаем
	btn = browser.find_element_by_css_selector('.btn.btn-default')
	btn.click()
	
finally:
	print('Done')
	time.sleep(3)
	