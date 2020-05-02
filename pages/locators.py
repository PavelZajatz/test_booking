from selenium.webdriver.common.by import By


class MainPageLocators():
    """
    Class with locators for main page
    """
    GUESTS_COUNTER_FIELD = (By.XPATH, ".//*[contains(@class, 'xp__guests__count')]")
    ADD_CHILD_BTN = (By.XPATH, "(.//*[contains(@class, 'bui-button__text')])[4]")
    AGE_DROP_DOWN = (By.NAME, 'age')
    WHERE_ARE_YOU_FIELD = (By.ID, "ss")
    LOCATION = "Za"
    AUTOCOMPLETE_LIST_OPTION = (By.CSS_SELECTOR, ".sb-autocomplete__list-with_photos > li:nth-child(1)")
    SEARCH_BTN = (By.XPATH, "//div[@class='xp__button']")

class SearchPageLocators():
    """
    Class with locators for search results page
    """
    HOTEL_LIST = (By.ID, "hotellist_inner")
    CALENDAR = (By.CSS_SELECTOR, ".c2-calendar-body")
    BOOKING_PRICE_OR_STATUS = (By.XPATH, ".//*[contains(@class, 'bui-price-display__value')]|"
                                         ".//span[contains( @ class, 'sold_out_property')]")
    RESULTS_ITEM = (By.CLASS_NAME, 'sr_item')
    SHOW_BTN = (By.CSS_SELECTOR, ".bui-button__text")
    CHECK_IN_DATE = (By.XPATH, "(*//td[contains(@class, 'c2-day')][not(contains(@class, 'disabled'))])[1]")
    CHECK_OUT_FIELD = (By.XPATH, "(.//*[contains(@class, 'sb-date-field__display')])[2]")
    CHECK_OUT_DATE = (By.XPATH,
                 "(//*[contains(@class, '--checkout-field ')]"
                 "//td[not(contains(@class, 'disabled'))]//span[text() = '16'])[1]")
    SEARCH_BTN = (By.CSS_SELECTOR, ".sb-searchbox__button")








