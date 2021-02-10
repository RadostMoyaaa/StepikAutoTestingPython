import math, time
from selenium import webdriver

link = "http://suninjuly.github.io/find_link_text"
answer = str(math.ceil(math.pow(math.pi, math.e)*10000))
try:
	browser = webdriver.Chrome()
	browser.get(link)
	link_2 = browser.find_element_by_partial_link_text(answer)
	link_2.click()
	input_1 = browser.find_element_by_name("first_name")
	input_1.send_keys('Test_1')

	input_1 = browser.find_element_by_name("first_name")
	input_1.send_keys('Test_1')

	input_2 = browser.find_element_by_name('last_name')
	input_2.send_keys('Test_2')

	input_3 = browser.find_element_by_class_name('city')
	input_3.send_keys('Test_3')

	input_4 = browser.find_element_by_id('country')
	input_4.send_keys('Test_4')

	button = browser.find_element_by_class_name('btn-default')
	button.click()
finally:
	time.sleep(1)
	print('Okay')