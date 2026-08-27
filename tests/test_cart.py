# Тесты очистки корзины
import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.locators import InventoryPageLocators, CartPageLocators


class TestCart:

    def test_clear_cart(self, logged_in_user):
        """Добавление товара в корзину, очистка и проверка пустой корзины."""
        driver = logged_in_user

        # Добавляем два товара
        add_buttons = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located(InventoryPageLocators.ADD_TO_CART_BUTTON)
        )
        add_buttons[0].click()
        add_buttons[1].click()

        # Проверяем, что на иконке корзины отображается количество "2"
        badge = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(InventoryPageLocators.CART_BADGE)
        )
        assert badge.text == "2", f"Ожидалось количество товаров 2, получено {badge.text}"

        # Переходим в корзину
        driver.find_element(*InventoryPageLocators.CART_LINK).click()

        # Убеждаемся, что в корзине есть товары
        items = driver.find_elements(*CartPageLocators.CART_ITEM)
        assert len(items) == 2, f"Ожидалось 2 товара в корзине, найдено {len(items)}"

        # Удаляем все товары (нажимаем Remove для каждого)
        remove_buttons = driver.find_elements(*CartPageLocators.REMOVE_BUTTON)
        for btn in remove_buttons:
            btn.click()

        # Проверяем, что корзина пуста
        items_after = driver.find_elements(*CartPageLocators.CART_ITEM)
        assert len(items_after) == 0, f"Корзина должна быть пуста, но найдено товаров: {len(items_after)}"

        # Проверяем, что пользователь на странице корзины или может вернуться к покупкам
        # Ожидаем, что заголовок страницы "Your Cart" (корзина пуста, но мы на странице корзины)
        # Согласно сценарию можно проверить, что корзина пуста и доступна кнопка Continue Shopping
        continue_btn = driver.find_element(*CartPageLocators.CONTINUE_SHOPPING_BUTTON)
        assert continue_btn.is_displayed(), "Кнопка Continue Shopping не отображается"