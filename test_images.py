from .pages.image_page import ImagePage

import pytest

def test_images(browser):
	link = 'https://yandex.ru/'
	page = ImagePage(browser, link)
	page.open()
	page.image_test()



#pytest -v test_images.py -s