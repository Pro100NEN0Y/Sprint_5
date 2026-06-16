# helpers.py
import random
from data import UserData

def generate_unique_user():
    # Генерирует уникального пользователя для регистрации
    random_num = random.randint(100, 999)
    email = f"nikita_tihomirov_{random_num}@yandex.ru"
    return {
        "name": UserData.NAME,
        "email": email,
        "password": UserData.EXISTING_PASSWORD # Используем тот же пароль
    }