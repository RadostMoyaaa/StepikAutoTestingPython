import os
from selenium import webdriver

# print(os.path.abspath(__file__))

# print(os.path.abspath(os.path.dirname(__file__)))

link = 'http://suninjuly.github.io/file_input.html'

try:
	browser = webdriver.Chrome()
	browser.get(link)
	inputs = browser.find_elements_by_css_selector('input[required]')

	for i in range(len(inputs)-1):
		inputs[i].send_keys('Test')
	directory = os.path.abspath(os.path.dirname(__file__))
	file = os.path.join(directory, 'file.txt')

	inputs[len(inputs)-1].send_keys(file)
	browser.find_element_by_tag_name('button').click()

finally:
	print('done')