from selenium.webdriver.common.by import By


class MainPageLocators(): #локаторы главной страницы
    GUESTS_COUNTER = (By.XPATH, ".//*[contains(@class, 'xp__guests__count')]")
    ADD_CHILD_BTN = (By.XPATH, "(.//*[contains(@class, 'bui-button__text')])[4]")


class ProductPageLocators(): #локаторы страницы товара
    ADD_TO_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")



