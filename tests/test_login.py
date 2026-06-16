from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import StellarBurgersLocators as Locators
from data import Urls, UserData

class TestLogin:
    def test_login_from_main_page(self, driver):
        driver.find_element(*Locators.MAIN_LOGIN_BUTTON).click()
        driver.find_element(*Locators.LOGIN_EMAIL_INPUT).send_keys(UserData.EXISTING_EMAIL)
        driver.find_element(*Locators.LOGIN_PASSWORD_INPUT).send_keys(UserData.EXISTING_PASSWORD)
        driver.find_element(*Locators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 3).until(EC.url_to_be(Urls.BASE_URL))
        assert driver.current_url == Urls.BASE_URL

    def test_login_from_personal_account(self, driver):
        driver.find_element(*Locators.MAIN_PROFILE_BUTTON).click()
        driver.find_element(*Locators.LOGIN_EMAIL_INPUT).send_keys(UserData.EXISTING_EMAIL)
        driver.find_element(*Locators.LOGIN_PASSWORD_INPUT).send_keys(UserData.EXISTING_PASSWORD)
        driver.find_element(*Locators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 3).until(EC.url_to_be(Urls.BASE_URL))
        assert driver.current_url == Urls.BASE_URL

    def test_login_from_registration_form(self, driver):
        driver.get(Urls.REGISTER_URL)
        driver.find_element(*Locators.REGISTER_LOGIN_LINK).click()
        driver.find_element(*Locators.LOGIN_EMAIL_INPUT).send_keys(UserData.EXISTING_EMAIL)
        driver.find_element(*Locators.LOGIN_PASSWORD_INPUT).send_keys(UserData.EXISTING_PASSWORD)
        driver.find_element(*Locators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 3).until(EC.url_to_be(Urls.BASE_URL))
        assert driver.current_url == Urls.BASE_URL

    def test_login_from_forgot_password_form(self, driver):
        driver.get(Urls.FORGOT_PASSWORD_URL)
        driver.find_element(*Locators.LOGIN_REGISTER_LINK).click()
        driver.find_element(*Locators.LOGIN_EMAIL_INPUT).send_keys(UserData.EXISTING_EMAIL)
        driver.find_element(*Locators.LOGIN_PASSWORD_INPUT).send_keys(UserData.EXISTING_PASSWORD)
        driver.find_element(*Locators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 3).until(EC.url_to_be(Urls.BASE_URL))
        assert driver.current_url == Urls.BASE_URL