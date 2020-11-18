from .base_page import BasePage
from .locators import SearchPageLocators
import time
from selenium.webdriver.common.keys import Keys


class SearchPage(BasePage):

	def search_in_Yandex(self):
		self.search_field()
		self.visibility_suggest_table()
		self.tenzor_link_result()

	def search_field(self):
		assert self.is_element_present(*SearchPageLocators.SEARCH_WINDOW), \
			"Нет поля поиск на главной странице"

	def visibility_suggest_table(self):
		search_box = self.browser.find_element(*SearchPageLocators.SEARCH_WINDOW)
		search_box.send_keys('Тензор')
		time.sleep(2)
		assert self.is_visibility_located(*SearchPageLocators.SUGGEST_TABLE), \
			"Нет таблицы с подсказками на главной странице"
		search_box.send_keys(Keys.ENTER)

	def tenzor_link_result(self):
		links = self.browser.find_elements(*SearchPageLocators.LINKS_IN_SEARCH)
		items = [elem.text.strip() for elem in links[:5]]
		#print(items)
		if "tensor.ru" not in items:
			raise Exception('сайта tensor.ru нет в первых 5 пунктах')
		time.sleep(1)#можно закомментировать




