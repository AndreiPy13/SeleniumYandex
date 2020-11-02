from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import time
import pytest
from selenium.common.exceptions import NoSuchElementException, TimeoutException 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

#ПОИСК В ЯНДЕКСЕ

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


def test_link(browser):
	link = "https://yandex.ru/"  #задаем ссылку https://yandex.ru/
	#link = 'https://mail.ru/' #нужна для проверки
	browser.get(link)   #переходим на yandex
	browser.implicitly_wait(5) #ждем пока все загрузится
	try:
		search = browser.find_element_by_css_selector('#text')
	except NoSuchElementException: #проверяем есть ли поле поиск
		print('Нет поля поиск на главной странице')
	search.send_keys('Тензор')
	time.sleep(2)#можно закомментировать
	try:
		popup = WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.mini-suggest__popup.mini-suggest__popup_theme_flat.mini-suggest__popup_visible')))
	except TimeoutException: #проверяем есть ли таблица с подсказками
		print('Нет таблицы с подсказками на главной странице')
	search.send_keys(Keys.ENTER) #жмем ENTER
	links = browser.find_elements_by_css_selector('.path.path_show-https.organic__path > a > b')
	items = [elem.text.strip() for elem in links[:5]]
	#print(items)
	if "tensor.ru" not in items:
		raise Exception('сайта tensor.ru нет в первых 5 пунктах')
	time.sleep(1)#можно закомментировать

