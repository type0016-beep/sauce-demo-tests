# Локаторы для SauceDemo

"""
Модуль содержит все локаторы, используемые в тестах.
Локаторы сгруппированы по страницам.
"""


class LoginPageLocators:
    USERNAME_INPUT = ("id", "user-name")
    PASSWORD_INPUT = ("id", "password")
    LOGIN_BUTTON = ("id", "login-button")
    ERROR_MESSAGE = ("css selector", "h3[data-test='error']")


class InventoryPageLocators:
    PAGE_TITLE = ("css selector", "span.title")
    ADD_TO_CART_BUTTON = ("css selector", "button.btn_primary.btn_inventory")
    CART_LINK = ("css selector", "a.shopping_cart_link")
    CART_BADGE = ("css selector", "span.shopping_cart_badge")


class CartPageLocators:
    PAGE_TITLE = ("css selector", "span.title")
    CHECKOUT_BUTTON = ("css selector", "button#checkout")
    REMOVE_BUTTON = ("css selector", "button.btn_secondary.btn_small.cart_button")
    CART_ITEM = ("css selector", "div.cart_item")
    CONTINUE_SHOPPING_BUTTON = ("css selector", "button#continue-shopping")


class CheckoutPageLocators:
    FIRST_NAME_INPUT = ("id", "first-name")
    LAST_NAME_INPUT = ("id", "last-name")
    POSTAL_CODE_INPUT = ("id", "postal-code")
    CONTINUE_BUTTON = ("css selector", "input#continue")
    FINISH_BUTTON = ("css selector", "button#finish")
    COMPLETE_HEADER = ("css selector", "h2.complete-header")
    COMPLETE_TEXT = ("css selector", "div.complete-text")