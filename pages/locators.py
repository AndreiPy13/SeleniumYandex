from selenium.webdriver.common.by import By


class SearchPageLocators():
	SEARCH_WINDOW = (By.CSS_SELECTOR, "#text")
	SUGGEST_TABLE = (By.CSS_SELECTOR, '.mini-suggest__popup.mini-suggest__popup_theme_flat.mini-suggest__popup_visible')
	LINKS_IN_SEARCH = (By.CSS_SELECTOR, ".path.path_show-https.organic__path > a > b")




class ImagePageLocators():
	LINK_IMAGES = (By.CSS_SELECTOR, '[data-id="images"]')
	FIRST_CATEGORY = (By.CSS_SELECTOR, '.PopularRequestList-Item.PopularRequestList-Item_pos_0 > a > img')
	FIRST_CATEGORY_TEXT = (By.CSS_SELECTOR, '.PopularRequestList-Item.PopularRequestList-Item_pos_0 > a > div.PopularRequestList-SearchText')
	FIRST_IMAGE_IN_SEARCH = (By.XPATH, '//body/div[5]/div[1]/div[1]/div[1]/div/div[1]/div/a')
	WINDOW_WITH_IMG = (By.CSS_SELECTOR,'.MediaViewer.MediaViewer_theme_fiji.ImagesViewer-Container')
	BACK_BUTTON = (By.CSS_SELECTOR, ".MediaViewer-ButtonPrev.MediaViewer_theme_fiji-ButtonPrev > i")
	FORWARD_BUTTON = (By.CSS_SELECTOR, ".MediaViewer-ButtonNext.MediaViewer_theme_fiji-ButtonNext > i")
	OPENED_IMAGE = (By.CSS_SELECTOR, '.MediaViewer-View.MediaViewer_theme_fiji-View > div > img')
