import allure
import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.locators import InventoryPageLocators, CartPageLocators


@allure.suite("Тесты корзины")
class TestCart:

    @allure.title("Очистка корзины после добавления товаров")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.tag("smoke", "cart", "positive")
    @allure.label("owner", "student")
    @allure.label("layer", "UI")
    def test_clear_cart(self, logged_in_user):
        """Добавление товара в корзину, очистка и проверка пустой корзины."""
        driver = logged_in_user

        with allure.step("Добавить два товара в корзину"):
            add_buttons = WebDriverWait(driver, 10).until(
                EC.presence_of_all_elements_located(InventoryPageLocators.ADD_TO_CART_BUTTON)
            )
            add_buttons[0].click()
            add_buttons[1].click()

        with allure.step("Проверить, что на иконке корзины отображается '2'"):
            badge = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located(InventoryPageLocators.CART_BADGE)
            )
            assert badge.text == "2", f"Ожидалось количество товаров 2, получено {badge.text}"

        with allure.step("Перейти в корзину"):
            driver.find_element(*InventoryPageLocators.CART_LINK).click()

        with allure.step("Убедиться, что в корзине два товара"):
            items = driver.find_elements(*CartPageLocators.CART_ITEM)
            assert len(items) == 2, f"Ожидалось 2 товара в корзине, найдено {len(items)}"

        with allure.step("Удалить все товары из корзины"):
            remove_buttons = driver.find_elements(*CartPageLocators.REMOVE_BUTTON)
            for btn in remove_buttons:
                btn.click()

        with allure.step("Проверить, что корзина пуста"):
            items_after = driver.find_elements(*CartPageLocators.CART_ITEM)
            assert len(items_after) == 0, f"Корзина должна быть пуста, но найдено товаров: {len(items_after)}"

        with allure.step("Проверить доступность кнопки Continue Shopping"):
            continue_btn = driver.find_element(*CartPageLocators.CONTINUE_SHOPPING_BUTTON)
            assert continue_btn.is_displayed(), "Кнопка Continue Shopping не отображается"