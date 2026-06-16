from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import StellarBurgersLocators as Locators
from data import Urls, UserData

class TestLogout:
    def test_logout_from_personal_account(self, driver):
        driver.find_element(*Locators.MAIN_LOGIN_BUTTON).click()
        driver.find_element(*Locators.LOGIN_EMAIL_INPUT).send_keys(UserData.EXISTING_EMAIL)
        driver.find_element(*Locators.LOGIN_PASSWORD_INPUT).send_keys(UserData.EXISTING_PASSWORD)
        driver.find_element(*Locators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 3).until(EC.url_to_be(Urls.BASE_URL))

        driver.find_element(*Locators.MAIN_PROFILE_BUTTON).click()
        WebDriverWait(driver, 3).until(EC.url_contains('/account'))

        driver.find_element(*Locators.PROFILE_LOGOUT_BUTTON).click()
        WebDriverWait(driver, 3).until(EC.url_to_be(Urls.LOGIN_URL))
        assert driver.current_url == Urls.LOGIN_URL