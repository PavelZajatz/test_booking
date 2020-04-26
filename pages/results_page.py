from .base_page import BasePage
from .locators import SearchPageLocators


class ResultPage(BasePage):
    def should_be_result_page(self): # проверка, что есть форма логина зарегистрированного пользователя на странице
        assert self.is_element_present(*SearchPageLocators.HOTEL_LIST), "page with listed hotels should be opened"
    def should_be_opened_calendar(self):
        assert self.is_element_visible(*SearchPageLocators.CALENDAR), "calendar should be displayed"
    def should_not_be_displayed_booking_price(self):
        assert self.is_not_element_present(*SearchPageLocators.BOOKING_PRICE), "Booking price should not be displayed"
        assert self.is_not_element_present(*SearchPageLocators.AVAILABILITY_LABLE), \
            "Availability lable should not be displayed"
    def should_still_be_opened_calendar(self):
        show_button = self.browser.find_element(*SearchPageLocators.SHOW_BTN)
        show_button.click()
        assert self.is_element_visible(*SearchPageLocators.CALENDAR), "calendar should be displayed"
    def should_set_any_dates_for_check_in_and_out(self):
        check_in = self.browser.find_element(*SearchPageLocators.CHECK_IN)
        check_in.click()
        #check_out_field = self.browser.find_element(*SearchPageLocators.CHECK_OUT_FIELD)
        #check_out_field.click()
        serch_btn = self.browser.find_element(*SearchPageLocators.SEARCH_BTN)
        serch_btn.click()
        lables = self.browser.find_element(*SearchPageLocators.AVAILABILITY_LABLE)
        assert ("See availability" or "Select your room") in lables.text, \
            f"expected 'See availability' or 'Select your room' to be substring of '{lables.text}'"


    '''
    def add_to_basket(self): #добавление товара в корзину
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET), "Button is not presented"
        add_btn = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        add_btn.click()

    def should_be_book_price(self): #сверка цены книги в корзине
        book_price = self.browser.find_element(*ProductPageLocators.BOOK_PRICE).text
        basket_price = self.browser.find_element(*ProductPageLocators.BOOK_PRICE_BASKET).text
        assert book_price == basket_price, "Price is not same"

    def should_be_book_name(self): #сверка имени книги в корзине
        book_name = self.browser.find_element(*ProductPageLocators.BOOK_NAME).text
        book_basket = self.browser.find_element(*ProductPageLocators.BOOK_NAME_BASKET).text
        assert book_name == book_basket, "Name is not same"

    def should_not_be_success_message(self): #проверка что сообщение об успехе не отображено
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented"
    '''