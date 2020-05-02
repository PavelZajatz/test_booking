from .base_page import BasePage
from .locators import SearchPageLocators
import allure

class ResultPage(BasePage):
    """
    Class with methods for Result page(descendant of the BasePage class)
    """
    @allure.step("checking that page with listed hotels is opened")
    def should_be_result_page(self):
        """
        Method checks that page with listed hotels is opened
        """
        self.screenshot()
        assert self.is_element_visible(*SearchPageLocators.HOTEL_LIST), \
            "Listed hotels aren't displayed after opening result page"

    @allure.step("checking that calendar for specifying check in date is opened")
    def should_be_opened_calendar(self):
        """
        Method checks that calendar for specifying check in date is opened after
        opening the Result page
        """
        self.screenshot()
        assert self.is_element_visible(*SearchPageLocators.CALENDAR), \
            "The calendar isn't displayed after opening result page"

    @allure.step("checking that no result entry containing booking price or booking status")
    def should_not_be_displayed_booking_price_or_booking_status(self):
        """
        Method checks that no result entry containing booking price or booking status are present after
        opening the Result page
        """
        self.screenshot()
        assert self.is_not_element_present(*SearchPageLocators.BOOKING_PRICE_OR_STATUS), \
            "Booking price or status is displayed after opening result page"

    @allure.step("checking that calendar for specifying check in date is opened")
    def should_still_be_opened_calendar(self):
        """
        Method checks that calendar for specifying check in date is opened after clicking the 'Show' button
        """
        show_button = self.browser.find_element(*SearchPageLocators.SHOW_BTN)
        show_button.click()
        self.screenshot()
        assert self.is_element_visible(*SearchPageLocators.CALENDAR), \
            "The calendar isn't displayed after clicking the 'Show' button"

    @allure.step("checking that each result entry has booking price or banner saying no free places")
    def should_set_any_dates_for_check_in_and_out(self):
        """
        Method checks that each result entry has booking price or banner saying no free places after
        setting check in and check out dates and searching
        """
        check_in_date = self.browser.find_element(*SearchPageLocators.CHECK_IN_DATE)
        check_in_date.click()
        check_out_field = self.browser.find_element(*SearchPageLocators.CHECK_OUT_FIELD)
        check_out_field.click()
        check_out_date = self.browser.find_element(*SearchPageLocators.CHECK_OUT_DATE)
        check_out_date.click()
        search_btn = self.browser.find_element(*SearchPageLocators.SEARCH_BTN)
        search_btn.click()
        booking_prise_or_status = self.browser.find_elements(*SearchPageLocators.BOOKING_PRICE_OR_STATUS)
        results_items = self.browser.find_elements(*SearchPageLocators.RESULTS_ITEM)
        self.screenshot()
        assert len(booking_prise_or_status) == len(results_items), \
            "result entry has not booking price or banner saying no free places"





