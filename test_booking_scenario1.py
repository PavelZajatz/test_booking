import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

link = "https://www.booking.com/"



class TestBookingScenario():
    def test_booking_scenario_1(self, browser):
        try:
            browser.get(link)
            #should open guests counter drop-down
            input1 = browser.find_element_by_css_selector(".xp__guests__count")
            input1.click()
            time.sleep(1)
            # should find the "+" children button
            input2 = browser.find_element_by_css_selector(
                ".sb-group-children [data-bui-ref='input-stepper-add-button']")
            # the number of children should be equal to 1
            input2.click()
            time.sleep(1)
            # the number of children should be equal to 2
            input2.click()
            time.sleep(1)
            #should find first children age drop-down
            select_child_1 = Select(browser.find_element_by_css_selector(".clearfix > select:nth-child(2)"))
            #should select "2 years old" age for first children by visible text
            select_child_1.select_by_visible_text("2 years old")
            #should find selected "2 years old" option for first child from previous step
            sel_1 = browser.find_element_by_css_selector(".clearfix > select:nth-child(2) > option:nth-child(4)")
            #check if  "2 years old" option for first child has 'selected' attribute
            sel_1_res = sel_1.get_attribute("selected")
            # should find second children age drop-down
            select_child_2 = Select(browser.find_element_by_css_selector(".clearfix > select:nth-child(3)"))
            # should select "2 years old" age for second children by visible text
            select_child_2.select_by_visible_text("2 years old")
            # should find selected "2 years old" option for second child from previous step
            sel_2 = browser.find_element_by_css_selector(".clearfix > select:nth-child(3) > option:nth-child(4)")
            # check if  "2 years old" option for second child has 'selected' attribute
            sel_2_res = sel_2.get_attribute("selected")

        finally:
            # check if 'selected' attribute is present for '2 year' age option for 1st child
            assert sel_1_res == "true", "the 'selected' attribute should be present in selected 'sel'_1 option "
            # check if 'selected' attribute is present for '2 year' age option for 2nd child
            assert sel_2_res == "true", "the 'selected' attribute should be present in selected 'sel'_2 option "










