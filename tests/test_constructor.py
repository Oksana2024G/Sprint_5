from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from locators import Locators

class TestConstructorSections:
    def test_go_to_sauces_section(self, driver):
        driver.find_element(*Locators.SAUCES_BUTTON).click()
        WebDriverWait(driver, 10).until(ec.visibility_of_element_located((Locators.SAUCES_MENU)))
        sauses_section = driver.find_element(*Locators.SAUCES_MENU)
        assert sauses_section.text == 'Соусы'

    def test_go_to_fillings_section(self, driver):
        driver.find_element(*Locators.FILLINGS_BUTTON).click()
        WebDriverWait(driver, 10).until(ec.visibility_of_element_located((Locators.FILLINGS_MENU)))
        fillings_section = driver.find_element(*Locators.FILLINGS_MENU)
        assert fillings_section.text == 'Начинки'

    def test_go_to_buns_section(self, driver):
        driver.find_element(*Locators.SAUCES_BUTTON).click()
        driver.find_element(*Locators.BUNS_BUTTON).click()
        WebDriverWait(driver, 10).until(ec.visibility_of_element_located((Locators.BUNS_MENU)))
        buns_section = driver.find_element(*Locators.BUNS_MENU)
        assert buns_section.text == 'Булки'
