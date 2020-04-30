from selenium.webdriver.common.by import By


class MainPageLocators(): #locators for main page
    GUESTS_COUNTER = (By.XPATH, ".//*[contains(@class, 'xp__guests__count')]")
    ADD_CHILD_BTN = (By.XPATH, "(.//*[contains(@class, 'bui-button__text')])[4]")
    AGE = (By.NAME, 'age')
    WHERE_ARE_YOU = (By.ID, "ss")
    LOCATION = "Za"
    AUTOCOMPLETE_LIST_OPTION = (By.CSS_SELECTOR, ".sb-autocomplete__list-with_photos > li:nth-child(1)")
    SEARCH_BTN = (By.XPATH, "//div[@class='xp__button']")

class SearchPageLocators(): #locators for search results page
    RESULT_URL = "https://www.booking.com/searchresults"
    HOTEL_LIST = (By.ID, "hotellist_inner")
    CALENDAR = (By.CSS_SELECTOR, ".c2-calendar-body")
    BOOKING_PRICE_OR_STATUS = (By.XPATH, ".//*[contains(@class, 'bui-price-display__value')]|"
                                         ".//span[contains( @ class, 'sold_out_property')]")
    SHOW_BTN = (By.CSS_SELECTOR, ".bui-button__text")
    CHECK_IN = (By.XPATH, "(*//td[contains(@class, 'c2-day')][not(contains(@class, 'disabled'))])[1]")
    CHECK_OUT_FIELD = (By.XPATH, "(.//*[contains(@class, 'sb-date-field__display')])[2]")
    CHECK_OUT = (By.XPATH,
                 "(//*[contains(@class, '--checkout-field ')]"
                 "//td[not(contains(@class, 'disabled'))]//span[text() = '16'])[1]")
    SEARCH_BTN = (By.CSS_SELECTOR, ".sb-searchbox__button")
    '''

    NO_FREE_OR_PRICE= (By.XPATH, ".//div[contains(@class, 'sr_item_new')]"
                                 "//*[contains(@class, 'bui-price-display__value')]|"
                                 ".//div[contains(@class, 'sr_item_new')]"
                                 ".//span[contains( @ class, 'sold_out_property')]")

    '''





