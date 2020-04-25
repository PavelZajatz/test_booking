from .pages.base_page import BasePage
import time
import pytest


class TestUserIsAbleToSpecifyAgeOfEachChild():
    def test_user_should_be_able_to_specify_age_of_each_child(self, browser):
        link = "https://www.booking.com/"
        main_page = BasePage(browser, link)
        main_page.open()
