import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
import time

def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="chrome",
                         help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default="en-gb",
                         help="Choose language: en-gb or ru")

@pytest.fixture(scope="class") #fixture for language and browser selection
def browser(request):
    print("\nstart browser for test..")
    user_language = request.config.getoption("language")
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        options = Options()
        options.add_argument("--kiosk")
        options.add_argument("–disable-infobars")
        options.add_experimental_option("prefs", {"intl.accept_languages": user_language})
        browser = webdriver.Chrome(ChromeDriverManager().install(), options=options)

    elif (browser_name=="firefox"):
        fp = webdriver.FirefoxProfile()
        fp.set_preference("intl.accept_languages", user_language)
        browser = webdriver.Firefox(GeckoDriverManager().install(), firefox_profile=fp)
        browser.maximize_window()

    else:
        print("Browser <browser_name> is still not implemented")
    yield browser
    print("\nquit browser..")
    time.sleep(2)
    browser.quit()
