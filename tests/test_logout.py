from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from data import Credentials
from locators import Locators

class TestLogoutFromExistingAccount:
    def test_logout(self, driver):
        driver.find_element(*Locators.LOGIN_ACCOUNT_BUTTON).click()
        driver.find_element(*Locators.EMAIL).send_keys(Credentials.email)
        WebDriverWait(driver, 10).until(ec.visibility_of_element_located((Locators.EMAIL)))
        driver.find_element(*Locators.PASSWORD).send_keys(Credentials.password)
        WebDriverWait(driver, 10).until(ec.visibility_of_element_located((Locators.PASSWORD)))
        driver.find_element(*Locators.LOGIN_BUTTON_FORM).click()
        WebDriverWait(driver, 10).until(ec.visibility_of_element_located((Locators.PLACE_ORDER_BUTTON)))
        driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 3).until(ec.visibility_of_element_located((Locators.LOGOUT_BUTTON)))
        driver.find_element(*Locators.LOGOUT_BUTTON).click()
        WebDriverWait(driver, 10).until(ec.visibility_of_element_located(Locators.LOGIN_BUTTON_FORM))

        assert driver.find_element(*Locators.LOGIN_BUTTON_FORM).is_displayed()
