from .base_page import BasePage
from .locators import MainPageLocators
import allure
from allure_commons.types import AttachmentType

class MainPage(BasePage):
    def should_add_children(self): #method with checking the number of age inputs is equal to N
        add_guest = self.browser.find_element(*MainPageLocators.GUESTS_COUNTER)
        add_guest.click()
        add_child = self.browser.find_element(*MainPageLocators.ADD_CHILD_BTN)
        add_child.click()
        add_child.click()
        ages_inputs = self.browser.find_elements(*MainPageLocators.AGE)
        assert len(ages_inputs) == 2, 'The number of age inputs should be equal to 2'


    def should_choose_any_city(self): #method with choosing a city and going to the search page
        input_location = self.browser.find_element(*MainPageLocators.WHERE_ARE_YOU)
        input_location.send_keys(*MainPageLocators.LOCATION)
        first_location_option = self.browser.find_element(*MainPageLocators.AUTOCOMPLETE_LIST_OPTION)
        first_location_option.click()
        search_btn = self.browser.find_element(*MainPageLocators.SEARCH_BTN)
        search_btn.click()
