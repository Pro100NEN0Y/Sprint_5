# Фикстура для запуска и закрытия браузера
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from data import Urls

@pytest.fixture
def driver():
    options = Options()
    driver = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install()),
        options=options
    )
    driver.get(Urls.BASE_URL)  # Открываем главную страницу
    yield driver  # Передаем driver в тест
    driver.quit() # Закрываем браузер