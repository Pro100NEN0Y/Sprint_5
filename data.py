class Urls:
    BASE_URL = 'https://stellarburgers.education-services.ru/'
    REGISTER_URL = f'{BASE_URL}register'
    LOGIN_URL = f'{BASE_URL}login'
    FORGOT_PASSWORD_URL = f'{BASE_URL}forgot-password'

class UserData:
    # Данные для тестового пользователя, который уже создан в системе
    EXISTING_EMAIL = "NikitaTihomirov48111@yandex.ru"
    EXISTING_PASSWORD = "123456"
    NAME = "Никита"

    # Данные для теста регистрации нового пользователя
    INVALID_PASSWORD = "123"