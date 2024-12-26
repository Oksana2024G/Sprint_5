from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from data import Credentials
from locators import Locators

class TestLoginWithExistingAccount:
    def test_login_from_main_page(self, driver):
        driver.find_element(*Locators.LOGIN_ACCOUNT_BUTTON).click()
        driver.find_element(*Locators.EMAIL).send_keys(Credentials.email)
        WebDriverWait(driver, 10).until(ec.visibility_of_element_located((Locators.EMAIL)))
        driver.find_element(*Locators.PASSWORD).send_keys(Credentials.password)
        WebDriverWait(driver, 10).until(ec.visibility_of_element_located((Locators.PASSWORD)))
        driver.find_element(*Locators.LOGIN_BUTTON_FORM).click()
        WebDriverWait(driver, 10).until(ec.visibility_of_element_located((Locators.PLACE_ORDER_BUTTON)))
        order_button = driver.find_element(*Locators.PLACE_ORDER_BUTTON)

        assert order_button.text == 'Оформить заказ'


    def test_login_from_account_page(self, driver):
        driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()
        driver.find_element(*Locators.EMAIL).send_keys(Credentials.email)
        WebDriverWait(driver, 10).until(ec.visibility_of_element_located((Locators.EMAIL)))
        driver.find_element(*Locators.PASSWORD).send_keys(Credentials.password)
        WebDriverWait(driver, 10).until(ec.visibility_of_element_located((Locators.PASSWORD)))
        driver.find_element(*Locators.LOGIN_BUTTON_FORM).click()
        WebDriverWait(driver, 10).until(ec.visibility_of_element_located((Locators.PLACE_ORDER_BUTTON)))
        order_button = driver.find_element(*Locators.PLACE_ORDER_BUTTON)

        assert order_button.text == 'Оформить заказ'


    def test_login_from_registration_form(self, driver):
        driver.find_element(*Locators.LOGIN_ACCOUNT_BUTTON).click()
        driver.find_element(*Locators.REG_BUTTON).click()
        driver.find_element(*Locators.LINK_LOGIN).click()
        driver.find_element(*Locators.EMAIL).send_keys(Credentials.email)
        WebDriverWait(driver, 10).until(ec.visibility_of_element_located((Locators.EMAIL)))
        driver.find_element(*Locators.PASSWORD).send_keys(Credentials.password)
        WebDriverWait(driver, 10).until(ec.visibility_of_element_located((Locators.PASSWORD)))
        driver.find_element(*Locators.LOGIN_BUTTON_FORM).click()
        WebDriverWait(driver, 10).until(ec.visibility_of_element_located((Locators.PLACE_ORDER_BUTTON)))
        order_button = driver.find_element(*Locators.PLACE_ORDER_BUTTON)

        assert order_button.text == 'Оформить заказ'


    def test_login_from_forgot_password_form(self, driver):
        driver.find_element(*Locators.LOGIN_ACCOUNT_BUTTON).click()
        driver.find_element(*Locators.FORGOT_PASSWORD_LINK).click()
        driver.find_element(*Locators.LINK_LOGIN).click()
        driver.find_element(*Locators.EMAIL).send_keys(Credentials.email)
        WebDriverWait(driver, 10).until(ec.visibility_of_element_located((Locators.EMAIL)))
        driver.find_element(*Locators.PASSWORD).send_keys(Credentials.password)
        WebDriverWait(driver, 10).until(ec.visibility_of_element_located((Locators.PASSWORD)))
        driver.find_element(*Locators.LOGIN_BUTTON_FORM).click()
        WebDriverWait(driver, 10).until(ec.visibility_of_element_located((Locators.PLACE_ORDER_BUTTON)))
        order_button = driver.find_element(*Locators.PLACE_ORDER_BUTTON)

        assert order_button.text == 'Оформить заказ'
