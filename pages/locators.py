from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators:
    ADD_TO_BASKET = (By.CSS_SELECTOR, "#add_to_basket_form > button")

    ITEM_NAME = (By.XPATH, "/html[1]/body[1]/div[2]/div[1]/div[2]/div[2]/article[1]/div[1]/div[2]/h1[1]")
    ADDED_ITEM = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > div > strong")

    PRODUCT_PRICE = (By.XPATH, "/html[1]/body[1]/div[2]/div[1]/div[2]/div[2]/article[1]/div[1]/div[2]/p[1]")
    TOTAL_PRICE = (By.XPATH, "/html/body/div[2]/div/div[1]/div[3]/div/p[1]/strong")
