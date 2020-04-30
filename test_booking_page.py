from .pages.main_page import MainPage
from .pages.results_page import ResultPage
import pytest
import allure


#Scenario 1. User is able to specify age of each child
class TestUserIsAbleToSpecifyAgeOfEachChild():
    @pytest.mark.scenario_1
    def test_user_should_be_able_to_specify_age_of_each_child(self, browser):
        link = "https://www.booking.com/"
        main_page = MainPage(browser, link)
        main_page.open()
        main_page.should_add_children()

#Scenario 2. User is required to specify booking date to see booking price
class TestUserIsRequiredToSpecifyBookingDateToSeeBookingPrice():
    @pytest.mark.scenario_2
    def test_user_is_required_to_specify_booking_date_to_see_booking_price(self, browser):
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
