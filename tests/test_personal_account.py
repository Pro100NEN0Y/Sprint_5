from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import StellarBurgersLocators as Locators
from data import Urls, UserData

class TestPersonalAccount:
    def test_go_to_personal_account(self, driver):
        driver.find_element(*Locators.MAIN_LOGIN_BUTTON).click()
        driver.find_element(*Locators.LOGIN_EMAIL_INPUT).send_keys(UserData.EXISTING_EMAIL)
        driver.find_element(*Locators.LOGIN_PASSWORD_INPUT).send_keys(UserData.EXISTING_PASSWORD)
        driver.find_element(*Locators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 3).until(EC.url_to_be(Urls.BASE_URL))

        driver.find_element(*Locators.MAIN_PROFILE_BUTTON).click()
        WebDriverWait(driver, 3).until(EC.url_contains('/account'))
        assert '/account' in driver.current_url

    def test_go_to_constructor_from_personal_account(self, driver):
        driver.find_element(*Locators.MAIN_LOGIN_BUTTON).click()
        driver.find_element(*Locators.LOGIN_EMAIL_INPUT).send_keys(UserData.EXISTING_EMAIL)
        driver.find_element(*Locators.LOGIN_PASSWORD_INPUT).send_keys(UserData.EXISTING_PASSWORD)
        driver.find_element(*Locators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 3).until(EC.url_to_be(Urls.BASE_URL))
        driver.find_element(*Locators.MAIN_PROFILE_BUTTON).click()
        WebDriverWait(driver, 3).until(EC.url_contains('/account'))

        driver.find_element(*Locators.MAIN_CONSTRUCTOR_BUTTON).click()
        WebDriverWait(driver, 3).until(EC.url_to_be(Urls.BASE_URL))
        assert driver.current_url == Urls.BASE_URL

    def test_go_to_constructor_by_logo_from_personal_account(self, driver):
        driver.find_element(*Locators.MAIN_LOGIN_BUTTON).click()
        driver.find_element(*Locators.LOGIN_EMAIL_INPUT).send_keys(UserData.EXISTING_EMAIL)
        driver.find_element(*Locators.LOGIN_PASSWORD_INPUT).send_keys(UserData.EXISTING_PASSWORD)
        driver.find_element(*Locators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 3).until(EC.url_to_be(Urls.BASE_URL))
        driver.find_element(*Locators.MAIN_PROFILE_BUTTON).click()
        WebDriverWait(driver, 3).until(EC.url_contains('/account'))

        driver.find_element(*Locators.MAIN_LOGO).click()
        WebDriverWait(driver, 3).until(EC.url_to_be(Urls.BASE_URL))
        assert driver.current_url == Urls.BASE_URL