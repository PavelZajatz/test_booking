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

- To run Allure reports, you need install Allure:
  
  1. Linux

    ```shell
    $ sudo apt-add-repository ppa:qameta/allure
    $ sudo apt-get update 
    $ sudo apt-get install allure
    ```
    2. Mac OS X. For Mas OS, automated installation is available via Homebrew
    ```shell
    $ brew install allure
    ```
    3. Windows. For Windows, Allure is available from the Scoop commandline-installer.

To install Allure, download and install Scoop and then execute in the Powershell:

   
    $ scoop install allure
    
Also Scoop is capable of updating Allure distribution installations. To do so navigate to the Scoop installation directory and execute

\bin\checkver.ps1 allure -u
This will check for newer versions of Allure, and update the manifest file. Then execute

scoop update allure

 - After you download these files, you need to install
all dependencies:
```shell
$ pip3 install -r requirements.txt
```
#How to run it


To run all tests type in terminal:
```shell
$ pytest -s -v test_booking/test_booking_page.py
```
To run test scenario 1 type in terminal:
```shell
$ pytest -s -v -m scenario_1 test_booking/test_booking_page.py 
```
or
```shell
$ pytest -s -v test_booking/test_booking_page.py::TestUserIsAbleToSpecifyAgeOfEachChild
``` 
To run test scenario 2 type in terminal:
```shell
$ pytest -s -v -m scenario_2 test_booking/test_booking_page.py 
```
or
```shell
$ pytest -s -v test_booking/test_booking_page.py::TestUserIsRequiredToSpecifyBookingDateToSeeBookingPrice 
```

- Optional parameters:
  - -v : verbose (trace import statements)
  - --browser_name=firefox  :to choose Firefox browser, default is Chrome
  - --alluredir results : to put allure report into the "results" folder
  
#How to run Allure report


To run Allure report type in terminal:
```shell
$ allure serve results
```
  
#Technologies used
- Python 3.
- Selenium Package.
- Chromedriver and geckodriver for Chrome and Firefox web drivers respectively.
- Pytest and Allure in order to have test cases and reports.

