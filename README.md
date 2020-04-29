# Object
This is a project for testing booking.com web-site using Selenium, Python, Pytest and page object model.

# File structure
 
- /test_booking/README.md - readme file
- /test_booking/__init__.py - file is required to make Python treat the directories as containing packages
- /test_booking/conftest.py - fixture with launching the browser
- /test_booking/pytest.ini - this is the main Pytest configuration file
- /test_booking/requirements.txt - dependency file
- /test_booking/test_booking_page.py - test scenario file
- /test_booking/pages/locators.py - file with locators
- /test_booking/pages/base_page.py - file with basic methods
- /test_booking/pages/main_page.py - file with methods for main page
- /test_booking/pages/results_page.py - file with methods for result page

#How to install it
- Make sure you have python installed on your machine by typing in console "python --version" if not go to https://realpython.com/installing-python/#step-1-download-the-python-3-installer.
- Clone the repository to any local path.
- Note: This has been created using Python environment in order to have all dependencies in the same folder rather than taking the packages for the global python configuration.
- To run these tests, you need to download the Geko-Driver file for managing the Firefox browser and ChromeDriver for Google Chrome. You can download the file here:

  - https://sites.google.com/a/chromium.org/chromedriver/downloads
  - https://github.com/mozilla/geckodriver/releases
Download and and unzip it into the:  C:\geckodriver folder on Windows, /usr/local / bin on Ubuntu and macOS.

 - After you download these files, you need to install
all dependencies:
```shell
pip3 install -r requirements.txt
```
#How to run it


To run all tests type:
```shell
pytest -s -v test_booking/test_booking_page.py
```
To run test scenario 1 type:
```shell
pytest -s -v -m scenario_1 test_booking/test_booking_page.py 
```
or
```shell
pytest -s -v test_booking/test_booking_page.py::TestUserIsAbleToSpecifyAgeOfEachChild
``` 
To run test scenario 2 type:
```shell
pytest -s -v -m scenario_2 test_booking/test_booking_page.py 
```
or
```shell
pytest -s -v test_booking/test_booking_page.py::TestUserIsRequiredToSpecifyBookingDateToSeeBookingPrice 
```

- Optional parameters:
  - -v : verbose (trace import statements)
  - -browser_name=firefox  :to choose Firefox browser, default is Chrome
#Technologies used
- Python 3.
- Selenium Package.
- Chromedriver and geckodriver for Chrome and Firefox web drivers respectively.
- Pytest in order to have test cases.
