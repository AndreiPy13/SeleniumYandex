from .pages.search_page import SearchPage

import pytest


def test_main_yandex(browser):
	link = 'https://yandex.ru/'
	page = SearchPage(browser, link)
	page.open()
	page.search_in_Yandex()



#pytest -v test_yandex.py -s