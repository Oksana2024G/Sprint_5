from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from curl import *
from data import Credentials
from locators import Locators

class TestTransition:
    def test_Transition_to_constructor_from_accaunt(self, driver):
        driver.find_element(*Locators.LOGIN_ACCOUNT_BUTTON).click()
        driver.find_element(*Locators.EMAIL).send_keys(Credentials.email)
        WebDriverWait(driver, 10).until(ec.visibility_of_element_located((Locators.EMAIL)))
        driver.find_element(*Locators.PASSWORD).send_keys(Credentials.password)
        WebDriverWait(driver, 10).until(ec.visibility_of_element_located((Locators.PASSWORD)))
        driver.find_element(*Locators.LOGIN_BUTTON_FORM).click()
        WebDriverWait(driver, 10).until(ec.visibility_of_element_located((Locators.PLACE_ORDER_BUTTON)))
        driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 3).until(ec.visibility_of_element_located((Locators.PROFILE)))
        driver.find_element(*Locators.CONSTRUCTOR).click()
        WebDriverWait(driver, 10).until(ec.url_to_be(main_site))

        assert driver.current_url == main_site

    def test_Transition_to_constructor_by_logo(self, driver):
        driver.find_element(*Locators.LOGIN_ACCOUNT_BUTTON).click()
        driver.find_element(*Locators.EMAIL).send_keys(Credentials.email)
        WebDriverWait(driver, 10).until(ec.visibility_of_element_located((Locators.EMAIL)))
        driver.find_element(*Locators.PASSWORD).send_keys(Credentials.password)
        WebDriverWait(driver, 10).until(ec.visibility_of_element_located((Locators.PASSWORD)))
        driver.find_element(*Locators.LOGIN_BUTTON_FORM).click()
        WebDriverWait(driver, 10).until(ec.visibility_of_element_located((Locators.PLACE_ORDER_BUTTON)))
        driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 3).until(ec.visibility_of_element_located((Locators.PROFILE)))
        driver.find_element(*Locators.LOGO).click()
        WebDriverWait(driver, 10).until(ec.url_to_be(main_site))

        assert driver.current_url == main_site
