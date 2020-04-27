from selenium.webdriver.common.by import By


class MainPageLocators(): #локаторы главной страницы
    GUESTS_COUNTER = (By.XPATH, ".//*[contains(@class, 'xp__guests__count')]")
    ADD_CHILD_BTN = (By.XPATH, "(.//*[contains(@class, 'bui-button__text')])[4]")
    FIRST_CHILD_DD = (By.CSS_SELECTOR, ".clearfix > select:nth-child(2)")
    FIRST_CHILD_2_YEAR_OPTION = (By.CSS_SELECTOR, ".clearfix > select:nth-child(2) > option:nth-child(4)")
    SECOND_CHILD_DD = (By.CSS_SELECTOR, ".clearfix > select:nth-child(3)")
    SECOND_CHILD_2_YEAR_OPTION = (By.CSS_SELECTOR, ".clearfix > select:nth-child(3) > option:nth-child(4)")
    WHERE_ARE_YOU = (By.ID, "ss")
    LOCATION = "Za"
    AUTOCOMPLETE_LIST_OPTION = (By.CSS_SELECTOR, ".sb-autocomplete__list-with_photos > li:nth-child(1)")
    SEARCH_BTN = (By.XPATH, "//div[@class='xp__button']")

class SearchPageLocators():
    RESULT_URL = "https://www.booking.com/searchresults"
    HOTEL_LIST = (By.ID, "hotellist_inner")
    CALENDAR = (By.CSS_SELECTOR, ".c2-calendar-body")
    BOOKING_PRICE = (By.CSS_SELECTOR, ".bui-price-display__value")
    AVAILABILITY_LABLE = (By.XPATH, "//*[contains(text(),'Select your room') or contains(text(),'See availability')][contains(@class, 'bui-button__text')]")
    SHOW_BTN = (By.CSS_SELECTOR, ".bui-button__text")
    CHECK_IN = (By.XPATH, "(*//td[contains(@class, 'c2-day')][not(contains(@class, 'disabled'))])[1]")
    CHECK_OUT_FIELD = (By.XPATH, "(.//*[contains(@class, 'sb-date-field__display')])[2]")
    #CHECK_OUT = (By.XPATH,
    #             "(*//td[contains(@class, 'c2-day')][not(contains(@class, 'disabled'))]//span[text() = '16'])[1]")
    SEARCH_BTN = (By.CSS_SELECTOR, ".sb-searchbox__button")






