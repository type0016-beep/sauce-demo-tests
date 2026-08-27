import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from locators.locators import LoginPageLocators


@pytest.fixture(scope="session")
def driver():
    """
    Фикстура инициализирует WebDriver (Chrome) с автоматическим управлением драйвером.
    Закрывает браузер после завершения всех тестов.
    """
    service = Service(ChromeDriverManager().install())
    options = webdriver.ChromeOptions()
    # Для запуска в фоновом режиме (если нужно) раскомментируйте:
    # options.add_argument("--headless")
    driver = webdriver.Chrome(service=service, options=options)
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture
def logged_in_user(driver):
    """
    Фикстура выполняет авторизацию с валидными данными и возвращает драйвер.
    Используется в тестах покупки и корзины.
    """
    driver.get("https://www.saucedemo.com/")
    username = driver.find_element(*LoginPageLocators.USERNAME_INPUT)
    password = driver.find_element(*LoginPageLocators.PASSWORD_INPUT)
    login_button = driver.find_element(*LoginPageLocators.LOGIN_BUTTON)

    username.send_keys("standard_user")
    password.send_keys("secret_sauce")
    login_button.click()
    return driver