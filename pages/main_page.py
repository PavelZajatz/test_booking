from .base_page import BasePage
from .locators import MainPageLocators
from selenium.webdriver.support.ui import Select


class MainPage(BasePage):

    def should_add_children(self):
        add_guest = self.browser.find_element(*MainPageLocators.GUESTS_COUNTER)
        add_guest.click()
        add_child = self.browser.find_element(*MainPageLocators.ADD_CHILD_BTN)
        add_child.click()
        add_child.click()
        select_first_child_dd = Select(self.browser.find_element(*MainPageLocators.FIRST_CHILD_DD))
        select_first_child_dd.select_by_visible_text("2 years old")
        first_child_2_year_option = self.browser.find_element(*MainPageLocators.FIRST_CHILD_2_YEAR_OPTION)
        assert first_child_2_year_option.get_attribute("selected"), \
                           "the 'selected' attribute should be present in selected '2 years old' option "
        select_second_child_dd = Select(self.browser.find_element(*MainPageLocators.SECOND_CHILD_DD))
        select_second_child_dd.select_by_visible_text("2 years old")
        second_child_2_year_option = self.browser.find_element(*MainPageLocators.SECOND_CHILD_2_YEAR_OPTION)
        assert second_child_2_year_option.get_attribute("selected"), \
                            "the 'selected' attribute should be present in selected '2 years old' option "

    def should_choose_any_city(self):
        input_location = self.browser.find_element(*MainPageLocators.WHERE_ARE_YOU)
        input_location.send_keys(*MainPageLocators.LOCATION)
        first_location_option = self.browser.find_element(*MainPageLocators.AUTOCOMPLETE_LIST_OPTION)
        first_location_option.click()
        search_btn = self.browser.find_element(*MainPageLocators.SEARCH_BTN)
        search_btn.click()
