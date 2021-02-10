from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select

link = "http://suninjuly.github.io/selects1.html"

try:
	browser = webdriver.Chrome()
	browser.get(link)

	# Ищем числа
	num_1 = int(browser.find_element_by_id('num1').text)
	num_2 = int(browser.find_element_by_id('num2').text)

	# Суммируем
	answer = num_1 + num_2

	# Ищем select
	select = Select(browser.find_element_by_id('dropdown'))

	# Ищем option, который соответствует по значению сумме
	select.select_by_value(str(answer))

	# Ищем button, кликаем
	browser.find_element_by_tag_name('button').click()

	# Задержка
	time.sleep(4)

finally:
	print('Done')
	browser.close()

