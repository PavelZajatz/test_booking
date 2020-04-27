from .base_page import BasePage
from .locators import SearchPageLocators


class ResultPage(BasePage):
    def should_be_result_page(self): # проверка, что есть форма логина зарегистрированного пользователя на странице
        assert self.is_element_present(*SearchPageLocators.HOTEL_LIST), "page with listed hotels should be opened"
    def should_be_opened_calendar(self):
        assert self.is_element_visible(*SearchPageLocators.CALENDAR), "calendar should be displayed"
    def should_not_be_displayed_booking_price_or_booking_status(self):
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
        search_btn = self.browser.find_element(*SearchPageLocators.SEARCH_BTN)
        search_btn.click()
        lables = self.browser.find_elements(*SearchPageLocators.AVAILABILITY_LABLE)
        for lable in lables:
            print(lable.text)
            continue
        assert ("See availability" or "Select your room") in lable.text, \
            f"expected 'See availability' or 'Select your room' to be substring of '{lable.text}'"
