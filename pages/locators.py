from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators:
    ADD_TO_CARD = (By.XPATH, "//button[text()='Добавить в корзину']")
    MESSAGE_ABOUT_ADDING = (By.CSS_SELECTOR, "div.alertinner")
    MESSAGE_ABOUT_ADDING_PRODUCT_NAME = (By.CSS_SELECTOR, "#messages div:nth-child(1) div strong")
    PRODUCT_NAME = (By.CSS_SELECTOR, "div.product_main h1")
    MESSAGE_BASKET_TOTAL = (By.CSS_SELECTOR, ".alert-info .alertinner strong")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    SHOW_TO_BASKET = (By.XPATH, "//a[@class ='btn btn-default']")


class BasketPageLockators:
    GET_PURCHASE = (By.XPATH, "//a[@class='btn btn-lg btn-primary btn-block']")
    EMPTY_BASKET_TEXT = (By.CSS_SELECTOR, "#content_inner>p")
