import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.locators import (
    InventoryPageLocators,
    CartPageLocators,
    CheckoutPageLocators,
)


class TestPurchase:

    def test_successful_purchase(self, logged_in_user):
        """Полный сценарий успешной покупки товара."""
        driver = logged_in_user

        # Добавляем первый товар в корзину
        add_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(InventoryPageLocators.ADD_TO_CART_BUTTON)
        )
        add_button.click()

        # Переходим в корзину
        cart_link = driver.find_element(*InventoryPageLocators.CART_LINK)
        cart_link.click()

        # Нажимаем Checkout
        checkout_btn = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(CartPageLocators.CHECKOUT_BUTTON)
        )
        checkout_btn.click()

        # Заполняем форму
        driver.find_element(*CheckoutPageLocators.FIRST_NAME_INPUT).send_keys("Иван")
        driver.find_element(*CheckoutPageLocators.LAST_NAME_INPUT).send_keys("Петров")
        driver.find_element(*CheckoutPageLocators.POSTAL_CODE_INPUT).send_keys("123456")
        driver.find_element(*CheckoutPageLocators.CONTINUE_BUTTON).click()

        # Завершаем покупку
        finish_btn = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(CheckoutPageLocators.FINISH_BUTTON)
        )
        finish_btn.click()

        # Проверяем сообщение об успешном завершении
        complete_header = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(CheckoutPageLocators.COMPLETE_HEADER)
        )
        header_text = complete_header.text
        assert header_text == "Thank you for your order!", \
            f"Ожидалось 'Thank you for your order!', получено '{header_text}'"