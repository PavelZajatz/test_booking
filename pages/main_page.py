from .base_page import BasePage
from .locators import MainPageLocators
import allure


class MainPage(BasePage):
    """
    Class with methods for Main page(descendant of the BasePage class)
    """
    @allure.step("checking that the number of age inputs is equal to N")
    def should_add_children(self):
        """
        Method with checking that the number of age inputs isn't equal to number of added child's
        """
        add_guest = self.browser.find_element(*MainPageLocators.GUESTS_COUNTER_FIELD)
        add_guest.click()
        add_child = self.browser.find_element(*MainPageLocators.ADD_CHILD_BTN)
        add_child.click()
        add_child.click()
        ages_inputs = self.browser.find_elements(*MainPageLocators.AGE_DROP_DOWN)
        self.screenshot()
        assert len(ages_inputs) == 2, "The number of age inputs isn't equal to number of added child's"

    @allure.step("choosing a city and going to the search page")
    def should_choose_any_city(self):
        """
        Method with choosing a city from the menu and going to the search page
        """
        input_location = self.browser.find_element(*MainPageLocators.WHERE_ARE_YOU_FIELD)
        input_location.send_keys(*MainPageLocators.LOCATION)
        first_location_option = self.browser.find_element(*MainPageLocators.AUTOCOMPLETE_LIST_OPTION)
        first_location_option.click()
        self.screenshot()
        search_btn = self.browser.find_element(*MainPageLocators.SEARCH_BTN)
        search_btn.click()
