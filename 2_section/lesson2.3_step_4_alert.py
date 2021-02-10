import math, time
from selenium import webdriver

link = 'http://suninjuly.github.io/alert_accept.html'

try:
	# Открываем браузер, страницу
	browser = webdriver.Chrome()
	browser.get(link)
	
	# Кликаем кнопку
	browser.find_element_by_css_selector(".btn.btn-primary").click()
	
	# Кликаем на confirm
	browser.switch_to.alert.accept()
	
	# Считаем уравние, отправляем ответ
	x = int(browser.find_element_by_id('input_value').text)
	answer = math.log(abs(12*math.sin(x)))
	browser.find_element_by_id('answer').send_keys(str(answer))
	
	# Кликаем кнопку
	browser.find_element_by_css_selector(".btn.btn-primary").click()
finally:
	print('done')