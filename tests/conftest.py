import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

from curl import *


@pytest.fixture(scope="function")
def driver():
    options = Options()
    options.binare_location = "C:/Program Files/Google/Chrome/Application"
    options.add_argument("--windows-size=1200,600")
    service = Service("C:/WebDriver/bin/chromedriver.exe")
    driver = webdriver.Chrome(options = options, service = service)
    driver.get(main_site)
    yield driver
    driver.quit()

