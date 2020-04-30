from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure
from allure_commons.types import AttachmentType



class BasePage():
    def __init__(self, browser, link, timeout=2): #basic browser initialization method
        self.browser = browser
        self.link = link
        self.browser.implicitly_wait(timeout)

    def open(self):  #basic page opening method
        self.browser.get(self.link)

    def screenshot(self): #method for making screenshot for allure report
        with allure.step("make screenshot"):
            allure.attach(self.browser.get_screenshot_as_png(), name='Screenshot', attachment_type=AttachmentType.PNG)


    def is_element_visible(self, how, what, timeout=3): #basic method of checking that the element is visible
        try:
            WebDriverWait(self.browser, timeout).until(EC.visibility_of_element_located((how, what)))
        except TimeoutException:
            return False
        return True


    def is_element_present(self, how, what, timeout=3):  #basic method of checking that an element is present
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False
        return True
    '''

    def is_element_present(self, how, what):  # базовый метод проверки что элемент присутствует
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True
    '''

    def is_not_element_present(self, how, what, timeout=3): #basic method of checking that an element isn't present
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True
        return False