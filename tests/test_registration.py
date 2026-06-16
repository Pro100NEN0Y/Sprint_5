import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import StellarBurgersLocators as Locators
from data import Urls, UserData
from helpers import generate_unique_user

class TestRegistration:
    def test_successful_registration(self, driver):
        # Клик по кнопке "Личный Кабинет" на главной
        driver.find_element(*Locators.MAIN_PROFILE_BUTTON).click()
        # Клик по ссылке "Зарегистрироваться" на странице входа
        driver.find_element(*Locators.LOGIN_REGISTER_LINK).click()
        # Ожидание загрузки формы регистрации
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.REGISTER_NAME_INPUT))

        # Генерация уникального пользователя
        user = generate_unique_user()
        driver.find_element(*Locators.REGISTER_NAME_INPUT).send_keys(user["name"])
        driver.find_element(*Locators.REGISTER_EMAIL_INPUT).send_keys(user["email"])
        driver.find_element(*Locators.REGISTER_PASSWORD_INPUT).send_keys(user["password"])
        driver.find_element(*Locators.REGISTER_BUTTON).click()

        # Проверка: после регистрации перенаправляет на страницу входа
        WebDriverWait(driver, 3).until(EC.url_to_be(Urls.LOGIN_URL))
        assert driver.current_url == Urls.LOGIN_URL

    def test_registration_invalid_password_error(self, driver):
        # Клик по кнопке "Личный Кабинет" на главной
        driver.find_element(*Locators.MAIN_PROFILE_BUTTON).click()
        # Клик по ссылке "Зарегистрироваться" на странице входа
        driver.find_element(*Locators.LOGIN_REGISTER_LINK).click()
        # Ожидание загрузки формы регистрации
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.REGISTER_NAME_INPUT))

        # Генерация уникального пользователя с некорректным паролем
        user = generate_unique_user()
        driver.find_element(*Locators.REGISTER_NAME_INPUT).send_keys(user["name"])
        driver.find_element(*Locators.REGISTER_EMAIL_INPUT).send_keys(user["email"])
        driver.find_element(*Locators.REGISTER_PASSWORD_INPUT).send_keys(UserData.INVALID_PASSWORD)
        driver.find_element(*Locators.REGISTER_BUTTON).click()

        # Проверка появления ошибки
        error_element = WebDriverWait(driver, 3).until(
            EC.visibility_of_element_located(Locators.REGISTER_ERROR_MESSAGE)
        )
        assert error_element.is_displayed()
        assert driver.current_url == Urls.REGISTER_URL