import time
from selenium import webdriver

link = "http://suninjuly.github.io/find_xpath_form"
try:
	browser = webdriver.Chrome()
	browser.get(link)
	elements = browser.find_elements_by_tag_name('input')
	for elem in elements:
		elem.send_keys('Test')
	btn = browser.find_element_by_xpath('//button[contains(text(), "submit")]')
	btn.click()
finally:
	time.sleep(1)
	print('Done')
	