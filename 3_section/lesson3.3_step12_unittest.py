import unittest

# Создаем класс теста
class TestSumma(unittest.TestCase):  # Наследование от TestCase
	# 1 метод - 1 тест
	def test_summa_1(self):
		number_1 = 3
		number_2 = 3
		test_num_1 = 3
		test_num_2 = 3
		self.assertEqual(number_1 + number_2, test_num_1 + test_num_2, f"Summa should be{number_1 + number_2}, was {test_num_1 + test_num_2}")

	def test_summa_2(self):
		number_1 = 4
		number_2 = 3
		test_num_1 = 3
		test_num_2 = 3
		self.assertEqual(number_1 + number_2, test_num_1 + test_num_2, f"Summa should be{number_1 + number_2}, was {test_num_1 + test_num_2}")

if __name__ == "__main__":
	unittest.main()