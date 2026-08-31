import pytest
import allure
from selenium import webdriver
from locators.locators import LoginPageLocators


@pytest.fixture(scope="session")
def driver():
    with allure.step("Инициализировать WebDriver (Chrome)"):
        options = webdriver.ChromeOptions()
        # options.add_argument("--headless")  # раскомментируйте при необходимости
        driver = webdriver.Chrome(options=options)
    yield driver
    with allure.step("Закрыть браузер"):
        driver.quit()


@pytest.fixture
def logged_in_user(driver):
    """
    Фикстура выполняет авторизацию с валидными данными и возвращает драйвер.
    Используется в тестах покупки и корзины.
    """
    with allure.step("Открыть страницу входа"):
        driver.get("https://www.saucedemo.com/")

    with allure.step("Ввести логин и пароль"):
        driver.find_element(*LoginPageLocators.USERNAME_INPUT).send_keys("standard_user")
        driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys("secret_sauce")
        driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()

    return driver