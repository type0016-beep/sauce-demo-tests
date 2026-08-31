import allure
import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.locators import (
    InventoryPageLocators,
    CartPageLocators,
    CheckoutPageLocators,
)


@allure.suite("Тесты оформления заказа")
class TestPurchase:

    @allure.title("Успешное оформление покупки")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.tag("smoke", "purchase", "positive")
    @allure.label("owner", "student")
    @allure.label("layer", "UI")
    def test_successful_purchase(self, logged_in_user):
        """Полный сценарий успешной покупки товара."""
        driver = logged_in_user

        with allure.step("Добавить первый товар в корзину"):
            add_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable(InventoryPageLocators.ADD_TO_CART_BUTTON)
            )
            add_button.click()

        with allure.step("Перейти в корзину"):
            cart_link = driver.find_element(*InventoryPageLocators.CART_LINK)
            cart_link.click()

        with allure.step("Нажать кнопку Checkout"):
            checkout_btn = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable(CartPageLocators.CHECKOUT_BUTTON)
            )
            checkout_btn.click()

        with allure.step("Заполнить форму данными покупателя"):
            driver.find_element(*CheckoutPageLocators.FIRST_NAME_INPUT).send_keys("Иван")
            driver.find_element(*CheckoutPageLocators.LAST_NAME_INPUT).send_keys("Петров")
            driver.find_element(*CheckoutPageLocators.POSTAL_CODE_INPUT).send_keys("123456")

        with allure.step("Нажать кнопку Continue"):
            driver.find_element(*CheckoutPageLocators.CONTINUE_BUTTON).click()

        with allure.step("Нажать кнопку Finish"):
            finish_btn = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable(CheckoutPageLocators.FINISH_BUTTON)
            )
            finish_btn.click()

        with allure.step("Проверить сообщение об успешном завершении"):
            complete_header = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located(CheckoutPageLocators.COMPLETE_HEADER)
            )
            header_text = complete_header.text
            assert header_text == "Thank you for your order!", \
                f"Ожидалось 'Thank you for your order!', получено '{header_text}'"