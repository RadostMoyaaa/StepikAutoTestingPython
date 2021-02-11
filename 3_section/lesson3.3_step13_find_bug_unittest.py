import time, unittest
from selenium import webdriver

# Класс TestSite
class TestSite(unittest.TestCase):
	# Тест формы 1
	def test_registration_form_1(self):
		# Данные
		link = "http://suninjuly.github.io/registration1.html"
		corrected_text = "Congratulations! You have successfully registered!"
		
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
		# Чек финального текста
		final_text = browser.find_element_by_tag_name('h1').text
		self.assertEqual(final_text, corrected_text , f"Text in uncorrected: Should be - {corrected_text}, Was - {final_text}, Address - {browser.current_url}")
		browser.quit()

	# Тест формы 1
	def test_registration_form_2(self):
		# Данные
		link = "http://suninjuly.github.io/registration2.html"
		corrected_text = "Congratulations! You have successfully registered!"
		
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
		# Чек финального текста
		final_text = browser.find_element_by_tag_name('h1').text
		self.assertEqual(final_text, corrected_text , f"Text in uncorrected: Should be - {corrected_text}, Was - {final_text}, Address - {browser.current_url}")
		browser.quit()

if __name__ == "__main__":
	unittest.main()