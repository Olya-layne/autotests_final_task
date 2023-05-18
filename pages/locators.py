from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators():
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, ".add-to-basket .btn")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages :nth-child(1) > .alertinner")
    BASKET_MESSAGE = (By.XPATH, "//div/div/div/p")
    BOOK_NAME = (By.TAG_NAME, "h1")
    BOOK_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
