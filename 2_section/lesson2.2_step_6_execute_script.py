import math, time
from selenium import webdriver

link = 'http://suninjuly.github.io/execute_script.html'

try:
	browser = webdriver.Chrome()
	browser.get(link)

	x = int(browser.find_element_by_id('input_value').text)

	answer = math.log(abs(12*math.sin(x)))

	browser.execute_script("window.scrollBy(0, 130);")

	browser.find_element_by_id('answer').send_keys(str(answer))

	browser.find_element_by_css_selector("[for='robotCheckbox']").click()

	browser.find_element_by_css_selector("[for='robotsRule']").click()

	browser.find_element_by_tag_name('button').click
finally:
	print('Done')

