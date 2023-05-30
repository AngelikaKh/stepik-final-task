from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#incorrect_login_link")

    BASKET_BTN = (By.XPATH, "/html/body/header/div[1]/div/div[2]/span/a")
    EMPTY_BASKET = (By.CSS_SELECTOR, "#content_inner > p")
    NOT_EMPTY_BASKET = (By.CLASS_NAME, "basket-items")

    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

    EMAIL_REG = (By.XPATH, "//input[@id='id_registration-email']")
    PASSWORD_REG = (By.XPATH, "//input[@id='id_registration-password1']")
    CONFIRM_PASSWORD = (By.XPATH, "//input[@id='id_registration-password2']")
    REGISTER_BUTTON = (By.CSS_SELECTOR, "#register_form > button")


class ProductPageLocators:
    ADD_TO_BASKET = (By.CSS_SELECTOR, "#add_to_basket_form > button")

    ITEM_NAME = (By.XPATH, "/html[1]/body[1]/div[2]/div[1]/div[2]/div[2]/article[1]/div[1]/div[2]/h1[1]")
    ADDED_ITEM = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > div > strong")

    PRODUCT_PRICE = (By.XPATH, "/html[1]/body[1]/div[2]/div[1]/div[2]/div[2]/article[1]/div[1]/div[2]/p[1]")
    TOTAL_PRICE = (By.XPATH, "/html/body/div[2]/div/div[1]/div[3]/div/p[1]/strong")

    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages div:nth-child(1)")
