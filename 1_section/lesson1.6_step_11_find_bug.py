import time
from selenium import webdriver
link = "http://suninjuly.github.io/registration2.html"

try:
	browser = webdriver.Chrome()
	browser.get(link)
	# Находим элементы для проверки
	first_inp = browser.find_element_by_css_selector('input.first[required]')
	second_inp = browser.find_element_by_css_selector('input.second[required]')
	third_inp = browser.find_element_by_css_selector('input.third[required]')
	# Отправляем данные в элемент
	first_inp.send_keys('Test_1')
	second_inp.send_keys('Test_2')
	third_inp.send_keys('Test_3')
	# Находим кнопку и кликаем
	btn = browser.find_element_by_css_selector('button.btn')
	btn.click()
	
	time.sleep(3)
	# Чек финального текста
	w_text = browser.find_element_by_tag_name('h1')
	assert w_text.text == "Congratulations! You have successfully registered!"
finally:	
	print('Done')
	time.sleep(3)
	browser.quit()
