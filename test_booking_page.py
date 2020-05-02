from .pages.main_page import MainPage
from .pages.results_page import ResultPage
import pytest



class TestUserIsAbleToSpecifyAgeOfEachChild():
    """
    Scenario 1. User is able to specify age of each child
    1. go to home page
    2. open menu for selecting strangers number
    3. specify N number of children (N > 1)
    Expect: the number of age inputs is equal to N
    """
    @pytest.mark.scenario_1
    def test_user_should_be_able_to_specify_age_of_each_child(self, browser):
        """
        Test scenario 1
        :param browser: driver instance
        """
        link = "https://www.booking.com/"
        main_page = MainPage(browser, link)
        main_page.open()
        main_page.should_add_children()


class TestUserIsRequiredToSpecifyBookingDateToSeeBookingPrice():
    """
    Scenario 2. User is required to specify booking date to see booking price
    Preconditions:
    User is at home page
    1. choose any city from the menu below
    Expect:
    - page with listed hotels is opened
    - calendar for specifying check in date is opened
    - no result entry containing booking price or booking status
    2. Click "show prices" button for any hotel
    Expect: calendar for specifying check in date is opened
    3. Set any dates for check in and out
    4. Submit search form
    Expect: each result entry has booking price or banner saying no free places
    """
    @pytest.mark.scenario_2
    def test_user_is_required_to_specify_booking_date_to_see_booking_price(self, browser):
        """
        Test scenario 2
        :param browser: driver instance
        """
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
