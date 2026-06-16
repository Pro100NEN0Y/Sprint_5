from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import StellarBurgersLocators as Locators

class TestConstructor:
    def test_go_to_sauces_section(self, driver):
        driver.find_element(*Locators.MAIN_SAUCES_SECTION).click()
        active_section = WebDriverWait(driver, 3).until(
            EC.visibility_of_element_located(Locators.MAIN_SAUCES_SECTION)
        )
        assert active_section.is_displayed()

    def test_go_to_fillings_section(self, driver):
        driver.find_element(*Locators.MAIN_FILLINGS_SECTION).click()
        active_section = WebDriverWait(driver, 3).until(
            EC.visibility_of_element_located(Locators.MAIN_FILLINGS_SECTION)
        )
        assert active_section.is_displayed()

    def test_go_to_buns_section(self, driver):
        driver.find_element(*Locators.MAIN_SAUCES_SECTION).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.MAIN_SAUCES_SECTION))
        driver.find_element(*Locators.MAIN_BUNS_SECTION).click()
        active_section = WebDriverWait(driver, 3).until(
            EC.visibility_of_element_located(Locators.MAIN_BUNS_SECTION)
        )
        assert active_section.is_displayed()