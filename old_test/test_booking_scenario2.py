import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

link = "https://www.booking.com/"

class TestBookingScenario():

    def test_booking_scenario_step_1(self, browser):
        try:
            browser.get(link)
            # send search key into input box
            input_ss = browser.find_element_by_id("ss")
            input_ss.send_keys("Za")
            time.sleep(1)
            # select first element in the autocomplete_list
            autocomplete_list = browser.find_element_by_css_selector(
                ".sb-autocomplete__list-with_photos > li:nth-child(1)")
            autocomplete_list.click()
            time.sleep(1)
            # submit
            button = browser.find_element_by_xpath("//div[@class='xp__button']")
            button.click()
            # get current URL
            expected_url = "https://www.booking.com/searchresults"
            current_url = browser.current_url

            # check calendar visibility
            calendar = WebDriverWait(browser, 5).until(EC.visibility_of_element_located((
                By.CSS_SELECTOR, '.c2-calendar-body'))
            )
            # Expected - no result entry containing booking price or booking status
            bui_buttons = browser.find_elements_by_xpath("//*[contains(@class,'no_dates_click jq_tooltip')]")
            for bui_button in bui_buttons:
                continue

        finally:
            # show error if wrong URL is opened
            assert expected_url in current_url, \
                f"expected '{expected_url}' to be substring of '{current_url}'"

            # show error if calendar is not displayed after clicking the 'Show prises' button
            assert calendar, "calendar should be displayed"

            # show error if 'Show prices' lable is not displayed
            assert "Show prices" in bui_button.text, \
                f"expected 'Show prices' to be substring of '{bui_button.text}'"



    def test_booking_scenario_step_2(self, browser):
        try:

            # Click the 'Show prises' button
            show_button = browser.find_element_by_css_selector(".sr_item_no_dates:nth-of-type(1) .bui-button__text")
            show_button.click()
            # check calendar visavility again
            calendar2 = WebDriverWait(browser, 5).until(EC.visibility_of_element_located((
                By.CSS_SELECTOR, '.c2-calendar-body'))
            )
        finally:
            # show error if calendar is not displayed after loading the page
            assert calendar2, "calendar2 should be displayed"

    def test_booking_scenario_step_3(self, browser):
        try:

            # Select start day IN (*//td[contains(@class, 'c2-day')][not(contains(@class, 'disabled'))])[1]
            # OUT (*//td[contains(@class, 'c2-day')][not(contains(@class, 'disabled'))]//span[text() = '16'])[1]
            WebDriverWait(browser, 10).until(
                EC.visibility_of_element_located((
                    By.CSS_SELECTOR, ".c2-day.c2-day-s-today"))).click()
            time.sleep(1)
            # Click the 'Search' button
            submit = browser.find_element_by_css_selector(".sb-searchbox__button")
            submit.click()
            time.sleep(5)
            # Check  results for 'Select your room' test if result is avaiable for booking or 'See availability' if not
            lables = browser.find_elements_by_class_name("sr_cta_button")
            for lable in lables:
                continue
        finally:
            # show error if "See availability" or "Select your room" lable is not displayed
            assert ("See availability" or "Select your room") in lable.text, \
                f"expected 'See availability' or 'Select your room' to be substring of '{lable.text}'"















