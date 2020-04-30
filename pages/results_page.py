from .base_page import BasePage
from .locators import SearchPageLocators
import allure

class ResultPage(BasePage):
    @allure.step("checking that page with listed hotels is opened")
    def should_be_result_page(self):
        self.screenshot()
        assert self.is_element_present(*SearchPageLocators.HOTEL_LIST), "page with listed hotels should be opened"

    @allure.step("checking that calendar for specifying check in date is opened")
    def should_be_opened_calendar(self):
        self.screenshot()
        assert self.is_element_visible(*SearchPageLocators.CALENDAR), "calendar should be displayed"

    @allure.step("checking that no result entry containing booking price or booking status")
    def should_not_be_displayed_booking_price_or_booking_status(self):
        self.screenshot()
        assert self.is_not_element_present(*SearchPageLocators.BOOKING_PRICE_OR_STATUS), \
            "Booking price or status should not be displayed"

    @allure.step("checking that calendar for specifying check in date is opened")
    def should_still_be_opened_calendar(self):
        show_button = self.browser.find_element(*SearchPageLocators.SHOW_BTN)
        show_button.click()
        self.screenshot()
        assert self.is_element_visible(*SearchPageLocators.CALENDAR), "calendar should be displayed"

    @allure.step("checking that each result entry has booking price or banner saying no free places")
    def should_set_any_dates_for_check_in_and_out(self):
        check_in = self.browser.find_element(*SearchPageLocators.CHECK_IN)
        check_in.click()
        check_out_field = self.browser.find_element(*SearchPageLocators.CHECK_OUT_FIELD)
        check_out_field.click()
        check_out = self.browser.find_element(*SearchPageLocators.CHECK_OUT)
        check_out.click()
        search_btn = self.browser.find_element(*SearchPageLocators.SEARCH_BTN)
        search_btn.click()
        self.screenshot()
        assert self.is_element_present(*SearchPageLocators.BOOKING_PRICE_OR_STATUS), \
            "Booking price or status should be displayed"


