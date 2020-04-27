from .pages.base_page import BasePage
from .pages.main_page import MainPage
from .pages.results_page import ResultPage
import time
import pytest


class TestUserIsAbleToSpecifyAgeOfEachChild():
    def test_user_should_be_able_to_specify_age_of_each_child(self, browser):
        link = "https://www.booking.com/"
        main_page = MainPage(browser, link)
        main_page.open()
        main_page.should_add_children()
'''
class TestUserIsRequiredToSpecifyBookingDateToSeeBookingPrice():
    @pytest.fixture(scope="function", autouse=False)
    def setup(self, browser):
        link = "https://www.booking.com/"
        main_page = MainPage(browser, link)
        main_page.open()
'''
class TestUserIsRequiredToSpecifyBookingDateToSeeBookingPrice():
    def test_user(self, browser):
        link = "https://www.booking.com/"
        main_page = MainPage(browser, link)
        main_page.open()
        main_page.should_choose_any_city()
        result_page = ResultPage(browser, browser.current_url)
        result_page.should_be_result_page()
        result_page.should_be_opened_calendar()
        result_page.should_not_be_displayed_booking_price_or_booking_status()
        result_page.should_still_be_opened_calendar()
        result_page.should_set_any_dates_for_check_in_and_out()
