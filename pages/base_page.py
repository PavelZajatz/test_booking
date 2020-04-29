from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class BasePage():
    def __init__(self, browser, link, timeout=2):
        self.browser = browser
        self.link = link


    def open(self):
        self.browser.get(self.link)

    '''
    def is_element_present(self, how, what): #базовый метод проверки что элемент присутствует
        try:
            self.browser.find_element(how, what)
        except (NoSuchElementException):
            return False
        return True
    '''



    def is_element_visible(self, how, what, timeout=3): #базовый метод проверки что элемент присутствует
        try:
            WebDriverWait(self.browser, timeout).until(EC.visibility_of_element_located((how, what)))
        except TimeoutException:
            return False
        return True

    def is_element_present(self, how, what, timeout=3):  # базовый метод проверки что элемент присутствует
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False
        return True

    def is_not_element_present(self, how, what, timeout=3): #базовый метод проверки что элемент не присутствует
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True
        return False