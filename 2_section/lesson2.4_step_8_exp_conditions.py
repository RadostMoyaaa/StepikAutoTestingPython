from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math 

link = 'http://suninjuly.github.io/explicit_wait2.html'

try:
	# Открываем браузер, страницу
	browser = webdriver.Chrome()
	browser.get(link)
	# Ставим явное ожидание, пока не появится текст $100 в поле
	cost = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), '$100'))

	btn = browser.find_element_by_id('book')
	btn.click()
	
	# Считаем уравние, отправляем ответ
	x = int(browser.find_element_by_id('input_value').text)
	answer = math.log(abs(12*math.sin(x)))
	browser.find_element_by_id('answer').send_keys(str(answer))
	
	# Кликаем кнопку
	browser.find_element_by_id("solve").click()

finally:
	print('done')