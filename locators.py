# locators.py
from selenium.webdriver.common.by import By


class StellarBurgersLocators:
  
    # СТРАНИЦА РЕГИСТРАЦИИ
    
    # Поле "Имя"
    REGISTER_NAME_INPUT = (By.XPATH, "//label[text()='Имя']/following-sibling::input")
    # Поле "Email"
    REGISTER_EMAIL_INPUT = (By.XPATH, "//label[text()='Email']/following-sibling::input")
    # Поле "Пароль"
    REGISTER_PASSWORD_INPUT = (By.XPATH, "//label[text()='Пароль']/following-sibling::input")
    # Кнопка "Зарегистрироваться"
    REGISTER_BUTTON = (By.XPATH, "//button[text()='Зарегистрироваться']")
    # Сообщение об ошибке для некорректного пароля
    REGISTER_ERROR_MESSAGE = (By.XPATH, "//p[text()='Некорректный пароль']")

    
    # СТРАНИЦА ВХОДА
    
    # Поле "Email"
    LOGIN_EMAIL_INPUT = (By.XPATH, "//label[text()='Email']/following-sibling::input")
    # Поле "Пароль"
    LOGIN_PASSWORD_INPUT = (By.XPATH, "//input[@type='password']")
    # Кнопка "Войти"
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти']")
    # Ссылка "Зарегистрироваться"
    LOGIN_REGISTER_LINK = (By.XPATH, "//a[text()='Зарегистрироваться']")
    # Ссылка "Восстановить пароль"
    LOGIN_FORGOT_PASSWORD_LINK = (By.XPATH, "//a[text()='Восстановить пароль']")

    
    # ГЛАВНАЯ СТРАНИЦА (КОНСТРУКТОР)
    
    # Кнопка "Войти в аккаунт"
    MAIN_LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти в аккаунт']")
    # Кнопка "Личный Кабинет"
    MAIN_PROFILE_BUTTON = (By.XPATH, "//p[text()='Личный Кабинет']")
    # Кнопка "Конструктор"
    MAIN_CONSTRUCTOR_BUTTON = (By.XPATH, "//a[p[text()='Конструктор']]")
    # Логотип Stellar Burgers (кликабельная ссылка)
    MAIN_LOGO = (By.XPATH, "//a[.//svg[@width='290' and @height='50']]")
    # Раздел "Булки"
    MAIN_BUNS_SECTION = (By.XPATH, "//h2[text()='Булки']")
    # Раздел "Соусы"
    MAIN_SAUCES_SECTION = (By.XPATH, "//h2[text()='Соусы']")
    # Раздел "Начинки"
    MAIN_FILLINGS_SECTION = (By.XPATH, "//h2[text()='Начинки']")

    
    # ЛИЧНЫЙ КАБИНЕТ
    
    # Кнопка "Выход"
    PROFILE_LOGOUT_BUTTON = (By.XPATH, "//button[text()='Выход']")