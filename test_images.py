from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import time
import pytest
from selenium.common.exceptions import NoSuchElementException 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from urllib.parse import unquote

#КАРТИНКИ НА ЯНДЕКСЕ

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()



def test_images(browser):
	link = "https://yandex.ru/"
	browser.get(link)   #переходим на yandex
	browser.implicitly_wait(5)
	window_before = browser.window_handles[0]
	try:
		images = browser.find_element_by_css_selector('[data-id="images"]')
	except NoSuchElementException: #проверяем есть ссылка картинки
		print('Нет ссылки "Картинки" на главной странице')
	images.click()
	window_after = browser.window_handles[1]
	browser.switch_to.window(window_after)
	time.sleep(2) #можно закомметировать
	assert 'https://yandex.ru/images/' in browser.current_url, 'Вы перешли не на страницу с картинками'
	first_category = browser.find_element_by_css_selector('.PopularRequestList-Item.PopularRequestList-Item_pos_0 > a > img')
	text1 = browser.find_element_by_css_selector('.PopularRequestList-Item.PopularRequestList-Item_pos_0 > a > div.PopularRequestList-SearchText').text
	browser.execute_script("arguments[0].click();", first_category)
	#print(text1)
	time.sleep(2) #можно закомметировать
	text2 = unquote(browser.current_url).replace('https://yandex.ru/images/search?utm_source=main_stripe_big&text=', '')
	text_corrected = text2.strip('&nl=1')
	assert text1 == text_corrected, 'Поиск не соответствует выбранной картинке'
	firstimg = browser.find_element_by_xpath('//body/div[5]/div[1]/div[1]/div[1]/div/div[1]/div/a')
	firstimg.click()
	try:
		imgcontrol = browser.find_element_by_css_selector('.MediaViewer.MediaViewer_theme_fiji.ImagesViewer-Container')
	except NoSuchElementException: 
		print('Окно с картинкой не открывается')
	time.sleep(2)
	button_next = browser.find_element_by_css_selector(".MediaViewer-ButtonNext.MediaViewer_theme_fiji-ButtonNext > i") 
	img1 = browser.find_element_by_css_selector('.MediaViewer-View.MediaViewer_theme_fiji-View > div > img')
	pic1 = img1.get_attribute('src')
	#print(pic1)
	button_next.click()
	time.sleep(2) #можно закомметировать
	img2 = browser.find_element_by_css_selector('.MediaViewer-View.MediaViewer_theme_fiji-View > div > img')
	pic2 = img2.get_attribute('src')
	#print(pic2)
	assert pic1 != pic2, 'Картинка не изменилась после нажатия кнопки "вперед"'
	time.sleep(2) #можно закомметировать
	button_back = browser.find_element_by_css_selector(".MediaViewer-ButtonPrev.MediaViewer_theme_fiji-ButtonPrev > i") 
	button_back.click()
	img3 = browser.find_element_by_css_selector('.MediaViewer-View.MediaViewer_theme_fiji-View > div > img')
	pic3 = img3.get_attribute('src')
	#Sprint(pic3)
	assert pic1 == pic3, 'Кнопка назад возвращает на другую картинку'
	time.sleep(2) #можно закомметировать