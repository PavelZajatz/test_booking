import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

link = "https://www.booking.com/"



class TestBookingScenario():
    def test_booking_scenario_1(self, browser):
        browser.get(link)
        input1 = browser.find_element_by_css_selector(".xp__guests__count")
        input1.click()
        time.sleep(1)
        input2 = browser.find_element_by_css_selector(".sb-group-children [data-bui-ref='input-stepper-add-button']")
        input2.click()
        time.sleep(1)
        input2.click()
        time.sleep(1)

        select_child_1 = Select(browser.find_element_by_css_selector(".clearfix > select:nth-child(2)"))
        select_child_1.select_by_visible_text("2 years old")

        sel_1 = browser.find_element_by_css_selector(".clearfix > select:nth-child(2) > option:nth-child(4)")
        sel_1_res = sel_1.get_attribute("selected")

        select_child_2 = Select(browser.find_element_by_css_selector(".clearfix > select:nth-child(3)"))
        select_child_2.select_by_visible_text("2 years old")

        sel_2 = browser.find_element_by_css_selector(".clearfix > select:nth-child(3) > option:nth-child(4)")
        sel_2_res = sel_2.get_attribute("selected")

        assert sel_1_res == "true", "the 'selected' attribute should be present in selected 'sel'_1 option "
        assert sel_2_res == "true", "the 'selected' attribute should be present in selected 'sel'_2 option "

    def test_booking_scenario_2(self, browser):
        browser.get(link)
        # send search key into input box
        input_ss = browser.find_element_by_id("ss")
        input_ss.send_keys("Za")
        time.sleep(1)
        # select first element in the autocomplite_list
        autocomplite_list = browser.find_element_by_css_selector(".sb-autocomplete__list-with_photos > li:nth-child(1)")
        autocomplite_list.click()
        time.sleep(1)
        # submit
        button = browser.find_element_by_xpath("//div[@class='xp__button']")
        button.click()
        # нужно тут еще поработать
        current_url = browser.current_url  # get current URL
        expected_url = "https://www.booking.com/searchresults"

        # check calendar visability
        calendar = WebDriverWait(browser, 5).until(EC.visibility_of_element_located((
            By.CSS_SELECTOR, '.c2-calendar-body'))
        )

        # Expected - no result entry containing booking price or booking status- no result entry containing booking price or booking status

        # Click the 'Show prises' button
        show_button = browser.find_element_by_css_selector(".sr_item_no_dates:nth-of-type(1) .bui-button__text")
        show_button.click()
        # check calendar visavility again
        calendar2 = WebDriverWait(browser, 5).until(EC.visibility_of_element_located((
            By.CSS_SELECTOR, '.c2-calendar-body'))
        )

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

        # show error if wrong URL is opened
        assert expected_url in current_url, \
            f"expected '{expected_url}' to be substring of '{current_url}'"

        # show error if calendar is not displayed after clicking the 'Show prises' button
        assert calendar, "calendar should be displayed"

        # show error if calendar is not displayed after loading the page
        assert calendar2, "calendar2 should be displayed"

        # show error if "See availability" or "Select your room" lable is not displayed
        assert ("See availability" or "Select your room") in lable.text, \
            f"expected 'See availability' or 'Select your room' to be substring of '{lable.text}'"








