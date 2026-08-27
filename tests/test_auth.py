# Тесты авторизации
import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.locators import LoginPageLocators, InventoryPageLocators


class TestAuthentication:

    def test_successful_login(self, driver):
        """Проверка успешной авторизации с валидными данными."""
        driver.get("https://www.saucedemo.com/")
        driver.find_element(*LoginPageLocators.USERNAME_INPUT).send_keys("standard_user")
        driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys("secret_sauce")
        driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()

        # Ожидаем появления заголовка страницы товаров
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(InventoryPageLocators.PAGE_TITLE)
        )
        title = driver.find_element(*InventoryPageLocators.PAGE_TITLE).text
        assert title == "Products", f"Ожидался заголовок 'Products', получен '{title}'"

    def test_failed_login(self, driver):
        """Проверка появления сообщения об ошибке при неверных учётных данных."""
        driver.get("https://www.saucedemo.com/")
        driver.find_element(*LoginPageLocators.USERNAME_INPUT).send_keys("locked_out_user")
        driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys("secret_sauce")
        driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()

        error = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(LoginPageLocators.ERROR_MESSAGE)
        )
        error_text = error.text
        assert "Epic sadface" in error_text, f"Ожидалось сообщение об ошибке, получено: '{error_text}'"