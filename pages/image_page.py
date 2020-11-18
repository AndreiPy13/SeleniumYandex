from .base_page import BasePage
from .locators import ImagePageLocators

from urllib.parse import unquote
import time


class ImagePage(BasePage):


	def image_test(self):
		self.link_images()
		self.category_check()
		self.action_with_images()

	def link_images(self):
		window_before = self.browser.window_handles[0]
		assert self.is_element_present(*ImagePageLocators.LINK_IMAGES), \
			"Нет ссылки 'Картинки' на странице"
		images = self.browser.find_element(*ImagePageLocators.LINK_IMAGES)
		images.click()
		window_after = self.browser.window_handles[1]
		self.browser.switch_to.window(window_after)
		time.sleep(2)
		assert 'https://yandex.ru/images/' in self.browser.current_url, \
			'Вы перешли не на страницу с картинками'

	def category_check(self):
		category1 = self.browser.find_element(*ImagePageLocators.FIRST_CATEGORY) 
		category1_text = self.browser.find_element(*ImagePageLocators.FIRST_CATEGORY_TEXT).text
		self.browser.execute_script("arguments[0].click();", category1)
		time.sleep(2)
		search_text = unquote(self.browser.current_url).replace('https://yandex.ru/images/search?utm_source=main_stripe_big&text=', '')
		search_text_corrected = search_text.strip('&nl=1')
		assert category1_text == search_text_corrected, 'Поиск не соответствует выбранной картинке'

	def action_with_images(self):
		picture1 = self.browser.find_element(*ImagePageLocators.FIRST_IMAGE_IN_SEARCH).click()
		assert self.is_element_present(*ImagePageLocators.WINDOW_WITH_IMG),\
			'Окно с картинкой не открывается!'
		#time.sleep(2)
		id_image1 = self.browser.find_element(*ImagePageLocators.OPENED_IMAGE).get_attribute('src')
		button_next = self.browser.find_element(*ImagePageLocators.FORWARD_BUTTON).click()
		#time.sleep(2)
		id_image2 = self.browser.find_element(*ImagePageLocators.OPENED_IMAGE).get_attribute('src')
		assert id_image1 != id_image2, 'Картинка не изменилась после нажатия кнопки "вперед"!'
		#time.sleep(2)
		button_prev = self.browser.find_element(*ImagePageLocators.BACK_BUTTON).click()
		id_image3 = self.browser.find_element(*ImagePageLocators.OPENED_IMAGE).get_attribute('src')
		assert id_image1 == id_image3, 'Кнопка "назад" не возвращает на предыдущую картинку!'
		#time.sleep(2)

	