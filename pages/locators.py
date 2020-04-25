from selenium.webdriver.common.by import By


class MainPageLocators(): #локаторы главной страницы
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class ProductPageLocators(): #локаторы страницы товара
    ADD_TO_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")



