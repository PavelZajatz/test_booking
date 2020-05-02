from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure
from allure_commons.types import AttachmentType


class BasePage():
    """
    Class with Base methods
    """
    def __init__(self, browser, link, timeout=2):
        """
        BasePage constructor
        :param browser: driver instance
        :param link: site URL
        :param timeout: an argument that indicates how long to wait
        """
        self.browser = browser
        self.link = link
        self.browser.implicitly_wait(timeout)

    def open(self):
        """
        Page opening method
        """
        self.browser.get(self.link)

    def screenshot(self):
        """
        Screenshot making method for allure report
        """
        with allure.step("make screenshot"):
            allure.attach(self.browser.get_screenshot_as_png(), name='Screenshot', attachment_type=AttachmentType.PNG)

    def is_element_visible(self, how, what, timeout=3):
        """
        Basic method of checking that the element is visible
        :param how: an argument that indicates how to search (css, id, xpath и i.e.)
        :param what: an argument that indicates what to search for (selector string)
        :param timeout: an argument that indicates how long to wait
        :return: bool. return True if the element is visible else it will return False
        """
        try:
            WebDriverWait(self.browser, timeout).until(EC.visibility_of_element_located((how, what)))
        except TimeoutException:
            return False
        return True

    def is_not_element_present(self, how, what, timeout=3):
        """
        Basic method of checking that an element isn't present
        :param how: an argument that indicates how to search (css, id, xpath и i.e.)
        :param what: an argument that indicates what to search for (selector string)
        :param timeout: an argument that indicates how long to wait
        :return:  bool. return False if the element is present else it will return True
        """
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True
        return False
