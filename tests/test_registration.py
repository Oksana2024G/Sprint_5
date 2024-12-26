from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from helper import generate_registration_data
from locators import Locators

class TestRegistrationWithNewCredentials:

    def test_sucsess_registration(self, driver):
        name, email, password = generate_registration_data()
        driver.find_element(*Locators.LOGIN_ACCOUNT_BUTTON).click()
        driver.find_element(*Locators.REG_BUTTON).click()
        driver.find_element(*Locators.NAME).send_keys(name)
        WebDriverWait(driver, 10).until(ec.visibility_of_element_located((Locators.NAME)))
        driver.find_element(*Locators.EMAIL).send_keys(email)
        WebDriverWait(driver, 10).until(ec.visibility_of_element_located((Locators.EMAIL)))
        driver.find_element(*Locators.PASSWORD).send_keys(password)
        WebDriverWait(driver, 10).until(ec.visibility_of_element_located((Locators.PASSWORD)))
        driver.find_element(*Locators.REGISTER_BUTTON).click()
        WebDriverWait(driver, 10).until(ec.element_to_be_clickable((Locators.LOGIN_BUTTON_FORM)))
        assert driver.find_element(*Locators.LOGIN_BUTTON_FORM).is_displayed()

    def test_registration_with_invalid_password(self, driver):
        name, email, password = generate_registration_data()
        driver.find_element(*Locators.LOGIN_ACCOUNT_BUTTON).click()
        driver.find_element(*Locators.REG_BUTTON).click()
        driver.find_element(*Locators.NAME).send_keys(name)
        WebDriverWait(driver, 10).until(ec.visibility_of_element_located((Locators.NAME)))
        driver.find_element(*Locators.EMAIL).send_keys(email)
        WebDriverWait(driver, 10).until(ec.visibility_of_element_located((Locators.EMAIL)))
        driver.find_element(*Locators.PASSWORD).send_keys("345")
        WebDriverWait(driver, 10).until(ec.visibility_of_element_located((Locators.PASSWORD)))
        driver.find_element(*Locators.REGISTER_BUTTON).click()
        WebDriverWait(driver, 10).until(ec.visibility_of_element_located(Locators.ERROR_TEXT))
        error_message = driver.find_element(*Locators.ERROR_TEXT)
        assert error_message.text == "Некорректный пароль"
