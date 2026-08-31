import allure
import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.locators import LoginPageLocators, InventoryPageLocators


@allure.suite("Тесты авторизации")
class TestAuthentication:

    @allure.title("Успешный вход с корректными учетными данными")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.tag("smoke", "login", "positive")
    @allure.label("owner", "student")
    @allure.label("layer", "UI")
    def test_successful_login(self, driver):
        """Проверка успешной авторизации с валидными данными."""
        with allure.step("Открыть страницу входа"):
            driver.get("https://www.saucedemo.com/")

        with allure.step("Ввести имя пользователя 'standard_user'"):
            driver.find_element(*LoginPageLocators.USERNAME_INPUT).send_keys("standard_user")

        with allure.step("Ввести пароль 'secret_sauce'"):
            driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys("secret_sauce")

        with allure.step("Нажать кнопку Login"):
            driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()

        with allure.step("Дождаться загрузки страницы товаров"):
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located(InventoryPageLocators.PAGE_TITLE)
            )

        with allure.step("Проверить заголовок страницы"):
            title = driver.find_element(*InventoryPageLocators.PAGE_TITLE).text
            assert title == "Products", f"Ожидался заголовок 'Products', получен '{title}'"

    @allure.title("Неудачный вход с заблокированным пользователем")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.tag("smoke", "login", "negative")
    @allure.label("owner", "student")
    @allure.label("layer", "UI")
    def test_failed_login(self, driver):
        """Проверка появления сообщения об ошибке при неверных учётных данных."""
        with allure.step("Открыть страницу входа"):
            driver.get("https://www.saucedemo.com/")

        with allure.step("Ввести имя пользователя 'locked_out_user'"):
            driver.find_element(*LoginPageLocators.USERNAME_INPUT).send_keys("locked_out_user")

        with allure.step("Ввести пароль 'secret_sauce'"):
            driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys("secret_sauce")

        with allure.step("Нажать кнопку Login"):
            driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()

        with allure.step("Дождаться появления сообщения об ошибке"):
            error = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located(LoginPageLocators.ERROR_MESSAGE)
            )

        with allure.step("Проверить текст ошибки"):
            error_text = error.text
            assert "Epic sadface" in error_text, f"Ожидалось сообщение об ошибке, получено: '{error_text}'"